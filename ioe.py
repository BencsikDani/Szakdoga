# -*- coding: utf-8 -*-
# Import:
import smbus
import time


class IOE:
    bus = smbus.SMBus(1)

    # Címek
    device = 0x20
    config = 0x05
    iodira = 0x00
    iodirb = 0x01
    gpioa = 0x12
    gpiob = 0x13
    olata = 0x14
    olatb = 0x15

    def initIoe():
        # BANK = 0
        originalConfig = IOE.bus.read_byte_data(IOE.device, IOE.config)
        originalConfig = originalConfig & 0b01111111
        IOE.bus.write_byte_data(IOE.device, IOE.config, originalConfig)

        # IODIR
        # 0 = output; 1 = input
        IOE.bus.write_byte_data(IOE.device, IOE.iodira, 0b00001111)
        IOE.bus.write_byte_data(IOE.device, IOE.iodirb, 0b00000000)

        # Output nullára
        IOE.bus.write_byte_data(IOE.device, IOE.olatb, 0)
        return

    def relayTest():
        IOE.bus.write_byte_data(IOE.device, IOE.olatb, 0b0000)
        time.sleep(1)
        IOE.bus.write_byte_data(IOE.device, IOE.olatb, 0b0001)
        time.sleep(1)
        IOE.bus.write_byte_data(IOE.device, IOE.olatb, 0b0011)
        time.sleep(1)
        IOE.bus.write_byte_data(IOE.device, IOE.olatb, 0b0111)
        time.sleep(1)
        IOE.bus.write_byte_data(IOE.device, IOE.olatb, 0b1111)
        time.sleep(1)
        IOE.bus.write_byte_data(IOE.device, IOE.olatb, 0b0000)
        return

    def optoTest():
        readByte = IOE.bus.read_byte_data(IOE.device, IOE.gpioa)
        print(readByte)

    def getInput(input):
        # input = 1...4
        readByte = IOE.bus.read_byte_data(IOE.device, IOE.gpioa)
        if input == 1:
            return readByte & 0b0001
        elif input == 2:
            return readByte & 0b0010
        elif input == 3:
            return readByte & 0b0100
        elif input == 4:
            return readByte & 0b1000
        else:
            return False

    def getOutput(output):
        # output = 1...4
        readByte = IOE.bus.read_byte_data(IOE.device, IOE.gpiob)
        if output == 1:
            return readByte & 0b0001
        elif output == 2:
            return readByte & 0b0010
        elif output == 3:
            return readByte & 0b0100
        elif output == 4:
            return readByte & 0b1000
        else:
            return False

    def setOutput(output, value):
        # output = 1...4
        readByte = IOE.bus.read_byte_data(IOE.device, IOE.gpiob)

        if value:
            if output == 1:
                writeByte = readByte | 0b0001
            elif output == 2:
                writeByte = readByte | 0b0010
            elif output == 3:
                writeByte = readByte | 0b0100
            elif output == 4:
                writeByte = readByte | 0b1000
        elif not value:
            if output == 1:
                writeByte = readByte & ~(0b0001)
            elif output == 2:
                writeByte = readByte & ~(0b0010)
            elif output == 3:
                writeByte = readByte & ~(0b0100)
            elif output == 4:
                writeByte = readByte & ~(0b1000)

        IOE.bus.write_byte_data(IOE.device, IOE.olatb, writeByte)
        return

    def toggleOutput(output):
        # output = 1...4
        if IOE.getOutput(output):
            IOE.setOutput(output, 0)
        else:
            IOE.setOutput(output, 1)
        return