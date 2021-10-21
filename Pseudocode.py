
#Config
PORT = 5000
MAX_CLIENTS = 30
path = <Path of text file>

def findMethod(req):
    do something
    return "GET" or "POST" or "PUT" or "DELETE" or "HEAD"

def createResponse(code):
    do something
    return response

# For accept-encoding
def encodeData(data, encoding):
    do something
    return encodedData

def parseGet(req):
    do something
    return createResponse()

def parsePost(req):
    do something
    return createResponse()

def parsePut(req):
    do something
    return createResponse()

def parseDelete(req):
    do something
    return createResponse()

def parseHead(req):
    do something
    return createResponse()

# Create response and set cookie
def createResponse():
    do something
    setCookies()
    return response

def setCookies():
    do something


def acceptClient(socketOb, addr):
    # Receive requests
    while True:
        request = s.recv()

        method = findMethod(req)
        if method == "GET":
            # Parse request and Generate response according to request
            res = parseGet()
        
        # Same as GET request for other methods
        elif method == "HEAD":
        elif method == "PUT":.
        elif method == "DELETE":
        elif method == "POST":
        else:
            # Generate response with 501 code
            res = createResponse(501)

        #send response to client
        s.send(res)

        if(connectio-type == "close"):
            #close socket
            s.close()
    
#open socket
s = socket()

#bind socket to the PORT
s.bind('', PORT)

s.listen(50)

# Accept client
while True:
    socketOb, addr = s.accept()
    #create thread for client
    t = Thread(target = acceptClient, args = (socketOb, addr,))
    t.start()






