# -*- coding: utf-8 -*-
from enum import Enum


class Globals:
    width = 128
    height = 64
    border = 5

    text = "Szia Csengeee"
    wait = 1.5
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

    currentScreenState = screenState.CLOCK