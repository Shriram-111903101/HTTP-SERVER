

##  Info : 

This project is a simple demonstration of the HTTP/1.1 protocol.
Consists of basic HTTP methods viz., GET, HEAD, POST, PUT, DELETE

###  Execution Steps :

Follow the below steps to start the server

```
./startServer.sh
```

This will start the server on a default port of as mentioned in the config.py file.

```
1. PORT = Specify the port on which the server will keep listenting
2. ROOT_PATH = Specify the document root directory that will serve the requests
3. MAX_CONNECTIONS = Specify the maximum number of simultaneous connections that the server will accept
5. ACCESSLOG = Specify the file to save access logs
6. ERRORLOG = Specify the file to save error logs
7. POSTLOG = Specify the file to save post logs
```

The server will start in background.
To stop the server do :

```
./stopServer.sh
```

To restart the server do:

```
./restart.sh
```

## Testing

To test the five methods automatically do:

```
[cd testing/]
python3 test.py [options]
```

```
The options specifications for testing:
1. -get To test the GET method with some apecific cases.
2. -post To test the POST method with a form data
3. -put To test the PUT method with dummy form data/byte data
4. -head To test the HEAD method
5. -delete To test the DELETE method
6. -all To test all the above methods.
```


## Logging :

There are three types of logs maintained by the server:

1. Error Logs
2. Access Logs
3. POST Request Logs


## Contributors :

- [Harshal Chavan](https://gitlab.com/Harshal-Chavan)
- [Shriram Fajage](https://gitlab.com/ShriramFajage)

## Instructor:

- Abhijit.A.M sir

## Resources:

- [RFC2616](https://tools.ietf.org/html/rfc2616)
- [MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP)