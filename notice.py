#!/usr/bin/python3
import sys
import os

while True:
    string = input()
    start = string.find('<con>')
    end = string.find('</con>')

    if start != -1:
        command = string[start+5:end]
        command = command.strip()
        print(command)
    else:
        continue

    if command == 'FAST':
        os.system('python3 led.py green 0.1')
    elif command == 'SLOW':
        os.system('python3 led.py red 0.1')
