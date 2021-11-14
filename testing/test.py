import requests
import sys
import threading
import pathlib
import os
sys.path.append(os.path.abspath(os.path.join('..')))
from config import PORT


methods = []
n = len(sys.argv)

try:
    for i in range(1, n):
        methods.append(sys.argv[i])
except:
    pass


class Colour:
    yellow = '\033[93m'
    white = '\033[0m'
    green = '\033[92m'
    blue = '\033[94m'


class Test:
    def __init__(self):
        self.port = PORT
        self.url = "http://localhost:{}/".format(self.port)
        self.lock = threading.Lock()

    def result(self, result):
        print()
        print('Method: ' + result.request.method, end= '')
        print('     Status code: ' + str(result.status_code), end='')
        print('     Message: ' + result.reason, end='')
        print('     Result: ' + str(result))

    def testGet(self):
        print( "\n" + Colour.blue + 'Testing GET method' + Colour.white)
        url = [
            'login.html', 'image.png', 'unknown'
        ]
        for i in url:
            r = requests.get(self.url + i)
            if(r.status_code == 404):
                self.result(r)
            else:
                self.result(r)
            print('Length of Body: ', len(r.text))
            print("\n")
        
        self.badContent()
        self.badAccept()
        self.range()


    def badContent(self):
        print(Colour.yellow + "Testing Bad Content Type :" + Colour.white)
        r = requests.get(self.url + 'index.html', headers={'Accept-Encoding': 'NonExistent'})
        self.result(r)
        print('Length of Body: ', len(r.text))


    def badAccept(self, acceptType ="notFound/html"):
        print(Colour.yellow + '\nTesting a wrong Accept Type :' + Colour.white)
        r = requests.get(self.url, headers={'Accept': acceptType})
        self.result(r)

    def testHead(self):
        print("\n" + Colour.blue + 'Testing HEAD method' + Colour.white)
        url = [
            'image.png', 'login.html', 'unknown'
        ]
        for i in url:
            r = requests.head(self.url + i)
            if r.status_code == 404 :
                self.result(r)
            else:
                self.result(r)
            print('Length of Body: ', len(r.text))

    def range(self):
        print(Colour.yellow + '\nTesting Range Headers\n' + Colour.white)
        r1 = requests.head(self.url)
        length = int(r1.headers['Content-Length'])
        print('Requesting 20 bytes')
        r2 = requests.get(self.url + 'login.html',
                          headers={'Accept-Ranges': '20'})
        print("Content Length received : " + str(len(r2.text)))
        self.result(r2)

    def testDelete(self):
        print("\n" + Colour.blue + 'Testing DELETE method' + Colour.white)
        r = requests.delete(self.url + 'remove.txt')
        self.result(r)


    def testPost(self):
        print(Colour.blue + 'Testing POST method' + Colour.white)
        print('\nTesting form data')
        payload = {"name": "Tony", "surname": "Stark", "age": 51}
        r = requests.post(self.url, data=payload)
        self.result(r)

        print('\nTesting file upload')
        payload = {"name": "Tony", "surname": "Stark", "age": 51}
        files = {
            'test': open(str(pathlib.Path().absolute()) + '/post.txt', 'rb')
        }
        r = requests.post(self.url + 'post.txt',  data=payload, files=files)
        self.result(r)

    def testPut(self):
        print("\n" + Colour.blue + 'Testing PUT method' + Colour.white)
        payload = {"name": "Steve", "surname": "Rogers", "age": 51}
        r = requests.put(self.url + 'put.txt', data=payload)
        self.result(r)

    def testAll(self):
        self.testGet()
        self.testHead()
        self.testPost()
        self.testPut()
        self.testDelete()
        

if __name__ == "__main__":
    Tester = Test()
 
    for i in methods:
        if (i == '-get'):
            Tester.testGet()
        if (i == '-head'):
            print('Testing Head Method')
            Tester.testHead()
        if (i == '-delete'):
            print('Testing Delete Method')
            Tester.testDelete()
        if (i == '-post'):
            print('Testing Post Method')
            Tester.testPost()
        if (i == '-put'):
            print('Testing Put Method')
            Tester.testPut()
        if (i == '-all'):
            Tester.testAll()
        if (i not in ['-get', '-head', '-delete', '-post', '-put', '-all']):
            print('Invalid option')