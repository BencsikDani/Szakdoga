import requests
import json

class HAAPI:
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI2ZjI3OGZhZmM3MGM0NTI4YWY5Y2U4Y2NmZjZhNTUzZCIsImlhdCI6MTYzNzE0NDcxOCwiZXhwIjoxOTUyNTA0NzE4fQ.F1w1a8J-QNQRt5GkkPkAmpX_PO4kwelr8XjjA-KPSJE"
    urlBase = "http://localhost:8123/"
    temperatureStateTag = "api/states/sensor.homerseklet_erzekelo"
    lightStateTag = "api/states/sensor.fenyerzekelo"
    LED1StateTag = "api/states/light.led1"
    LED2StateTag = "api/states/light.led2"
    sonoffStateTag = "api/states/light.1001018297"
    relayStateTag = "api/states/switch.relay"
    headers = {
        "Authorization": ("Bearer " + token),
        "content-type": "application/json",
    }

    def getTemperature():
        response = requests.get(HAAPI.urlBase + HAAPI.temperatureStateTag, headers=HAAPI.headers)
        data = json.loads(response.text)
        #print("Hőmérséklet: " + data["state"] + " °C")
        if data["state"] == "unavailable":
            return "??.?"
        else:
            return data["state"]

    def getLight():
        response = requests.get(HAAPI.urlBase + HAAPI.lightStateTag, headers=HAAPI.headers)
        data = json.loads(response.text)
        #print("Fényerősség: " + data["state"] + " lx")
        if data["state"] == "unavailable":
            return "??.?"
        else:
            return data["state"]

    def getLED1():
        response = requests.get(HAAPI.urlBase + HAAPI.LED1StateTag, headers=HAAPI.headers)
        data = json.loads(response.text)
        if data["state"] == "on":
            return True
        elif data["state"] == "off":
            return False

    def getLED2():
        response = requests.get(HAAPI.urlBase + HAAPI.LED2StateTag, headers=HAAPI.headers)
        data = json.loads(response.text)
        if data["state"] == "on":
            return True
        elif data["state"] == "off":
            return False

    def setLED1(state):
        if state:
            command = "api/services/light/turn_on"
        elif not state:
            command = "api/services/light/turn_off"

        entity = {"entity_id": "light.led1"}
        requests.post(HAAPI.urlBase + command, headers=HAAPI.headers, json=entity)

    def setLED2(state):
        if state:
            command = "api/services/light/turn_on"
        elif not state:
            command = "api/services/light/turn_off"

        entity = {"entity_id": "light.led2"}
        requests.post(HAAPI.urlBase + command, headers=HAAPI.headers, json=entity)

    def toggleLED(led):
        if led == 1:
            if HAAPI.getLED1():
                HAAPI.setLED1(0)
            else:
                HAAPI.setLED1(1)
        elif led == 2:
            if HAAPI.getLED2():
                HAAPI.setLED2(0)
            else:
                HAAPI.setLED2(1)

    def getSonoff():
        response = requests.get(HAAPI.urlBase + HAAPI.sonoffStateTag, headers=HAAPI.headers)
        data = json.loads(response.text)
        if data["state"] == "on":
            return True
        elif data["state"] == "off":
            return False

    def setSonoff(state):
        if state:
            command = "api/services/light/turn_on"
        elif not state:
            command = "api/services/light/turn_off"

        entity = {"entity_id": "light.1001018297"}
        requests.post(HAAPI.urlBase + command, headers=HAAPI.headers, json=entity)

    def toggleSonoff():
        if HAAPI.getSonoff():
            HAAPI.setSonoff(0)
        else:
            HAAPI.setSonoff(1)
        return

    def getRelay():
        response = requests.get(HAAPI.urlBase + HAAPI.relayStateTag, headers=HAAPI.headers)
        data = json.loads(response.text)
        if data["state"] == "on":
            return True
        elif data["state"] == "off":
            return False
        return

    def setRelay(state):
        if state:
            command = "api/services/switch/turn_on"
        elif not state:
            command = "api/services/switch/turn_off"

        entity = {"entity_id": "switch.relay"}
        requests.post(HAAPI.urlBase + command, headers=HAAPI.headers, json=entity)

    def toggleRelay():
        if HAAPI.getRelay():
            HAAPI.setRelay(0)
        else:
            HAAPI.setRelay(1)
        return
