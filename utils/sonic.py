#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time
import sys

trigger_pin_2 = 23
echo_pin_2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin_2, GPIO.OUT)
GPIO.setup(echo_pin_2, GPIO.IN)

def send_trigger_pulse(pin):
    GPIO.output(pin, True)
    time.sleep(0.001)
    GPIO.output(pin, False)

def wait_for_echo(value, timeout, pin):
    count = timeout
    while GPIO.input(pin) != value and count > 0:
        count = count - 1

def get_distance():
    send_trigger_pulse(trigger_pin_2)
    wait_for_echo(True, 8000, echo_pin_2)
    start = time.time()
    wait_for_echo(False, 8000, echo_pin_2)
    finish = time.time()
    pulse_len_2 = finish - start

    distance_cm_2 = pulse_len_2 * 340 * 100 / 2
    return distance_cm_2

if __name__ == '__main__':
    while True:
        print("cm=%f" % get_distance())
        time.sleep(1)
