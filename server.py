#!/usr/bin/env python3
import os
import sys
import datetime
import time
from om2m import get_data

data = {}
danger_distance = 20.0
danger_speed = 100.0
low_speed = 10.0

while True:
    datum = get_data('APP', 'DATA')
    s = datum.split(' ')
    cur_speed, cur_distance = s[18], s[19]
    print(cur_speed, cur_distance)

    data['TTT'] = [cur_speed, cur_distance]

    max_speed = 0.0

    if float(cur_distance) < danger_distance:
        os.system('./om2m.py 4 COMMAND TTT SLOW')
        print('SLOW')
    elif float(cur_speed) > danger_speed:
        os.system('./om2m.py 4 COMMAND TTT SLOW')
        print('SLOW')
    elif float(cur_speed) < max_speed:
        os.system('./om2m.py 4 COMMAND TTT FAST')
        print('FAST')
    elif float(cur_speed) < low_speed:
        os.system('./om2m.py 4 COMMAND TTT FAST')
        print('FAST')
    else:
        os.system('./om2m.py 4 COMMAND TTT KEEP')
        print('KEEP')
    time.sleep(1)

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
