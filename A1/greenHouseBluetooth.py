import bluetooth 
import sys, os
import subprocess as sp
import datetime
from pushBulletForBluetooth import pushNotification
from makeReminderforBluetooth import Reminder
import csv

class blueDev:
    
    def findmyDevice(self): 

        sendPushBullet = pushNotification()
        timestamp = datetime.datetime.now().strftime('%d/%m/%Y')
        nearby_devices = bluetooth.discover_devices(lookup_names = True)

        if nearby_devices is not None:
            
            for addr, name in nearby_devices:
                
                devices = addr.split("(")[-1]
            
        else:
            print("No device available")

        paired = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)

        (stdout, stdin) = (paired.stdout, paired.stdin)
        list_of_paired_devices = stdout.readlines()

        list_of_paired_devices.pop(0)

        for paired_device in list_of_paired_devices:
            
            pairedString = paired_device.decode()
            pairedSplit = pairedString.split("(")[-1]
            pairedDevice = pairedSplit[0:-2]
        print(devices, pairedDevice)
        if pairedDevice == devices:
            
            with open('bluetoothReminder.csv', 'r') as csvfile:
                readCSV = csv.reader(csvfile)
                
                for row in readCSV:
                    if row[0] != timestamp:
                        sendPushBullet.send()
                    else:
                        print("Notification has already been sent today.")
        else:
            print("No match device(s) found!")



def main():
    bluetooth = blueDev()
    reminder = Reminder()

    reminder.makeReminder()
    bluetooth.findmyDevice()

if __name__ == "__main__":
    main()

