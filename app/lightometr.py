import pykka
import time
import pyupm_grove

class LightMetr(pykka.ThreadingActor):
    def __init__(self, pin, frequency=0.2):
        super(LightMetr,self).__init__()
        self.light = pyupm_grove.GroveLight(pin)
        self.frequency=frequency

    def getTemp(self):
        readT=self.light.value()
        return readT

    #test
    def start(self):
        while(True):
            temp=self.getTemp()
            print(temp)
            time.sleep(self.frequency)
