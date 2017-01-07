#!/usr/bin/env python3
import socket
import sys

if (len(sys.argv) != 3):
    print("usage: ./client.py <IP> <MSG>")
    sys.exit()
TCP_IP = str(sys.argv[1])
TCP_PORT = 4000
BUFFER_SIZE = 1024
MESSAGE = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close

print("receive data:", data.decode())
