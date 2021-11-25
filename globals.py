# -*- coding: utf-8 -*-
from enum import Enum


class Globals:
    width = 128
    height = 64

    menuPos = 1
    LEDMenuPos = 1
    outputMenuPos = 1
    debounceTime = 0.1

    class screenState(Enum):
        BLACK = 1
        CLOCK = 2
        MENU = 3
        TEMPMENU = 4
        LIGHTMENU = 5
        LEDMENU = 6
        INPUTMENU = 7
        OUTPUTMENU = 8
        OFFLINE = 9

    currentScreenState = screenState.CLOCK