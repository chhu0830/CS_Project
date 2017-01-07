#!/usr/bin/env python3
import socket
import netifaces as ni
import os
import sys

if (len(sys.argv) != 3):
    print("usage:", sys.argv[0], "<net interface> <port>")
    sys.exit()

TCP_IP = ni.ifaddresses(sys.argv[1])[2][0]['addr']
TCP_PORT = int(sys.argv[2])
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("listen at", TCP_IP, TCP_PORT)

data = {}
danger_distance = 10
low_speed = 10

while True:
    conn, addr = s.accept()
    print('Connection address:', addr)

    recv = conn.recv(BUFFER_SIZE)
    recv = recv.decode()
    recv = recv.split(' ')
    data[recv[0]] = [recv[1], recv[2]]
    
    max_speed = 0.0
    for i in data:
        if float(data[i][0]) > max_speed:
            maxspeed = float(data[i][0])

    if float(recv[2]) < danger_distance:
        msg = "SLOW"
    elif float(recv[1]) < max_speed:
        msg = "FAST"
    elif float(recv[1]) < low_speed:
        msg = "FAST"
    else:
        msg = "KEEP"

    conn.send(msg.encode('utf-8'))
    conn.close()
