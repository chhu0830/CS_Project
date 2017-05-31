#!/usr/bin/env python3
import os
import sys
import datetime
import time
from om2m import get_data, create_content_instance

data = {}
danger_distance = 20.0
danger_speed = 100.0
low_speed = 10.0

while True:
    string = input()
    start = string.find('<con>')
    end = string.find('</con>')

    if start != -1:
        datum = string[start+5:end]
        datum = datum.strip().split(' ')
    else:
        continue

    print(datum)
    mac, cur_speed, cur_distance = datum

    data[mac] = [cur_speed, cur_distance]

    max_speed = 0.0
    command = ''

    if float(cur_distance) < danger_distance:
        command = 'SLOW'
        print('SLOW')
    elif float(cur_speed) > danger_speed:
        command = 'SLOW'
        print('SLOW')
    elif float(cur_speed) < max_speed:
        command = 'FAST'
        print('FAST')
    elif float(cur_speed) < low_speed:
        command = 'FAST'
        print('FAST')
    else:
        command = 'KEEP'
        print('KEEP')
    print(create_content_instance('COMMAND', mac, command))

'''
    for i in data:
        if float(data[i][0]) > max_speed:
            max_speed = float(data[i][0])
'''

'''
    f = open('log/' + recv[0], 'a')
    f.write(str(datetime.datetime.now()) + '\t' + cur_speed + '\t' + cur_distance + '\t' + msg + '\n')
    f.close()
'''
