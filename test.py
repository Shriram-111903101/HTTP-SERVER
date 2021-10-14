import sys
from socket import *
import time
import os

portNo = sys.argv[1]

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', int(sys.argv[1])))
username = os.getlogin()

requestPost = "POST /home/" + username + "/output.txt HTTP/1.1\r\n"
requestPost += "HOST: http://127.0.0.1:" + portNo + "\r\n"
requestPost += "User-Agent: Firefox/86\r\n"
requestPost += "Connection: keep-alive\r\n"
requestPost += "Accept: text/html\r\n\r\n"
requestPost += "Hello World!"

s.send(requestPost.encode())
data = s.recv(1024).decode()
print(data)
time.sleep(5)

requestGet = "GET /home/" + username + "/output.txt HTTP/1.1\r\n"
requestGet += "HOST: http://127.0.0.1:" + portNo + "\r\n"
requestGet += "User-Agent: Firefox/86\r\n"
requestGet += "Connection: keep-alive\r\n"
requestGet += "Accept: text/html\r\n\r\n"
requestGet += "Hello World!"

s.send(requestGet.encode())
data = s.recv(1024).decode()
print(data)