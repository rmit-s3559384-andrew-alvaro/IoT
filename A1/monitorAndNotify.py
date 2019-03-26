from virtual_sense_hat import VirtualSenseHat
import datetime
from logData import Logger
import sqlite3

class Info:
   
   def getInfo(self):
      sense = VirtualSenseHat.getSenseHat()
      timestamp = datetime.datetime.now().strftime('%I:%M %p')
      temperature = sense.get_temperature()
      humidity = sense.get_humidity()
        
      return timestamp, temperature, humidity

info = Info()
timestamp, temperature, humidity = info.getInfo()

logData = Logger()
logData.dataLogger(timestamp, temperature, humidity)

logData.displayData