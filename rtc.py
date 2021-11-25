# -*- coding: utf-8 -*-

# Import:
import os
from datetime import datetime

class RTC():
    def getRTC():
        stream = os.popen("sudo hwclock -r")
        output = stream.readlines()[0]
        dt = datetime.strptime(output, "%Y-%m-%d %H:%M:%S.%f%z\n")
        # %Y --> dt.year
        # %m --> dt.month
        # %d --> dt.day
        # %H --> dt.hour
        # %M --> dt.minute
        # %S --> dt.second
        # %f --> dt.microsecond
        # %z --> dt.tzinfo
        return dt

    def setRTCfromSystemTime():
        stream = os.popen("sudo hwclock -w")
        return stream.readlines()


