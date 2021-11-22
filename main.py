# Import:
from globals import Globals
import RPi.GPIO as GPIO  # Import Raspberry Pi GPIO library
import buttons
from display import Display
from ioe import IOE
import led

# Main Code

GPIO.cleanup()
# GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering

oled = Display.initOled()
buttons.initButtons()
IOE.initIoe()
led.ledInit()

while True:
    if Globals.currentScreenState == Globals.screenState.BLACK:
        Display.drawBlack(oled)
    elif Globals.currentScreenState == Globals.screenState.CLOCK:
        Display.drawClock(oled)
    elif Globals.currentScreenState == Globals.screenState.MENU:
        Display.drawMenu(oled, Globals.menuPos)
    elif Globals.currentScreenState == Globals.screenState.TEMPMENU:
        Display.drawTempMenu(oled)
    elif Globals.currentScreenState == Globals.screenState.LIGHTMENU:
        Display.drawLightMenu(oled)
    elif Globals.currentScreenState == Globals.screenState.LEDMENU:
        Display.drawLEDMenu(oled, Globals.LEDMenuPos)
    elif Globals.currentScreenState == Globals.screenState.INPUTMENU:
        Display.drawInputMenu(oled)
    elif Globals.currentScreenState == Globals.screenState.OUTPUTMENU:
        Display.drawOutputMenu(oled, Globals.outputMenuPos)

































        #time.sleep(1)
