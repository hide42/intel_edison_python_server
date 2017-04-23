
from app import app



@app.route('/')
@app.route('/index')
def index():
    return "/temp /ligh /flashOn /flashOff /flash"



@app.route('/temp')
def index1():
    return str(pribor1.getTemp())


@app.route('/ligh')
def index2():
    return str(pribor2.getTemp())


@app.route('/flashOn')
def index3():
    flashLight.turn_on()
    return "on"

@app.route('/flashOff')
def index4():
    flashLight.turn_off()
    return "off"

@app.route('/flash')
def index5():
    return str(flashLight.isOn())



import flashlight
flashLight = flashlight.Flash(pin=13)
import therm
pribor1 = therm.ThermMetr(pin=1)
import lightometr
pribor2 = lightometr.LightMetr(pin=0)