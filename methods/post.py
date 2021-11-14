from config import ROOT_PATH
from config import mediaTypes
from pathlib import Path
import parse
import response
import os
import sys
from logger import Logger



logger = Logger()

def parsePostReq(headers, clientAddr, rawData=None):
    logger.clientAddr = clientAddr
    resourceLength = len(rawData)
    headerValues, body = parse.parseHeaders(headers, 'POST')
    path = headers[0].split(' ')[1]
    print(headers)
    
    if path == '/':
        path = ROOT_PATH
    else:
        path = ROOT_PATH + path

    if os.path.exists(path):
        responseStatus = 204
    else:
        responseStatus = 201

    if int(headerValues['Content-Length']) != 0:
        contentType = headerValues.get('Content-Type', None)
        data = parse.parseBody(contentType, body, 'POST', headers)

        if 'isFile' in data.keys() and data['isFile']:

            if data['fileType'] in mediaTypes.keys():
                headerLength = data['headerLength']
                data['fileData'] = str(rawData[:-40][headerLength+1:])
                
            else:
                res = response.createResponse(len(body[0]), 415, body[0], None)
                logger.createLog(headers[0], res)
                logger.createErrorLog(headers[0], res)
                print(res)
                return(res, '')

        res = response.createResponse(len(body[0]), responseStatus, None, None)
        logger.createLog(headers[0], res)
        logger.createPostLog(data, headers[0], headerValues, responseStatus)
        return(res, '')

    else:
        data = parse.parseUrl(headers[0])
        res = response.createResponse(len(body[0]), responseStatus, body[0], None)
        logger.createLog(headers[0], res)
        logger.createPostLog(data, headers[0], headerValues, responseStatus)
        return(res, '')


