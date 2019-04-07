import csv
import os
class Reminder:

    def makeReminder(self): 
        exists = os.path.isfile('bluetoothReminder.csv')
        
        if exists:
            pass

        else:
            with open('bluetoothReminder.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["          ", "Notification last sent. Do not tamper or delete this file"])