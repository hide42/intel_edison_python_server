import mraa
import pykka
import time

class ThermMetr(pykka.ThreadingActor):
    def __init__(self,pin,frequency = 0.2):
        super(ThermMetr,self).__init__()
        self.therma = mraa.Aio(pin)
        self.frequency=frequency
    def getTemp(self):
        reading=self.therma.read()
        v = 5.0/1024*reading
        temp = (v-0.55)*100
        return temp

    #test
    def start(self):
        while(True):
            temp=self.getTemp()
            print(temp)
            time.sleep(self.frequency)
