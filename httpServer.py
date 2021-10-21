import socket
import sys
import parse


def handleReq(rawData, clientAddr):

    data = rawData.decode()
    headers = []
    for i in data.split('\n'):
        headers.append(i)

    method = headers[0].split(' ')[0]
    httpVersion = headers[0].split(' '[2])

    if (method == 'GET'):
        return parse.parseGetReq(headers, clientAddr, rawData)
    elif (method == 'POST'):
        return parse.parsePostReq(headers, clientAddr, rawData)
    elif (method == 'PUT'):
        return parse.parsePutReq(headers, clientAddr, rawData)
    elif (method == 'DELETE'):
        return parse.parseDeleteReq(headers, clientAddr, rawData)
    elif (method == 'HEAD'):
        return parse.parseHeadReq(headers, clientAddr, rawData)
    else:
        pass

def connectionType(data):
    headers = data.split('\n')

    for i in headers[1:]:
        header = i[:i.index(':')]
        if (header == "Connection"):
            return i[i.index(':') + 2 : len(i) - 1]


def acceptClient(clientSocket, clientAddr):

    clientSocket.settimeout(10)

    while True:
        try:
            rawData = clientSocket.recv(65565)

            response = handleReq(rawData, clientAddr)

            # send response

            # Close socket if connection type is close
            if (connectionType(rawData.decode()) == "close"):
                clientSocket.close()
                break

        except clientSocket.timeout:
            clientSocket.close()
            break
    return



        

