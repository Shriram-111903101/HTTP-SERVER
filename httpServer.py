from socket import *
import os
import sys
import datetime
import time
from threading import Thread

def http_post(connSock, message, ip, portNo):

	response = ''
	scode = 0
	path = message.split(' ')[1]
	msgBody = message.split('\r\n\r\n')[1]

	if os.path.exists(path):
		scode = 200
		fp = open(path, 'a')
		response += 'HTTP/1.1 ' + str(scode) + ' OK\r\n'
		fp.write(msgBody + '\n')
	else:
		scode = 201
		fp = open(path, 'w')
		response += 'HTTP/1.1 ' + str(scode) + ' Created\r\n'
		fp.write(msgBody + '\n')
	fp.close()

	date = datetime.datetime.now()
	date = date.strftime('%A,%d %B %Y %H:%M:%S')
	date += ' GMT'
	response += 'Date: ' + date + '\r\n'
	response += 'Server: ' + ip + '\r\n'

	lastModified = time.ctime(os.path.getmtime(path))
	l = lastModified.split(' ')
	lastModified = l[0]+', '+l[2]+' '+l[1]+' '+l[-1]+' '+l[3]
	response += 'Last-Modified: ' + lastModified + ' GMT\r\n'
	response += 'Content-Type: text/html\r\n'
	response += '\r\n'

	response = response.encode()
	connSock.send(response)

def http_get(connSock, message, ip, portNo):

	response = ''
	scode = 0
	path = message.split(' ')[1]
	flag = True;

	if os.path.exists(path):
		scode = 200
		fp = open(path, 'r')
		response += 'HTTP/1.1 ' + str(scode) + ' OK\r\n'
		msgBody = fp.read()
		fp.close()
	else:
		scode = 404
		response += 'HTTP/1.1 ' + str(scode) + ' Not Found\r\n'
		flag = False

	date = datetime.datetime.now()
	date = date.strftime('%A,%d %B %Y %H:%M:%S')
	date += ' GMT'
	response += 'Date: ' + date + '\r\n'
	response += 'Server: ' + ip + '\r\n'

	if flag:
		lastModified = time.ctime(os.path.getmtime(path))
		l = lastModified.split(' ')
		lastModified = l[0]+', '+l[2]+' '+l[1]+' '+l[-1]+' '+l[3]
		response += 'Last-Modified: ' + lastModified + ' GMT\r\n'
	response += 'Content-Type: text/html\r\n'
	response += '\r\n'
	if flag:
		response += msgBody

	response = response.encode()
	connSock.send(response)

def handleReq(client, ip, portNo):
	while True:
		message = client.recv(1024).decode()
		method = message.split(' ', 1)[0]
		if method == 'GET':
			http_get(client, message, ip, portNo)
		elif method == 'POST':
			http_post(client, message, ip, portNo)

if __name__ == '__main__':

	ip = '127.0.0.1'
	try:
		portNo = int(sys.argv[1])
	except:
		print("Enter port number as command line argument.")
		sys.exit()

	serversocket = socket(AF_INET, SOCK_STREAM)
	try:
		serversocket.bind(('', portNo))
	except:
		print("Port is already in use.")
		sys.exit()

	serversocket.listen(5)

	while True:
		client, addr = serversocket.accept()
		print(addr)
		th = Thread(target = handleReq, args = (client, ip, portNo,))
		th.start()


		




