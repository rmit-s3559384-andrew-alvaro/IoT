#!/usr/bin/env python3

import sqlite3 as lite
import sys

class CreateDB:

	def createData():
		connection = sqlite3.connect("sensehat.db")

		with connection:
			connection.execute("DROP TABLE IF EXISTS sensehat_data")
			connection.execute("CREATE TABLE sensehat_data(timestamp DATETIME, temperature NUMERIC. humidity NUMERIC)")
		connection.close()

    createData()