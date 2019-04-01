#!/usr/bin/env python3
import csv

class Report:
    
    def report(self):
        with open("sensehat.db", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            
            
        connection = sqlite3.connect("sensehat.db")
        connection.row_factory = sqlite3.Row
    
    with connection:
        cursor = connection.cursor()

        row = cursor.execute("SELECT MIN(temperature), MAX(temperature) FROM sensehat_data").fetchone()
        row2 = cursor.execute("SELECT MIN(humidity), MAX(humidity) FROM sensehat_data").fetchone()
        
        startTemperature = row[0]
        endTemperature = row[1]
        startHumidity = row2[0]
        endHumidity = row2[1]

        while startTemperature <= endTemperature:
            if
            row = cursor.execute(
                """SELECT COUNT(*) FROM sensehat_data
                WHERE timestamp >= :date AND timestamp < :date """,
                { "date": date.strftime(DATE_FORMAT) }).fetchone()
            
            print(date.strftime(DATE_FORMAT) + " | Row Count: " + str(row[0]))
            
            date += ONE_DAY_DELTA
    connection.close()