# -*- coding: utf-8 -*-
# Import:
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library


class LED:
    def ledInit():
        GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)

    def resetLEDs():
        for led in range(1, 5):
            GPIO.output(led + 21, GPIO.LOW)

    def getLED(led):
        # led = 1...4
        if (led == 1 or led == 4):
            return GPIO.input(led + 21)
        elif led == 2:
            return GPIO.input(24)
        elif led == 3:
            return GPIO.input(23)

    def setLED(led, state):
        # led = 1...4
        if state:
            if (led == 1 or led == 4):
                GPIO.output(led + 21, GPIO.HIGH)
            elif led == 2:
                GPIO.output(24, GPIO.HIGH)
            elif led == 3:
                GPIO.output(23, GPIO.HIGH)
        elif not state:
            if (led == 1 or led == 4):
                GPIO.output(led + 21, GPIO.LOW)
            elif led == 2:
                GPIO.output(24, GPIO.LOW)
            elif led == 3:
                GPIO.output(23, GPIO.LOW)

    def toggleLED(led):
        # led = 1...4
        if LED.getLED(led):
            LED.setLED(led, 0)
        else:
            LED.setLED(led, 1)