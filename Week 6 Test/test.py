from sense_hat import SenseHat
import datetime

class getPressure:
    
    def createData(self):
        connection = sqlite3.connect("sensehat.db")

        with connection:
            connection.execute("CREATE TABLE data(timestamp DATETIME, pressure NUMERIC")
        connection.close()
    
    def getInfo(self):

        sense = SenseHat.getSenseHat()
        timestamp = datetime.datetime.now().strftime('%d/%m/%Y %I:%M %p')
        pressure = sense.get_pressure()
        
        if pressure is not None:
        pressure = round(pressure, 2)

        return timestamp, pressure
    

    def dataLogger(self, timestamp, pressure):
        DB_NAME = "sensehat.db"
        connection = sqlite3.connect(DB_NAME)
        with connection:
             connection.execute(
             """INSERT INTO sensehat_data (timestamp, pressure)
             VALUES (:timestamp, :pressure)""", {"timestamp": timestamp, "pressure": temperature })

    
    
    def displayData(self):
        DB_NAME = "sensehat.db"
        connection = sqlite3.connect(DB_NAME)
        connection.row_factory = sqlite3.Row 
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM sensehat_data")
        
            print("Database content:")
            print("-----------------")
            print("Time              Pressure")
            for row in cursor:
                print(row["timestamp"], row["pressure"], sep="   ")

pressure = getPressure()

def main():
    pressure = getPressure()
    pressure.createData()
    timestamp, pressure = pressure.getInfo()
    pressure.dataLogger()
    pressure.displayData()

if __name__ == "__main__":
    main()