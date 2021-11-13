import socket
import sys
from methods.post import parsePostReq
from logger import Logger
from response import createResponse

logger = Logger()

def handleReq(rawData, clientAddr):

    data = rawData.decode('ISO-8859-1')
    headers = []
    for i in data.split('\n'):
        headers.append(i)

    method = headers[0].split(' ')[0]
    httpVersion = headers[0].split(' ')[2]

    if (method == 'GET'):
        return parse.parseGetReq(headers, clientAddr, rawData)
    elif (method == 'POST'):
        return parsePostReq(headers, clientAddr, rawData)
    elif (method == 'PUT'):
        return parse.parsePutReq(headers, clientAddr, rawData)
    elif (method == 'DELETE'):
        return parse.parseDeleteReq(headers, clientAddr, rawData)
    elif (method == 'HEAD'):
        return parse.parseHeadReq(headers, clientAddr, rawData)
    else:
        logger.serverError(501)
        return createResponse(0, 501)

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
            response, res = handleReq(rawData, clientAddr)

            # send response

            # Close socket if connection type is close
            if (connectionType(rawData.decode()) == "close"):
                clientSocket.close()
                break

        except clientSocket.timeout:
            clientSocket.close()
            break
    return


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 5002))
    s.listen(90)

    while True:
        clisock, addr = s.accept()
        acceptClient(clisock, addr)

