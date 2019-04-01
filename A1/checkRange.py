import json 
from pushBullet import pushNotification

class InRange:

    
    def checkConfig(self, temperature, humidity):
        sendPushBullet = pushNotification()
        with open("config.json", "r") as file:
            config = json.load(file)

        minTemp = config["min_temperature"]
        maxTemp = config["max_temperature"]
        minHumid = config["min_humidity"]
        maxHumid = config["max_humidity"]

        if(temperature < minTemp or temperature > maxTemp or humidity < minHumid or humidity > maxHumid):
            sendPushBullet.send()
        else:
            print("Temperature and Humidity in range")
