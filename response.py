import datetime
from config import statusCodes
from config import entityHeaders

def getDateTime():
    date = datetime.datetime.now()
    date = date.strftime('%A, %d %B %Y %H:%M:%S')
    date += ' GMT'
    return date

def createResponse(length, code, resource=None,  
                    lastModified = None,contentType = "text/html; charset = UTF-8",method='', encodeing = "gzip"):

    if code not in statusCodes.keys():
        return
    
    date = getDateTime()
    status = "HTTP/1.1 " + str(code) + " " + statusCodes[code] + "\r\n"
    server = "Server: myHTTP\r\n"
    entityHed = ("Content-Type: " + contentType + "\r\nDate: " + date + 
                "\r\nContent-Length: " + str(length) +"\r\nConnection: keep-alive\r\nAllow: " 
                + entityHeaders['Allow'] + "\r\n\r\n")
    return status + server + entityHed

#print(createResponse(30, 500))
