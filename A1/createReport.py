#!/usr/bin/env python3
import csv
import json
import sqlite3
from datetime import datetime, timedelta

class Report:
    
    def report(self):
        DATE_FORMAT = "%d/%m/%Y %I:%M %p"
        
        with open("config.json", "r") as file:
            config = json.load(file)

        minTempConfig = config["min_temperature"]
        maxTempConfig = config["max_temperature"]
        minHumidConfig = config["min_humidity"]
        maxHumidConfig = config["max_humidity"]   
       
            
        connection = sqlite3.connect("sensehat.db")
        connection.row_factory = sqlite3.Row
    
        with connection:
            cursor = connection.cursor()

            row = cursor.execute("SELECT MIN(timestamp), MAX(timestamp) FROM sensehat_data").fetchone()
            endDate = row[0]
            startDate = row[1]
            

            date = startDate
            print(startDate)
            print(endDate)
            
            
            while endDate <= date:
                row = cursor.execute(
                    """SELECT min(temperature), max(temperature), min(humidity), max(humidity) FROM sensehat_data
                    WHERE timestamp >= :date AND timestamp < :date""",
                    { "date": DATE_FORMAT }).fetchone()

                minTemp = row[0]
                maxTemp = row[1]
                minHumid = row[2]
                maxHumid = row[3]

            if minTemp is None:
                pass
            if maxTemp is None:
                pass
            if minHumid is None:
                pass
            if maxHumid is None:
                pass
                
            else:   
                while minTemp <= maxTemp:
                    while minHumid <= maxHumid:
                        if(minTemp < minTempConfig):
                            status = "BAD, Below configured temperature"
                        if(maxTemp > maxTempConfig):
                            status = "BAD, Above configured temperature"
                        if(minHumid < minHumidConfig):
                            status = "BAD, Below configured humidity"
                        if(maxHumid > maxHumidConfig):
                            status = "BAD, Above configured humidity"
                        else:
                            status = "OK"
            
                        print(status)
                        with open('report.csv', 'w') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(["Date", "Status"])
                            writer.writerow([date.strftime(DATE_FORMAT), status])

        connection.close()

run = Report()

def main():
    run.report()

if __name__ == "__main__":
    main()