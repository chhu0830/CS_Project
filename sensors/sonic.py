#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

trigger_pin_2 = 23
echo_pin_2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin_2, GPIO.OUT)
GPIO.setup(echo_pin_2, GPIO.IN)
def post(distance): 
    import requests
    from datetime import datetime
    from uuid import getnode as get_mac

    url = 'http://192.168.1.13:3000/data'
    now = datetime.now()

    payload = {
        'datum[mac]': get_mac(),
        'datum[speed]': now.second,
        'datum[distance]': distance
    }

    r = requests.post(url, data=payload)
    return

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
	# distance_in = distance_cm / 2.5
	return distance_cm_2

while True:
        post(get_distance())
	print("cm=%f" % get_distance())
	time.sleep(1)
