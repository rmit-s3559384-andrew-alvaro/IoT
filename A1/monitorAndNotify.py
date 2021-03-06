#!/usr/bin/env python3
from sense_hat import SenseHat
import datetime
import time
from logData import Logger
from checkRange import InRange
from makeRemindercsv import Reminder
import sqlite3

class Info:

   SAMPLE_FREQUENCY_SECONDS = 3

   def getInfo(self):
      
      sense = SenseHat.getSenseHat()
      timestamp = datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')
      temperature = sense.get_temperature()
      humidity = sense.get_humidity()
      
      if temperature is not None:
        temperature = round(temperature, 2)
        
      if humidity is not None:
        humidity = round(humidity, 2)
      
      return timestamp, temperature, humidity
   



def main():
   info = Info()
   logData = Logger()
   check = InRange()
   reminder = Reminder()
   timestamp, temperature, humidity = info.getInfo()

   

   for _ in range(0, 3):
      logData.dataLogger(timestamp, temperature, humidity)
      time.sleep(info.SAMPLE_FREQUENCY_SECONDS)

   logData.displayData()

   reminder.makeReminder()
   check.checkConfig(temperature, humidity)

if __name__ == "__main__":
        main()