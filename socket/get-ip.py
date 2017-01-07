#!/usr/bin/env python3
import netifaces as ni
print(ni.ifaddresses('enp0s3')[2][0]['addr'])
