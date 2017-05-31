#!/usr/bin/python3
import sys
import os

while True:
    string = input()
    print(string)
    start = string.find('<con>') + 5
    end = string.find('</con>')
    command = string[start:end]
    command = command.strip()
    if command == 'FAST':
        os.system('python3 led.py green 0.2')
    elif command == 'SLOW':
        os.system('python3 led.py red 0.2')
