#!/usr/bin/env python3
import socket
import netifaces as ni
import os
import sys

if (len(sys.argv) != 2):
    print("usage:", sys.agrv[0], "<net interface>")
    sys.exit()

TCP_IP = ni.ifaddresses(sys.argv[1])[2][0]['addr']
TCP_PORT = 4000
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("listen at", TCP_IP, TCP_PORT)

while 1:
    conn, addr = s.accept()
    print('Connection address:', addr)
    pid = os.fork()
    if (pid == 0):
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            print("received data:", data.decode())
            conn.send(data)
        conn.close()
        os._exit(0)
