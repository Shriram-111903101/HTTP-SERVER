import os
from pathlib import Path
import sys
from config import ROOT_PATH
import response


def parseHeaders(data, method):
    body = []
    boundary = ''
    hdrValues = {}
    if method == 'POST':

        for i in data[1:data.index('\r')]:
            if ':' in i:
                hdrField = i[: i.index(':')]
                hdrValues[hdrField] = i[i.index(':') + 2 : len(i) - 1]

        for i in data[data.index('\r') + 1:data.index('\r', data.index('\r')+1)]:
            body.append(i[:len(i) - 1])
        return hdrValues, body

    elif method == 'PUT':
        body = []
        for i in data[1:data.index('\r')]:
            if ':' in i:
                hdrField = i[:i.index(':')]
                hdrValues[hdrField] = i[i.index(':') : + 2 : len(i) - 1]

            else:
                hdrValues['index'] = data.index(i) + 1
                return hdrValues, body

        return hdrValues, body

        
def parseGetReq(headers, clientAddr, rawData):
    pass


def parsePostReq(headers, clientAddr, rawData):
    resourceLength = len(rawData)
    headerValues, body = parseHeaders(headers, 'POST')
    path = headers[0].split(' ')[1]

    if path == '/':
        path = ROOT_PATH
    else:
        path = ROOT_PATH + path

    if os.path.exists(path):
        if os.access(path, os.W_OK):
            responseStatus = 204
        else:
            responseStatus = 403
    else:
        responseStatus = 201

    bodyLength = 0
    for i in body:
        bodyLength += len(i)

    res = response.createResponse(bodyLength, responseStatus)


def parsePutReq(headers, clientAddr, rawData):
    pass


def parseDeleteReq(headers, clientAddr, rawData):
    pass


def parseHeadReq(headers, clientAddr, rawData):
    pass


req = ('POST / HTTP/1.1\r\n'+
        'HOST: reqbin.com\r\n'+
        'Accept: application/json\r\n'+
        'Content-Type: application/json\r\n'+
        'Content-Length: 12\r\n\r\n'+
        '"ID": 78912\r\n\r\n')

headers = []
for i in req.split('\n'):
    headers.append(i)

print(headers)
print(parseHeaders(headers, 'POST'))