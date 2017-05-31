#!/usr/bin/python3
import sys
import os

if sys.argv[1] == 'FAST':
    os.system('python3 led.py green 0.2')
elif sys.argv[1] == 'SLOW':
    os.system('python3 led.py red 0.2')
