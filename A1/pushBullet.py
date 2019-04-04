#!/usr/bin/env python3
import requests
import json
import os
import datetime
import csv

class pushNotification:


    def send_notification_via_pushbullet(self, title, body):
        ACCESS_TOKEN = "o.T3YzoJfL2PpiSk54KMTsTm9Y0VtSjjdS"
        timestamp = datetime.datetime.now().strftime('%d/%m/%Y')

        """ Sending notification via pushbullet.
            Args:
                title (str) : Title of text.
                body (str) : Body of text.
        """
        
        data = { "type": "note", "title": title, "body": body }

        response = requests.post("https://api.pushbullet.com/v2/pushes", data = json.dumps(data),
            headers = { "Authorization": "Bearer " + ACCESS_TOKEN, "Content-Type": "application/json" })

        if(response.status_code != 200):
            raise Exception()
        
        if(response.status_code == 200):
            with open('reminder.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([timestamp])

        print("Notification sent.")


    def send(self):
        push = pushNotification()


        ip_address = os.popen("hostname -I").read()
        push.send_notification_via_pushbullet(ip_address, "From Raspberry Pi")
    