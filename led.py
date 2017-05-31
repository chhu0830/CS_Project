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

def light(pin, time):
    trigger(pin, True, time)
    trigger(pin, False, 0)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == 'green':
            light(green_pin, float(sys.argv[2]))
        elif sys.argv[1] == 'red':
            light(red_pin, float(sys.argv[2]))
        elif sys.argv[1] == 'white':
            light(white_pin, float(sys.argv[2]))
        else:
            help()
    else:
        help()
