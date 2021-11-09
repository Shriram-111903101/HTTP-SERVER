import threading
from datetime import datetime, timedelta
import pathlib
import json
import pytz

absolutePath = str(pathlib.Path().absolute())
accessLog = absolutePath + '/logs/accessLog.txt'
errorLog = absolutePath + '/logs/errorLog.txt'
postLog = absolutePath + '/logs/postLog.txt'
logFormat = 'clientIP [dateTime] request response length'
logLevel = '-all'

class Logger():
    def __init__(self):
        self.lock = threading.Lock()

    clientAddr = ''

    def createLog(self, req, res):
        logFile = open(accessLog, 'a')
        res = res.split('\n')
        headers = {}
        for i in res[1:]:
            try:
                headerField = i[:i.index(':')]
                headers[headerField] = i[i.index(':') + 2 : len(i) - 1]
            except:
                pass
        statusCode = res[0].split(' ')[1]
        date = headers['Date'].split(' ')
        date = (date[1] + '/' + date[2] + '/' + date[3] + ':' 
                + date[4] + ' ' + date[5])

        log = (str(self.clientAddr) + ' [' + date + '] ' + 
            ' \"' + req[:len(req) - 1] + '\" ' + str(statusCode) + ' ' +
            str(headers['Content-Length']))

        self.lock.acquire()
        logFile.write(log + '\n')
        logFile.close()
        self.lock.release()

    def createPostLog(self, data, req, headers, statusCode):
        postFile = open(postLog, 'a')
        date = headers.get('Date', None)

        if date:
            date = (date[1] + '/' + date[2] + '/' + date[3] + ':' 
                + date[4] + ' ' + date[5])
        else:
            date = datetime.today()
            date = date.strftime('%a, %d %b %Y %X IST')

        log = (str(self.clientAddr) + ' [' + date + '] ' + 
            ' \"' + req[:len(req) - 1] + '\" ' + str(statusCode) + ' ' +
            str(headers['Content-Length']))

        data = json.dumps(data, indent=4)
        self.lock.acquire()
        postFile.write(log)
        postFile.write(data + '\n')
        postFile.close()
        self.lock.release()
        
    def createErrorLog(self, req, res):
        errorFile = open(errorLog, 'a')
        try:
            res = res.split('\n')
            headers = {}
            for i in res[1:]:
                try:
                    headerField = i[:i.index(':')]
                    headers[headerField] = i[i.index(':') + 2 : len(i) - 1]
                except:
                    pass
            statusCode = res[0].split(' ')[1]
            date = headers['Date'].split(' ')
            date = (date[1] + '/' + date[2] + '/' + date[3] + ':' 
                + date[4] + ' ' + date[5])

            log = (str(self.clientAddr) + ' [' + date + '] ' + 
                ' \"' + req[:len(req) - 1] + '\" ' + str(statusCode) + ' ' +
                str(headers['Content-Length']))
        except:
            log = 'Bad Request [' + res + ']'

        self.lock.acquire()
        errorFile.write(log + '\n')
        errorFile.close()
        self.lock.release()

    def serverError(self, e):
        offset = 0
        date = datetime.now(tz=pytz.utc) + timedelta(seconds=offset)
        time = (' ' + str(date.strftime('%h')) + ':' +
            str(date.strftime('%M')) + ':' + str(date.strftime('%S')) + ' GMT')

        date = (str(date.strftime('%a')) + ', ' + str(date.strftime('%d')) + 
            ' ' + date.strftime('%b') + ' ' + str(date.year)) + time

        file = open(errorLog, 'a')
        file.write(date + e + '\n')
        file.close