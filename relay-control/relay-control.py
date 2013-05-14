#!/usr/bin/python
from controls.time_of_day import DayNightStatus
from controls.sensor_data import SensorData
import sys, serial
from time import sleep
import syslog

class SerialRelayController:
    def __init__(self):
        self.COM_PORT = 1
        self.BAUD = 9600
        self.ser = serial.Serial( self.COM_PORT, self.BAUD, timeout=0.5, rtscts=0 )
        self.ser.setDTR(0)
        self.dtrStatus = 0
        
    def start(self):
        while(1):
            self.daytime_status = DayNightStatus()
            self.sensor_data  = SensorData()
            if int(self.daytime_status.status) == int(1):
                if int(self.sensor_data.ppm) > int(1500):
                    message = "Turning off device"
                    self.toggleDevice(0, message)
                elif int(self.sensor_data.ppm) < int(680):
                    message = "Turning on device"
                    self.toggleDevice(1, message)
                else:
                    message = "Turning on device"
                    self.toggleDevice(1, message)
            else:
                if int(self.sensor_data.ppm) < int(600):
                    message = "Turning on device"
                    self.toggleDevice(1, message)
                elif int(self.sensor_data.ppm) > int(700):
                    message = "Turning off device"
                    self.toggleDevice(0, message)
                else:
                    message = "Turning on device"
                    self.toggleDevice(1, message)
            sleep(10)
            
    def toggleDevice(self, status, message):
        if status == self.dtrStatus:
            pass
        else:
            self.dtrStatus = status
            syslog.syslog(message)
            self.ser.setDTR(status)
            return True

def main():
    sr = SerialRelayController()
    sr.start()
    
if __name__ == "__main__":
    main()
