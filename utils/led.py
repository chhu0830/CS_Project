#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import sys

red_pin = 17
green_pin = 22
white_pin = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)
GPIO.setup(white_pin, GPIO.OUT)

def help():
    print('usage: python3 led.py <red/green/white> <time>')

def trigger(pin, value, t):
    GPIO.output(pin, value)
    time.sleep(t)

def light(color, time):
    if color == 'green':
        pin = green_pin
    elif color == 'red':
        pin = red_pin
    elif color == 'white':
        pin = white_pin
    else:
        return
    trigger(pin, True, time)
    trigger(pin, False, 0)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        light(sys.argv[1], float(sys.argv[2]))
    else:
        help()
