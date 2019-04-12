import sqlite3

connection = sqlite3.connect("sensehat.db")

with connection:
    connection.execute("DROP TABLE IF EXISTS sensehat_data")
    connection.execute("CREATE TABLE sensehat_data(timestamp DATETIME, temperature NUMERIC)")

connection.close()
