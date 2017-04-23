
import mraa
import time

class Flash():
    def __init__(self,pin):
        self.light = mraa.Gpio(pin)
        self.light.dir(mraa.DIR_OUT)
        self.bool = False
    def turn_on(self):
        self.light.write(1)
        self.bool = True
    def turn_off(self):
        self.light.write(0)
        self.bool = False
    def isOn(self):
        return self.bool
