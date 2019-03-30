#!/usr/bin/env python3
import csv

class Report:
    
    def report(self):
        with open("sensehat.db", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)