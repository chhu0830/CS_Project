#!/usr/bin/env python3
import socket
import netifaces as ni
import os
import sys

if (len(sys.argv) != 2):
    print("usage:", sys.argv[0], "<net interface>")
    sys.exit()

import RPi.GPIO as GPIO
import time

red_pin = 17
green_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

TCP_IP = ni.ifaddresses(sys.argv[1])[2][0]['addr']
TCP_PORT = 4000
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print("listen at", TCP_IP, TCP_PORT)

def trigger(pin, value, t):
    GPIO.output(pin, value)
    time.sleep(t)

while 1:
    conn, addr = s.accept()
    print('Connection address:', addr)
    pid = os.fork()
    if (pid == 0):
        while 1:
            data = conn.recv(BUFFER_SIZE)
            if not data: break
            print("received data:", data.decode())
            if (data.decode() == "FAST"):
                trigger(green_pin, True, 0.2)
                trigger(green_pin, False, 0)
            elif (data.decode() == "SLOW"):
                trigger(red_pin, True, 0.2)
                trigger(red_pin, False, 0)
            conn.send(data)
        conn.close()
        os._exit(0)
