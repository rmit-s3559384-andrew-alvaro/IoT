from virtual_sense_hat import VirtualSenseHat
import sqlite3
import time

DB_NAME = "sensehat.db"
SAMPLE_FREQUENCY_SECONDS = 1

# Get data from SenseHat sensor.
def getSenseHatData():
    sense = VirtualSenseHat.getSenseHat()
    temperature = sense.get_temperature()

    if temperature is not None:
        temperature = round(temperature, 2)
        logData(temperature)

# Log sensor data on database.
def logData(temperature):
    connection = sqlite3.connect(DB_NAME)
    with connection:
        connection.execute(
            """INSERT INTO sensehat_data (timestamp, temperature)
            VALUES (DATETIME('now', 'localtime'), :temperature)""", { "temperature": temperature })
        # OR
        # cursor.execute("INSERT INTO sensehat_data (timestamp, temperature) VALUES (DATETIME('now', 'localtime'), ?)",
        #     (temperature,))
        # 
        # Note:
        # DATETIME('now') -> utc time
        # DATETIME('now', 'localtime') -> local timezone time
        # 
        # If using localtime be sure to set the timezone on your Pi correctly:
        # https://howchoo.com/g/njnlzjmyyjg/how-to-set-the-timezone-on-your-raspberry-pi
    connection.close()

# Display database data.
def displayData():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row # Use this if you want to use column names over indexes.
    with connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sensehat_data")
        
        print("Database content:")
        for row in cursor:
            print(row["timestamp"], row["temperature"])
            # OR
            # print(row[0], row[1])
    connection.close()

# Main function.
def main():
    for _ in range(0, 3):
        getSenseHatData()
        time.sleep(SAMPLE_FREQUENCY_SECONDS)
    displayData()

# Execute program.
if __name__ == "__main__":
    main()
