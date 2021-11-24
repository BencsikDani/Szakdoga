# -*- coding: utf-8 -*-
# Import:
from globals import Globals
import time
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import led
from haapi import HAAPI
from ioe import IOE

def initButtons():
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(17, GPIO.RISING, callback=b1_callback)
    GPIO.add_event_detect(18, GPIO.RISING, callback=b2_callback)
    GPIO.add_event_detect(19, GPIO.RISING, callback=b3_callback)
    GPIO.add_event_detect(20, GPIO.RISING, callback=b4_callback)
    GPIO.add_event_detect(21, GPIO.RISING, callback=b5_callback)
    return

def b1_callback(self):
    if Globals.currentScreenState == Globals.screenState.MENU:
        if (4 <= Globals.menuPos) and (Globals.menuPos <= 6):
            Globals.menuPos -= 3
    if Globals.currentScreenState == Globals.screenState.LEDMENU:
        if (Globals.LEDMenuPos == 3) or (Globals.LEDMenuPos == 4):
            Globals.LEDMenuPos -= 2

    time.sleep(Globals.debounceTime)
    return


def b2_callback(self):
    if Globals.currentScreenState == Globals.screenState.MENU:
        if (Globals.menuPos == 2) or (Globals.menuPos == 3) or (Globals.menuPos == 5) or (Globals.menuPos == 6):
            Globals.menuPos -= 1
    if Globals.currentScreenState == Globals.screenState.LEDMENU:
        if (Globals.LEDMenuPos == 2) or (Globals.LEDMenuPos == 4) or ((6 <= Globals.LEDMenuPos) and (Globals.LEDMenuPos <= 8)):
            Globals.LEDMenuPos -= 1
        elif Globals.LEDMenuPos == 5:
            Globals.LEDMenuPos = 2
    if Globals.currentScreenState == Globals.screenState.OUTPUTMENU:
        if (2 <= Globals.outputMenuPos) and (Globals.outputMenuPos <= 6):
            Globals.outputMenuPos -= 1

    time.sleep(Globals.debounceTime*1.5)
    return


def b3_callback(self):
    if Globals.currentScreenState == Globals.screenState.BLACK:
        Globals.currentScreenState = Globals.screenState.CLOCK
    elif Globals.currentScreenState == Globals.screenState.CLOCK:
        Globals.menuPos = 1
        Globals.currentScreenState = Globals.screenState.MENU
    elif Globals.currentScreenState == Globals.screenState.MENU:
        if Globals.menuPos == 1:
            Globals.currentScreenState = Globals.screenState.TEMPMENU
        elif Globals.menuPos == 2:
            Globals.currentScreenState = Globals.screenState.LIGHTMENU
        elif Globals.menuPos == 3:
            Globals.LEDMenuPos = 1
            Globals.currentScreenState = Globals.screenState.LEDMENU
        elif Globals.menuPos == 4:
            Globals.currentScreenState = Globals.screenState.INPUTMENU
        elif Globals.menuPos == 5:
            Globals.outputMenuPos = 1
            Globals.currentScreenState = Globals.screenState.OUTPUTMENU
        elif Globals.menuPos == 6:
            Globals.currentScreenState = Globals.screenState.BLACK
    elif Globals.currentScreenState == Globals.screenState.TEMPMENU:
        Globals.currentScreenState = Globals.screenState.MENU
    elif Globals.currentScreenState == Globals.screenState.LIGHTMENU:
        Globals.currentScreenState = Globals.screenState.MENU
    elif Globals.currentScreenState == Globals.screenState.LEDMENU:
        if (1 <= Globals.LEDMenuPos) and (Globals.LEDMenuPos <= 4):
            led.toggleLED(Globals.LEDMenuPos)
        elif (Globals.LEDMenuPos == 5) or (Globals.LEDMenuPos == 6):
            HAAPI.toggleLED(Globals.LEDMenuPos - 4)
        elif Globals.LEDMenuPos == 7:
            HAAPI.toggleSonoff()
        elif Globals.LEDMenuPos == 8:
            Globals.currentScreenState = Globals.screenState.MENU
    elif Globals.currentScreenState == Globals.screenState.INPUTMENU:
        Globals.currentScreenState = Globals.screenState.MENU
    elif Globals.currentScreenState == Globals.screenState.OUTPUTMENU:
        if (1 <= Globals.outputMenuPos) and (Globals.outputMenuPos <= 4):
            IOE.toggleOutput(Globals.outputMenuPos)
        elif Globals.outputMenuPos == 5:
            HAAPI.toggleRelay()
        elif Globals.outputMenuPos == 6:
            Globals.currentScreenState = Globals.screenState.MENU
    elif Globals.currentScreenState == Globals.screenState.OFFLINE:
        Globals.currentScreenState = Globals.screenState.MENU

    time.sleep(Globals.debounceTime)
    return


def b4_callback(self):
    if Globals.currentScreenState == Globals.screenState.MENU:
        if (Globals.menuPos == 1) or (Globals.menuPos == 2) or (Globals.menuPos == 4) or (Globals.menuPos == 5):
            Globals.menuPos += 1
    if Globals.currentScreenState == Globals.screenState.LEDMENU:
        if (Globals.LEDMenuPos == 1) or ((3 <= Globals.LEDMenuPos) and (Globals.LEDMenuPos <= 7)):
            Globals.LEDMenuPos += 1
        elif (Globals.LEDMenuPos == 2):
            Globals.LEDMenuPos = 5
    if Globals.currentScreenState == Globals.screenState.OUTPUTMENU:
        if (1 <= Globals.outputMenuPos) and (Globals.outputMenuPos <= 5):
            Globals.outputMenuPos += 1

    time.sleep(Globals.debounceTime)
    return


def b5_callback(self):
    if Globals.currentScreenState == Globals.screenState.MENU:
        if (1 <= Globals.menuPos) and (Globals.menuPos <= 3):
            Globals.menuPos += 3
    if Globals.currentScreenState == Globals.screenState.LEDMENU:
        if (Globals.LEDMenuPos == 1) or (Globals.LEDMenuPos == 2):
            Globals.LEDMenuPos += 2

    time.sleep(Globals.debounceTime)
    return