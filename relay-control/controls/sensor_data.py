#!/usr/bin/python
import urllib2

class SensorData:        # define nose data class
    def __init__(self):
        self.getData()

    def getData(self):
        retData = [] 
        req = urllib2.urlopen("http://thenose.someip-or-hostname/data.txt")
        data_string = req.read()
        fields = data_string.split("&")
        self.ppm = fields[7].split("=")[1]
        return self
