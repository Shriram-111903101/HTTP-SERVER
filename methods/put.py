import os
from get import *
import sys
import json
sys.path.append(os.path.abspath(os.path.join('..')))
from response import *
from logger import Logger

docRootPath = DOCUMENT_ROOT
logger = Logger()

def parsePutReq(headers, client, raw = None):

    resource = ''
    f =''
    logger.clientAddr = client
    headerValues, body = parse.parseHeaders(headers, 'PUT')
    path = headers[0].split(' ')[1]

    if path == '/':
        pass
    else:
        path = docRootPath + path

    if os.path.exists(path):
        if os.access(path.os.W_OK):
            f1 = open(path, 'wb')
            responseStatus = 204
        else:
            responseStatus = 403
            res = createResponse(0, responseStatus, headers[0])
            logger.createErrorLog(headers[0], res)
            return (res, "")
    else:
        f1 = open(path, 'wb')
        responseStatus = 201

    headerLength = len("\n".join(headers[:headerValues['index']]))
    f1.write(raw[headerLength + 1:])

    res = createResponse(0, responseStatus, headers[0])
    logger.createLog(headers[0], res)

    return (res, "")