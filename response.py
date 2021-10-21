import datetime
from config import statusCodes

def getDateTime():
    date = datetime.datetime.now()
    date = date.strftime('%A, %d %B %Y %H:%M:%S')
    date += ' GMT'
    return date

def createResponse(length, code):

    if code not in statusCodes.keys():
        return
        
    pass