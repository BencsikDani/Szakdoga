# -*- coding: utf-8 -*-
# Import:
from globals import Globals
import adafruit_ssd1306
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
from haapi import HAAPI
import led
from ioe import IOE
from rtc import RTC


class Display():
    swOff = Image.open("/home/pi/Documents/images/switch/swOff.png")
    swOffSel = Image.open("/home/pi/Documents/images/switch/swOffSel.png")
    swOn = Image.open("/home/pi/Documents/images/switch/swOn.png")
    swOnSel = Image.open("/home/pi/Documents/images/switch/swOnSel.png")
    swArray = [swOnSel, swOffSel, swOn, swOff]

    def initOled():
        spi = board.SPI()
        oled_cs = digitalio.DigitalInOut(board.D7)
        oled_reset = digitalio.DigitalInOut(board.D12)
        oled_dc = digitalio.DigitalInOut(board.D13)
        oled = adafruit_ssd1306.SSD1306_SPI(Globals.width, Globals.height, spi, oled_dc, oled_reset, oled_cs)
        return oled

    def drawText(draw, text, x, y, align, f, size):
        # font = ImageFont.load_default()
        if f == "Thin":
            font = ImageFont.truetype("/home/pi/Documents/Roboto/Roboto-Thin.ttf", size, encoding="unic")
        elif f == "Regular":
            font = ImageFont.truetype("/home/pi/Documents/Roboto/Roboto-Regular.ttf", size, encoding="unic")
        elif f == "Medium":
            font = ImageFont.truetype("/home/pi/Documents/Roboto/Roboto-Medium.ttf", size, encoding="unic")
        elif f == "Black":
            font = ImageFont.truetype("/home/pi/Documents/Roboto/Roboto-Black.ttf", size, encoding="unic")
        else:
            return

        if align == "topleft":
            draw.text((x, y), text, font=font, fill=1)
        elif align == "middle":
            (font_width, font_height) = font.getsize(text)
            draw.text((x - (font_width // 2), y - (font_height // 2)), text, font=font, fill=1)
        else:
            return
        return

    def drawBackButton(image, draw, selected):
        if selected:
            draw.rounded_rectangle((96, 40, 127, 63), radius=11, fill=0, outline=1, width=6)
        else:
            draw.rounded_rectangle((96, 40, 127, 63), radius=11, fill=0, outline=1, width=3)

        backIcon = Image.open("/home/pi/Documents/images/back.png")
        image.paste(backIcon, (104, 47))

        return

    def drawLEDSwitch(image, images, iconPos, state, xy):
        if iconPos == Globals.LEDMenuPos:
            if state == True:
                image.paste(images[0], box=xy)
            else:
                image.paste(images[1], box=xy)
        else:
            if state == True:
                image.paste(images[2], box=xy)
            else:
                image.paste(images[3], box=xy)
        return

    def drawOutputSwitch(image, images, iconPos, state, xy):
        if iconPos == Globals.outputMenuPos:
            if state == True:
                image.paste(images[0], box=xy)
            else:
                image.paste(images[1], box=xy)
        else:
            if state == True:
                image.paste(images[2], box=xy)
            else:
                image.paste(images[3], box=xy)
        return

    def drawOffline(display):
        image = Image.new('1', (Globals.width, Globals.height))
        draw = ImageDraw.Draw(image)

        Display.drawText(draw, "A Home Assistant", Globals.width // 2, 8, "middle", "Medium", 15)
        Display.drawText(draw, "nem elérhető :(", Globals.width // 2, 26, "middle", "Medium", 15)

        draw.rounded_rectangle((46, 39, 82, 63), radius=11, fill=0, outline=1, width=6)
        Display.drawText(draw, "OK", 63, 50, "middle", "Thin", 10)

        image.save("/home/pi/Documents/images/offline.png")
        display.image(image)
        display.show()
        return

    def drawBlack(display):
        display.fill(0)
        display.show()
        return

    def drawClock(display):
        image = Image.new('1', (Globals.width, Globals.height))
        draw = ImageDraw.Draw(image)

        #text = time.strftime("%H:%M:%S", time.localtime())
        dt = RTC.getRTC()
        text = str(dt.tm_hour).zfill(2) + ":" + str(dt.tm_min).zfill(2) + ":" + str(dt.tm_sec).zfill(2)
        Display.drawText(draw, text, Globals.width // 2, Globals.height // 2, "middle", "Thin", 20)

        display.image(image)
        display.show()
        return

    def drawMenu(display, pos):
        image = Image.new('1', (Globals.width, Globals.height))
        draw = ImageDraw.Draw(image)
        margin = 1
        radius = 11
        hBorder1 = 42
        hBorder2 = hBorder1 + 42  # = 84
        hBorder3 = hBorder2 + 42  # = 126
        vBorder1 = Globals.height // 2  # = 32
        vBorder2 = Globals.height  # = 64

        if pos == 1:
            draw.rounded_rectangle((0 + margin, 0, hBorder1 - margin, vBorder1 - (2 * margin)), radius=radius, fill=0, outline=1, width=6)
        else:
            draw.rounded_rectangle((0 + margin, 0, hBorder1 - margin, vBorder1 - (2 * margin)), radius=radius, fill=0, outline=1, width=3)

        if pos == 2:
            draw.rounded_rectangle((hBorder1 + margin, 0, hBorder2 - margin, vBorder1 - (2 * margin)), radius=radius, fill=0, outline=1, width=6)
        else:
            draw.rounded_rectangle((hBorder1 + margin, 0, hBorder2 - margin, vBorder1 - (2 * margin)), radius=radius, fill=0, outline=1, width=3)

        if pos == 3:
            draw.rounded_rectangle((hBorder2 + margin, 0, hBorder3 - margin, vBorder1 - (2 * margin)), radius=radius, fill=0, outline=1, width=6)
        else:
            draw.rounded_rectangle((hBorder2 + margin, 0, hBorder3 - margin, vBorder1 - (2 * margin)), radius=radius, fill=0, outline=1, width=3)

        if pos == 4:
            draw.rounded_rectangle((0 + margin, vBorder1, hBorder1 - margin, vBorder2 - (2 * margin)), radius=radius, fill=0, outline=1, width=6)
        else:
            draw.rounded_rectangle((0 + margin, vBorder1, hBorder1 - margin, vBorder2 - (2 * margin)), radius=radius, fill=0, outline=1, width=3)

        if pos == 5:
            draw.rounded_rectangle((hBorder1 + margin, vBorder1, hBorder2 - margin, vBorder2 - (2 * margin)), radius=radius, fill=0, outline=1, width=6)
        else:
            draw.rounded_rectangle((hBorder1 + margin, vBorder1, hBorder2 - margin, vBorder2 - (2 * margin)), radius=radius, fill=0, outline=1, width=3)

        if pos == 6:
            draw.rounded_rectangle((hBorder2 + margin, vBorder1, hBorder3 - margin, vBorder2 - (2 * margin)), radius=radius, fill=0, outline=1, width=6)
        else:
            draw.rounded_rectangle((hBorder2 + margin, vBorder1, hBorder3 - margin, vBorder2 - (2 * margin)), radius=radius, fill=0, outline=1, width=3)

        tempImage = Image.open("/home/pi/Documents/images/temp.png")
        image.paste(tempImage, box=(9, 7))
        lightImage = Image.open("/home/pi/Documents/images/light.png")
        image.paste(lightImage, box=(51, 7))
        LEDImage = Image.open("/home/pi/Documents/images/led.png")
        image.paste(LEDImage, box=(93, 7))
        inputImage = Image.open("/home/pi/Documents/images/input.png")
        image.paste(inputImage, box=(9, 39))
        outputImage = Image.open("/home/pi/Documents/images/output.png")
        image.paste(outputImage, box=(51, 39))
        offImage = Image.open("/home/pi/Documents/images/off.png")
        image.paste(offImage, box=(93, 39))

        # image.save("/home/pi/Documents/images/screen.png")
        display.image(image)
        display.show()
        return

    def drawTempMenu(display):
        temp = HAAPI.getTemperature()
        if temp == -1:
            Globals.currentScreenState = Globals.screenState.OFFLINE
        else:
            image = Image.new('1', (Globals.width, Globals.height))
            draw = ImageDraw.Draw(image)

            Display.drawText(draw, "Hőmérséklet:", 5, 5, "topleft", "Medium", 15)
            Display.drawText(draw, str(temp) + " °C", 5, 30, "topleft", "Thin", 15)

            Display.drawBackButton(image, draw, True)

            display.image(image)
            display.show()
        return

    def drawLightMenu(display):
        light = HAAPI.getLight()
        if light == -1:
            Globals.currentScreenState = Globals.screenState.OFFLINE
        else:
            image = Image.new('1', (Globals.width, Globals.height))
            draw = ImageDraw.Draw(image)

            Display.drawText(draw, "Fényerősség:", 5, 5, "topleft", "Medium", 15)
            Display.drawText(draw, str(light) + " lx", 5, 30, "topleft", "Thin", 15)

            Display.drawBackButton(image, draw, True)

            display.image(image)
            display.show()
        return

    def drawLEDMenu(display, pos):
        image = Image.new('1', (Globals.width, Globals.height))
        draw = ImageDraw.Draw(image)

        Display.drawLEDSwitch(image, Display.swArray, 1, led.getLED(1), (2, 0))
        Display.drawLEDSwitch(image, Display.swArray, 2, led.getLED(2), (19, 0))
        Display.drawLEDSwitch(image, Display.swArray, 3, led.getLED(3), (2, 32))
        Display.drawLEDSwitch(image, Display.swArray, 4, led.getLED(4), (19, 32))
        Display.drawLEDSwitch(image, Display.swArray, 5, HAAPI.getLED1(), (38, 16))
        Display.drawLEDSwitch(image, Display.swArray, 6, HAAPI.getLED2(), (55, 16))
        Display.drawLEDSwitch(image, Display.swArray, 7, HAAPI.getSonoff(), (78, 16))

        if pos == 8:
            Display.drawBackButton(image, draw, True)
        else:
            Display.drawBackButton(image, draw, False)

        display.image(image)
        display.show()
        return

    def drawInputMenu(display):
        image = Image.new('1', (Globals.width, Globals.height))
        draw = ImageDraw.Draw(image)

        Display.drawText(draw, "Bemenetek:", 0, 0, "topleft", "Medium", 15)

        if IOE.getInput(4):
            draw.ellipse((2, 20, 22, 40), fill=1, outline=1, width=3)
        else:
            draw.ellipse((2, 20, 22, 40), fill=None, outline=1, width=3)
        if IOE.getInput(3):
            draw.ellipse((26, 20, 46, 40), fill=1, outline=1, width=3)
        else:
            draw.ellipse((26, 20, 46, 40), fill=None, outline=1, width=3)
        if IOE.getInput(2):
            draw.ellipse((50, 20, 70, 40), fill=1, outline=1, width=3)
        else:
            draw.ellipse((50, 20, 70, 40), fill=None, outline=1, width=3)
        if IOE.getInput(1):
            draw.ellipse((74, 20, 94, 40), fill=1, outline=1, width=3)
        else:
            draw.ellipse((74, 20, 94, 40), fill=None, outline=1, width=3)

        Display.drawText(draw, "4", 12, 50, "middle", "Regular", 15)
        Display.drawText(draw, "3", 36, 50, "middle", "Regular", 15)
        Display.drawText(draw, "2", 60, 50, "middle", "Regular", 15)
        Display.drawText(draw, "1", 84, 50, "middle", "Regular", 15)

        Display.drawBackButton(image, draw, True)

        display.image(image)
        display.show()
        return

    def drawOutputMenu(display, pos):
        image = Image.new('1', (Globals.width, Globals.height))
        draw = ImageDraw.Draw(image)

        Display.drawText(draw, "Kimenetek:", 0, 0, "topleft", "Medium", 15)

        Display.drawOutputSwitch(image, Display.swArray, 1, IOE.getOutput(1), (4, 18))
        Display.drawOutputSwitch(image, Display.swArray, 2, IOE.getOutput(2), (21, 18))
        Display.drawOutputSwitch(image, Display.swArray, 3, IOE.getOutput(3), (38, 18))
        Display.drawOutputSwitch(image, Display.swArray, 4, IOE.getOutput(4), (55, 18))
        Display.drawOutputSwitch(image, Display.swArray, 5, HAAPI.getRelay(), (77, 18))

        Display.drawText(draw, "1", 11, 57, "middle", "Regular", 15)
        Display.drawText(draw, "2", 28, 57, "middle", "Regular", 15)
        Display.drawText(draw, "3", 45, 57, "middle", "Regular", 15)
        Display.drawText(draw, "4", 62, 57, "middle", "Regular", 15)
        Display.drawText(draw, "ext", 84, 57, "middle", "Regular", 15)

        if pos == 6:
            Display.drawBackButton(image, draw, True)
        else:
            Display.drawBackButton(image, draw, False)

        display.image(image)
        display.show()
        return