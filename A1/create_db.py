import sqlite3 as lite
import sys

con = lite.connect("report.db")

with con:
    cur = con.cursor()
    cur.execute()