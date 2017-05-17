#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import sys

red_pin = 17
green_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

def help():
    print('usage: python3 led.py <red/green> <time>')

def trigger(pin, value, t):
    GPIO.output(pin, value)
    time.sleep(t)

if __name__ == '__main__':
    if len(sys.argv == 3):
        if sys.argv[1] == 'green':
            trigger(green_pin, True, int(sys.argv[2]))
            trigger(green_pin, False, 0)
        elif sys.argv[1] == 'red':
            trigger(red_pin, True, int(sys.argv[2]))
            trigger(red_pin, False, 0)
        else:
            help()
    else:
        help()
