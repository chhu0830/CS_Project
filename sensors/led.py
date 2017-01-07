#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

red_pin = 17
green_pin = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)



def trigger(pin, value, t):
    GPIO.output(pin, value)
    time.sleep(t)

while True:
    trigger(red_pin, True, 0)
    trigger(green_pin, True, 1)
    trigger(red_pin, False, 0)
    trigger(green_pin, False, 1)
