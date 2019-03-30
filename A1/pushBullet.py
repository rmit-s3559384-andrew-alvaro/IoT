#!/usr/bin/env python3
import requests
import json
import os

class pushNotification:


    def send_notification_via_pushbullet(title, body):
        ACCESS_TOKEN = "o.T3YzoJfL2PpiSk54KMTsTm9Y0VtSjjdS"

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

        print("Notification sent.")

    # Main function.
push = pushNotification

def main():
    ip_address = os.popen("hostname -I").read()
    push.send_notification_via_pushbullet(ip_address, "From Raspberry Pi")

    # Execute.
if __name__ == "__main__":
    main()