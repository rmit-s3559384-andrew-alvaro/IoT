import sqlite3

class Logger:
    DB_NAME = "sensehat.db"

    def dataLogger(self, timestamp, temperature, humidity):
        connection = sqlite3.connect("sensehat.db")
        with connection:
             connection.execute(
             """INSERT INTO sensehat_data (timestamp, temperature, humidity)
             VALUES (:timestamp, :temperature, :humidity)""", {"timestamp": timestamp, "temperature": temperature, "humidity": humidity })

    
    
    def displayData():
        connection = sqlite3.connect("sensehat.db")
        connection.row_factory = sqlite3.Row 
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM sensehat_data")
        
            print("Database content:")
            print("-----------------")
            print("Time  Temperature  Humidity")
            for row in cursor:
                print(row["timestamp"], row["temperature"], row["humidity"], sep="  ")
    displayData()