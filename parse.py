import os

def parseHeaders(data, method):
    body = []
    hdrValues = {}
    if method == 'POST':

        for i in data[1:]:
            if ':' in i:
                hdrField = i[: i.index(':')]
                hdrValues[hdrField] = i[i.index(':') + 2 : len(i) - 1]
            else:
                if i != '\r' and i != '\n':
                    body.append(i)
        return hdrValues, body

    elif method == 'PUT':
        body = []
        for i in data[1:]:
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
    pass


def parsePutReq(headers, clientAddr, rawData):
    pass


def parseDeleteReq(headers, clientAddr, rawData):
    pass


def parseHeadReq(headers, clientAddr, rawData):
    pass
