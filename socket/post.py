#!/usr/bin/env python
import requests
from datetime import datetime
from uuid import getnode as get_mac

url = 'http://192.168.1.13:3000/data'
now = datetime.now()

payload = {
'datum[mac]': get_mac(),
'datum[speed]': now.minute,
'datum[distance]': now.seconde
}

r = requests.post(url, data=payload)

