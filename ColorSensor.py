"""
File Name: ColorSensor.py
Author: Akli Amrous
Description: This program uses the Adafruit TCS34725 color sensor to
gather color and illuminance data. This program created for the 2018
FIRST Robotics Competition. 
"""

from networktables import NetworkTables as nt
import time
import smbus
import Adafruit_TCS34725 as af
import os


class Sensor(object):
    def __init__(self, ip):
        
        self.ip = ip
        self.scale = nt.getTable('Scale')
        self.switch = nt.getTable('Switch')
        self.sensor = af.TCS34725()
        self.sensor.set_interrupt(False)

    def scan(self):
        
        while(True):
    
            r, g, b, c = self.sensor.get_raw_data()
            time.sleep(0.5)
            print("rgb=("+str(r)+", "+str(g)+", "+str(b)+")")
    
            colorTemp = af.calculate_color_temperature(r, g,b)
            lux = af.calculate_lux(r,g,b)
            print(str(colorTemp) + "k")
            print(str(lux) + " lux")

            if(lux <= 9):
                self.scale.putNumber('View', 0)
                print("Lumosity is %s, Robot is not in the Scale Area" % (str(lux)))

            elif(lux <= 10):
                self.scale.putNumber('View', 1)
                print("Lumosity is %s, Robot is in the Scale Area" % ((str(lux)))

        self.sensor.set_interrupt(True)
        self.sensor.disable()

        










