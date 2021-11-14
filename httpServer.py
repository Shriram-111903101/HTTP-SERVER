import socket
import sys
import os
from methods.post import parsePostReq
from methods.get import parseGetReq
from methods.head import parseHeadReq
from logger import Logger
from response import createResponse
import threading
from config import MAX_REQ
import time
sys.path.append(os.path.abspath(os.path.join('methods')))

logger = Logger()

def handleReq(rawData, clientAddr):
    try:

        data = rawData.decode('ISO-8859-1')
        headers = []
        for i in data.split('\n'):
            headers.append(i)

        method = headers[0].split(' ')[0]
        #httpVersion = headers[0].split(' ')[2]

        if (method == 'GET'):
            return parseGetReq(headers, clientAddr)
        elif (method == 'POST'):
            return parsePostReq(headers, clientAddr, rawData)
        elif (method == 'PUT'):
            return parse.parsePutReq(headers, clientAddr, rawData)
        elif (method == 'DELETE'):
            return parse.parseDeleteReq(headers, clientAddr, rawData)
        elif (method == 'HEAD'):
            return parseHeadReq(headers, clientAddr)
        else:
            logger.serverError(501)
            return createResponse(0, 501)

    except Exception as e:
        logger.createErrorLog(headers[0], 400)
        print(e)
        return createResponse(0, 400)


def connectionType(data):
    headers = data.split('\n')

    for i in headers[1:]:
        header = i[:i.index(':')]
        if (header == "Connection"):
            return i[i.index(':') + 2 : len(i) - 1]


def acceptClient(clientSocket, clientAddr):

    #clientSocket.settimeout(10)

    while True:
        try:
            rawData = clientSocket.recv(65565)
            if not rawData:
                break
            response, res = handleReq(rawData, clientAddr)
            print(response)
            print(res)
            clientSocket.send(response.encode('utf-8'))

            if len(res):
                clientSocket.send(res)
                
            # Close socket if connection type is close
            if (connectionType(rawData.decode()) == "close"):
                clientSocket.close()
                break

        except clientSocket.timeout:
            clientSocket.close()
            break
    return


if __name__ == '__main__':
    try:
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 4003))
        s.listen(90)
        threads = []
        while True:
            clisock, addr = s.accept()
            t = threading.Thread(target=acceptClient, args=(clisock, addr, ))
            t.start()
            threads.append(t)
            print(threading.active_count())

            if threading.active_count() > MAX_REQ:
                t.join()
                print('Limit exceeded. Wait 5 sec')
                time.sleep(5)

        for i in threads:
            i.join()

    except Exception as e:
        print('Internal Error')
        logger.serverError(e)
        sys.exit(1)

