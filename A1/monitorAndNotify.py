#!/usr/bin/env python3
from virtual_sense_hat import VirtualSenseHat
import datetime
from logData import Logger
import sqlite3

class Info:
   
   def getInfo(self):
      sense = VirtualSenseHat.getSenseHat()
      timestamp = datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')
      temperature = sense.get_temperature()
      humidity = sense.get_humidity()
      return timestamp, temperature, humidity
   

info = Info()

def main():
      
   timestamp, temperature, humidity = info.getInfo()

   logData = Logger()
   logData.dataLogger(timestamp, temperature, humidity)

   logData.displayData()
   
if __name__ == "__main__":
        main()