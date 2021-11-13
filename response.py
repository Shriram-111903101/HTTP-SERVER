import datetime
from config import statusCodes
from config import entityHeaders
import random

def getDateTime(offset=0):
    date = datetime.datetime.now() + datetime.timedelta(seconds=offset)
    date = date.strftime('%A, %d %B %Y %H:%M:%S')
    date += ' GMT'
    return date

def createResponse(length, code, resource=None,  
                    lastModified = None,contentType = "text/html; charset = UTF-8",method='', encodeing = "gzip"):

    if code not in statusCodes.keys():
        return
    
    date = getDateTime()
    status = "HTTP/1.1 " + str(code) + " " + statusCodes[code] + "\r\n"
    server = "Server: http-server\r\n"
    entityHed = ("Content-Type: " + contentType + "\r\nDate: " + date + 
                "\r\nContent-Length: " + str(length) +"\r\nConnection: keep-alive\r\nAllow: " 
                + entityHeaders['Allow'] + "\r\n\r\n")
    return status + server + entityHed

def cookie():
    return ('Set-Cookie: ID = cookie' + str(random.randint(1, 1000)) + 
            '; Expires = ' + getDateTime(15) + '; Path = /login\r\n')


def getResponse(headers):
    statusCode = headers['code']
    if statusCode not in statusCodes:
        return

    date = getDateTime()
    status = "HTTP/1.1 " + str(statusCode) + " " + statusCodes[statusCode] + "\r\n"
    server = "Server: http-server\r\n"
    entityHed = ("Content-Type: " + headers['cType'] + "\r\nDate: " + date + 
                "\r\nContent-Length: " + headers['length'] + + "\r\nContent-Language: en-US\r\nConnection: keep-alive\r\nAllow: " 
                + entityHeaders['Allow'] + "\r\n")

    eTag = headers['eTag']
    if eTag != '':
        if 'Cookie' not in headers.keys():
            entityHed += cookie()

        entityHed += 'E-Tag: ' + eTag + '\r\n\r\n'
    else:
        if 'Cookie' not in headers.keys():
            entityHed += cookie()
    return status + server + entityHed



#print(getDateTime(50))

