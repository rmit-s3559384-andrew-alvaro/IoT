#!/usr/bin/env python3
# More info: https://pypi.org/project/python-crontab/
from virtual_sense_hat import VirtualSenseHat
from datetime import datetime

time = datetime.now().strftime("%H:%M")
sense = VirtualSenseHat.getSenseHat()
sense.show_message("Time is {}".format(time), scroll_speed = 0.05)
