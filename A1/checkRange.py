#!/usr/bin/env python3
import json 
import csv
import datetime
from pushBullet import pushNotification

class InRange:

    def checkConfig(self, temperature, humidity):
        sendPushBullet = pushNotification()
        timestamp = datetime.datetime.now().strftime('%d/%m/%Y')

        with open("config.json", "r") as file:
            config = json.load(file)

        minTemp = config["min_temperature"]
        maxTemp = config["max_temperature"]
        minHumid = config["min_humidity"]
        maxHumid = config["max_humidity"]
        
        if(temperature < minTemp or temperature > maxTemp or humidity < minHumid or humidity > maxHumid):
            
            with open('reminder.csv', 'r') as csvfile:
                readCSV = csv.reader(csvfile)
                
                for row in readCSV:
                    if row[0] != timestamp:
                        sendPushBullet.send()
                    else:
                        print("Notification has already been sent today.")
        else:
            print("Temperature and Humidity in range")
