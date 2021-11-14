from abc import ABCMeta
import pathlib
# Maximum number of threads
MAX_REQ = 30

# Default port
PORT = 5005

absolutePath = str(pathlib.Path().absolute())
ROOT_PATH =  absolutePath + '/assets/'
ACCESSLOG = absolutePath + '/logs/accessLog.txt'
ERRORLOG = absolutePath + '/logs/errorLog.txt'
POSTLOG = absolutePath + '/logs/postLog.txt'

# Status Codes
statusCodes = {
    101 : "Switching Protocols",
    200 : "OK",
    201 : "Created",
    202 : "Accepted",
    203 : "Non-Authoritative Information",
    204 : "No Content",
    205 : "Reset Content",
    206 : "Partial Content",
    300 : "Multiple Choices",
    301 : "Moved Permanently",
    302 : "Found",
    303 : "See Other",
    304 : "Not Modified",
    305 : "Use Proxy",
    307 : "Temporary Redirect",
    400 : "Bad Request",
    401 : "Unauthorized",
    402 : "Payment Required",
    403 : "Forbidden",
    404 : "Not Found",
    405 : "Method Not Allowed",
    406 : "Not Acceptable",
    407 : "Proxy Authentication Required",
    408 : "Request Time-out",
    409 : "Conflict",
    410 : "Gone",
    411 : "Length Required",
    412 : "Precondition Failed",
    413 : "Request Entity Too Large",
    414 : "Request-URI Too Large",
    415 : "Unsupported Media Type",
    416 : "Requested range not satisfiable",
    417 : "Expectation Failed",
    500 : "Internal Server Error",
    501 : "Not Implemented",
    502 : "Bad Gateway",
    503 : "Service Unavailable",
    504 : "Gateway Time-out",
    505 : "HTTP Version Not Supported"
}

fileFormats = {
    "text/html" : ".html",
    "text/css" : ".css",
    "application/gzip" : ".gz",
    "application/json" : ".json",
    "application/javascript" : ".js",
    "application/pdf" : ".pdf",
    "appllication/octet-stream" : ".bin",
    "image/gif" : ".gif",
    "image/vnd.microsoft.icon" : ".ico",
    "image/jpeg" : ".jpg",
    "image/aviff" : ".png",
    "audio/mpeg" : ".mp3",
    "video/mpeg" : ".mpeg"
}

responseHeaders = {
    "Accept-Ranges" : None,
    "Server" : "myHTTP",
    "Age" : 0,
    "ETag" : "0",
    "Location" : 0,
    "Proxy-Authentication" : 0,
    "Retry-After" : 0,
    "WWW-Authenticate" : 0
}

entityHeaders = {
    "Allow" : "GET, HEAD, PUT",
    "Content-Encoding" : ["gzip", "deflate", "br"],
    "Content-Language" : "en",
    "Content-Length" : 0,
    "Content-Range" : 0,
    "Content-Type" : 0,
    "Last-Modified" : 0,
}

mediaTypes = {
    "application/octet-stream": ".bin",
    "application/x-bzip": ".bz",
    "text/css": ".css",
    "application/gzip": ".gz",
    "image/gif": ".gif",
    "text/html": ".html",
    "image/vnd.microsoft.icon": ".ico",
    "image/jpeg": ".jpg",
    "image/aviff": ".png",
    "application/javascript": ".js",
    "application/json": ".json",
    "audio/mpeg": ".mp3",
    "video/mpeg": ".mpeg",
    "application/x-httpd-php": ".php",
    "application/pdf": ".pdf"
}
