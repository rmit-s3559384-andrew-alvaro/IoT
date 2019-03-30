#!/usr/bin/env python3
from virtual_sense_hat import VirtualSenseHat
import datetime
import time
from logData import Logger
import sqlite3

class Info:

   SAMPLE_FREQUENCY_SECONDS = 3

   def getInfo(self):
      
      sense = VirtualSenseHat.getSenseHat()
      timestamp = datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')
      temperature = sense.get_temperature()
      humidity = sense.get_humidity()
      
      if temperature is not None:
        temperature = round(temperature, 2)
        
      return timestamp, temperature, humidity
   

info = Info()

def main():
      
   timestamp, temperature, humidity = info.getInfo()

   logData = Logger()
   
   for _ in range(0, 3):
      logData.dataLogger(timestamp, temperature, humidity)
      time.sleep(info.SAMPLE_FREQUENCY_SECONDS)

   logData.displayData()
   
if __name__ == "__main__":
        main()