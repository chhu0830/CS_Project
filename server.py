#!/usr/bin/env python3
import os
import sys
import datetime
import time
from utils.om2m import get_data, create_content_instance

data = {}
danger_distance = 100.0
danger_speed = 100.0
low_speed = 60.0

while True:
    string = input()
    start = string.find("<con>")
    end = string.find("</con>")

    if start != -1:
        datum = string[start+5:end]
        datum = datum.strip().split(" ")
    else:
        continue

    mac, cur_speed, cur_distance = datum
    data[mac] = [cur_speed, cur_distance]
    min_speed = min(float(d[0]) for mac, d in data.items())

    command = "KEEP"
    if float(cur_distance) < danger_distance:
        command = "SLOW"
    elif float(cur_speed) > danger_speed:
        command = "SLOW"
    elif float(cur_speed) <= min_speed:
        command = "FAST"
    elif float(cur_speed) < low_speed:
        command = "FAST"

    print(datum, min_speed, command, create_content_instance("COMMAND", mac, command))
