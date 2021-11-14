import os
from logger import Logger
import pathlib
from datetime import *
from config import mediaTypes
from response import getResponse
import time

qualityVal = []
logger = Logger()
docRootPath = str(pathlib.Path().absolute()) + '/assets'

def contentType(content):
    global qualityVal
    qualityVal = []
    content = content.split(',')
    for i in content:
        j = i.split(';')
        if (len(j) > 1):
            qualityVal.append(j[0], float(j[1].split('=')[1]))
    if (qualityVal == []):
        qualityVal.append((content[0], 1.0))
    qualityVal.sort(key=lambda x: x[1], reverse=True)
    return qualityVal


def parseHeadReq(headers, client):
    logger.clientAddr = client
    path = headers[0].split(' ')[1]
    headerValues = {}
    #print(headers)
    for i in headers[1:]:
        try:
            headerField = i[:i.index(':')]
            if(headerField == 'Accept'):
                contentType(i[i.index(':') + 2:len(i) - 1])
                
            headerValues[headerField] = i[i.index(':') + 2:len(i) - 1]
        except:
            pass
    par = []
    for i in qualityVal:
        par.append(list(i)[0])
    cType = ''

    if '*/*' in par or 'text/html' in par:
        cType = 'text/html'
        if '.' in path:
            ext = '.' + path.split('.')[1]
            if ext != '.html':
                extensions = {}
                for i in mediaTypes.keys():
                    extensions[mediaTypes[i]] = i
                if(ext == '.min'):
                    ext = '.js'
                cType = extensions[ext]

    for i in par:
        filePath = path.split('.')[0] + '.' + i.split('/')[1]
        if os.path.exists(docRootPath + filePath):
            cType = i
            break
    try:
        j = headerValues['Accept']

    except:
        j = '*/*'

    if cType == '':
        response = getResponse({'code': 406,
                                'cType': j,
                                'length': 0,
                                'eTag': ''
                                })
        logger.createErrorLog(headers[0], response)
        return response, ''
    try:
        if path == '/':
            path = docRootPath + 'index.html'
        else:
            try:
                try:
                    ext = '.' + path.split('.')[1]
                except:
                    ext = '.' + cType.split('/')[1]
                path = docRootPath + path
            except Exception as e:
                logger.serverError(e)
                for i in par:
                    if os.path.exists(docRootPath + i):
                        cType = i
                        break

        params = {
            'code': 200,
            'length': 0,
            'cType': cType,
            'eTag': '',
        }

        if '.' not in path.split('\n')[-1]:
            path += '.' + cType.split('/')[1]
        file = open(path, 'rb')
        res = file.read()
        params['modified'] = time.ctime(os.path.getmtime(path))
        eTag = str(os.path.getmtime(path)) + str(len(res))
        length = 0
        try:
            length = len(res)
        except:
            pass
        params['eTag'] = eTag
        params['length'] = length
        if 'Cookie' in headerValues.keys():
            params['Cookie'] = headerValues['Cookie']
        
        response = getResponse(params)
        logger.createLog(headers[0], response)
        return response, ""
    
    except FileNotFoundError:
        params['code'] = 404
        params['length'] = 0
        response = getResponse(params)
        logger.createLog(headers[0], response)
        logger.createErrorLog(headers[0], response)
        return response, ''