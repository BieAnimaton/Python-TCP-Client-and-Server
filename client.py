#!usr/bin/python

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 4466

clientsocket.connect(('192.168.1.26', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))