import sqlite3

class CreateDB:
    
    def createData():
        connection = sqlite3.connect("sensehat.db")

        with connection:
             connection.execute("DROP TABLE IF EXISTS sensehat_data")
             connection.execute("CREATE TABLE sensehat_data(timestamp STRING, temperature NUMERIC, humidity NUMERIC)")
        connection.close()

    createData()