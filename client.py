#!/usr/bin/env python3
import RPi.GPIO as GPIO
import requests
import smbus
import math
import time
import sys
import os
from uuid import getnode as get_mac
from om2m import subscribe

if (len(sys.argv) != 3):
    print("usage: python3 client.py APP DATA")
    sys.exit()

# sonic
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
    # distance_in = distance_cm / 2.5
    return distance_cm_2


# speed
# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

def read_byte(adr):
    return bus.read_byte_data(address, adr)

def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val

def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val

def dist(a,b):
    return math.sqrt((a*a)+(b*b))

def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)

def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)


'''
def post(speed, distance): 
    import requests
    from datetime import datetime
    from uuid import getnode as get_mac

    url = 'http://' + sys.argv[1] + '/data'
    now = datetime.now()

    print("Speed:", speed, "Distance:", distance)
    payload = {
        'datum[mac]': get_mac(),
        'datum[speed]': speed,
        'datum[distance]': distance
    }
    r = requests.post(url, data=payload)
    return
'''

def get_speed(x, y, z):
    return (abs(x)**3 + abs(y)**3 + abs(z)**3)**(1/3.0)

Gyrox = 0
Gyroy = 0
Gyroz = 0
lasttimeX = 0
lasttimeY = 0
lasttimeZ = 0
Accx = 0.00
Accy = 0.00
Accz = 0.00
Ax = 0.00
Ay = 0.00
Az = 0.00
lastAx = 0.00
lastAy = 0.00
lastAz = 0.00
speedX = 0.00
speedY = 0.00
speedZ = 0.00
counter = 0

#new container
os.system('python3 om2m.py 3 ' + 'COMMAND' + ' ' + str(get_mac()))
#subscribe
subscribe('COMMAND', str(get_mac()))

while True:
    bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
    address = 0x68       # This is the address value read via the i2cdetect command

    # Now wake the 6050 up as it starts in sleep mode
    bus.write_byte_data(address, power_mgmt_1, 0)

    t = time.time()
    gyro_xout = read_word_2c(0x43)
    gyro_yout = read_word_2c(0x45)
    gyro_zout = read_word_2c(0x47)

    accel_xout = read_word_2c(0x3b)
    accel_yout = read_word_2c(0x3d)
    accel_zout = read_word_2c(0x3f)

    Accx = accel_xout / 16384.0 * 9.81
    Accy = accel_yout / 16384.0 * 9.81
    Accz = (accel_zout / 16384.0 - 1) * 9.81

    gx = gyro_xout / 131.00
    gy = gyro_yout / 131.00
    gz = gyro_zout / 131.00

    dt = time.time() - t

    Gyrox = Gyrox + (lasttimeX + gx) * dt / 2
    Gyroy = Gyroy + (lasttimeY + gy) * dt / 2
    Gyroz = Gyroz + (lasttimeZ + gz) * dt / 2

    Ax = (lastAx + Accx) * dt / 2 * 100
    Ay = (lastAy + Accy) * dt / 2 * 100
    Az = (lastAz + Accz) * dt / 2 * 100

    offset = 0.5
    if abs(Ax) < offset:
        Ax = 0
    if abs(Ay) < offset:
        Ay = 0
    if abs(Az) < offset:
        Az = 0

    speedX += Ax
    speedY += Ay
    speedZ += Az

    lasttimeX = gx;
    lasttimeY = gy;
    lasttimeZ = gz;

    lastAx = Accx;
    lastAy = Accy;
    lastAz = Accz;

    counter = counter + 1
    if (counter >= 25):
        result = '"' + str(get_speed(speedX, speedY, speedZ)) + ' ' + str(get_distance()) + '"'
        os.system("python3 om2m.py 4 " + sys.argv[1] + ' ' + sys.argv[2] + ' ' + result)
        counter = 0
        speedX = speedY = speedZ = 0

