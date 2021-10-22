#!usr/bin/python

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 4466

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("received connection from: %s " % str(address))

    message = 'Hello! Thank yoy for connecting to the server' + "\r\n"

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()