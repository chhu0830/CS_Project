#!/usr/bin/env python3
import socket
import sys
import os
import RPi.GPIO as GPIO
import time

if (len(sys.argv) != 6):
    print("usage: ./client.py <IP> <PORT> <MAC> <SPEED> <DISTANCE>")
    sys.exit()

red_pin = 17
green_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

TCP_IP = str(sys.argv[1])
TCP_PORT = int(sys.argv[2])
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

msg = str(sys.argv[3]) + ' ' + str(sys.argv[4]) + ' ' + str(sys.argv[5])
s.send(msg.encode('utf-8'))
print("send msg:", msg)
data = s.recv(BUFFER_SIZE)
print("receive data:", data.decode())

if (data.decode() == "FAST"):
    trigger(green_pin, True, 0.5)
    trigger(green_pin, False, 0)
elif (data.decode() == "SLOW"):
    trigger(red_pin, True, 0.5)
    trigger(red_pin, False, 0)
