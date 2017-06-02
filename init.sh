#!/bin/sh

python3 utils/om2m.py app APP
python3 utils/om2m.py con APP DATA
python3 utils/om2m.py app COMMAND
python3 utils/om2m.py sub APP DATA
