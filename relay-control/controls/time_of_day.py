#!/usr/bin/python
import datetime

class DayNightStatus:        # define parent class

    def __init__(self):
       self.checkStatus()

    def checkStatus(self):
        ts = datetime.datetime.now()
        # Convert the timestamps into Date Objects
        if ts.hour in range(6, 18):
            self.status = 0
        else:
            self.status = 1

        return self
