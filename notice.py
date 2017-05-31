#!/usr/bin/python3
import sys
import os
from led import light

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
        light('green', 0.1)

    elif command == 'SLOW':
        light('red', 0.1)
