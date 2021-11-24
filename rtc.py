# -*- coding: utf-8 -*-

# Import:
import time
import adafruit_pcf8523
import board

class RTC():

    def initRTC():
        i2c = board.I2C()
        global rtc
        rtc = adafruit_pcf8523.PCF8523(i2c)
        RTC.setRTC(time.localtime())
        return rtc

    def setRTC(localTime):
        if not rtc:
            return False

        rtc.datetime = localTime
        return

    def getRTC():
        if not rtc:
            return False

        return rtc.datetime
