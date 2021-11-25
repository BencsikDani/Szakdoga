import time
from globals import Globals

class Sleeper:
    startTime = time.time()
    interval = 60

    def resetCount():
        Sleeper.startTime = time.time()
        return

    def checkIfTimeRanOut():
        if (time.time() - Sleeper.startTime) > Sleeper.interval:
            Globals.currentScreenState = Globals.screenState.BLACK
        return