
def parseHeaders(data, method):
    
    if method == 'POST':
        body = []
        boundary = ''
        hdrValues = {}

        for i in data[1:]:
            if ':' in i:
                hdrField = i[: i.index(':')]
                hdrValues[hdrField] = i[i.index(':') + 2 : len(i) - 1]

            elif 'boundary' in i:
                boundary = i[-1:i.index('=') + 1]

            elif '--' + boundary in i:
                j = data.index(i)
                body = data[j:]
                return (hdrValues, body)

            else:
                if i != '\r' and i != '\n':
                    body.append(i)
        return (hdrValues, body)

    elif method == 'PUT':
        hdrValues = {}
        body = []
        for i in data[1:]:
            if ':' in i:
                hdrField = i[:i.index(':')]
                hdrValues[hdrField] = i[i.index(':') : + 2 : len(i) - 1]

            else:
                hdrValues['index'] = data.index(i) + 1
                return hdrValues, body

        return hdrValues, body

def parseBody(encodingType, body, method, data):
    if method == 'POST':
        parsedData = {}

        if 'application/x-www-form-urlencoded' in encodingType:
            for i in body:
                i = i.split('&')
                for j in i:
                    j = j.split('=')
                    parsedData[j[0]] = j[1]

        elif 'multipart/form-data' in encodingType:
            boundary = encodingType[encodingType.find('=') + 1:]
            key = ''
            value = ''
            
            parsedData['isFile'] = False

            for i in body[1:]:
                if '----' in i:
                    parsedData[key] = value
                    key = ''
                    value = ''

                elif 'Content-Disposition: form-data' in i:
                    if 'filename=' in i:
                        parsedData['isFile'] = True
                        parsedData['fileType'] = 'text/html'
                        fileName = i[i.index('ename="') + 7:-2]
                        j = data.index(i)
                        headerString = '\n'.join(data[:j+2])
                        parsedData['headerLength'] = len(headerString)
                        if fileName != '':
                            parsedData['filename'] = fileName
                    key = i[i.index('=') + 2: -2]
                    value = body[body.index(i) + 2][:-1]

                elif 'Content-Type' in i or 'filename' in i:
                    fileType = i[i.index(':') + 1:]
                    parsedData['fileType'] = fileType
                    parsedData['isFile'] = True
                    j = data.index(i)
                    headerString = '\n'.join(data[:j+2])
                    parsedData['headerLength'] = len(headerString)

                else:
                    pass
        return parsedData

def parseUrl(header):
    parsedUrl = {}

    url = header.split(' ')[1]
    for i in url[2:]. split('&'):
        i = i.split('=')
        parsedUrl[i[0]] = i[1]
    return parsedUrl

        
