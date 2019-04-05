#!/usr/bin/env python3
import csv
import json
import sqlite3
from datetime import datetime, timedelta

class Report:
    
    def report(self):
        DB_NAME = "sensehat.db"
        DATE_FORMAT = "%d/%m/%Y %I:%M %p"
        ONE_DAY_DELTA = timedelta(days = 1)
        
        with open("config.json", "r") as file:
            config = json.load(file)

       
            
        connection = sqlite3.connect("sensehat.db")
        connection.row_factory = sqlite3.Row
    
        with connection:
            cursor = connection.cursor()

            row = cursor.execute("SELECT MIN(timestamp), MAX(timestamp) FROM sensehat_data").fetchone()
            startDate = datetime.strptime(row[0], DATE_FORMAT)
            endDate = datetime.strptime(row[1], DATE_FORMAT)

            print("Dates:")
            date = startDate
            minTempConfig = config["min_temperature"]
            maxTempConfig = config["max_temperature"]
            minHumidConfig = config["min_humidity"]
            maxHumidConfig = config["max_humidity"]   
            
            while date <= endDate:
                row = cursor.execute(
                    """SELECT MIN(temperature), MAX(temperature), MIN(humidity), MAX(humidity) FROM sensehat_data
                    WHERE """,
                    { "minTemp": minTemp, "maxTemp": maxTemp, "minHumid": minHumid, "maxHumid": maxHumid }).fetchone()

                minTemp = row[0]
                maxTemp = row[1]

                if(mintemp is None)

            print(date.strftime(DATE_FORMAT) + " | Row Count: " + str(row[0]))
            
            date += ONE_DAY_DELTA
        connection.close()

run = Report()

def main():
    run.report()

if __name__ == "__main__":
    main()