from flask import Flask
import json
import random

app = Flask(__name__)

data_obj = {
    "mac": "D8:80:39:91:73:89",
    "hw": "3.0",
    "sw": "1.58a",
    "vin": 4349,
    "tem": 3149,
    "diff1": "0",
    "diff2": "0",
    "diff3": "0",
    "dthTemp": "-600",
    "dthHum": "-600",
    "bm280p": "-600",
    "ds1": -478,
    "ds2": "-600",
    "ds3": "-600",
    "ds4": "-600",
    "ds5": "-600",
    "ds6": "-600",
    "ds7": "-600",
    "ds8": "-600",
    "out0": "0",
    "out1": "0",
    "out2": "0",
    "out3": "0",
    "out4": "0",
    "out5": "0",
    "inpp1": "5475",
    "inpp2": "2",
    "inpp3": "2",
    "inpp4": "2",
    "inpp5": "0",
    "inpp6": "0",
    "pwm": "0",
    "pwmd0": "50",
    "pwmd1": "50",
    "pwmd2": "50",
    "pwmd3": "73",
    "ind": "15",
    "power1": "2997",
    "power2": "2997",
    "power3": "2997",
    "power4": "2997",
    "energy1": "273490",
    "energy2": "273490",
    "energy3": "273490",
    "energy4": "273490",
    "pm1": "4",
    "pm2": "6",
    "pm4": "8",
    "pm10": "8",
    "co2": "-1",
    "d0": "0",
    "d1": "0",
    "d2": "0",
    "d3": "0",
    "d4": "0",
    "d5": "0",
    "d6": "0",
    "d7": "0",
    "d8": "0",
    "sdm1": "0",
    "sdm2": "0",
    "sdm3": "0",
    "sdm4": "0",
    "sdm5": "0",
    "sdm6": "0",
    "sdm7": "0",
    "sdm8": "0",
    "sdm9": "0",
    "sdm10": "0",
    "sdm11": "0",
    "sdm12": "0",
    "sdm13": "0",
    "sdm14": "0",
    "diffsel": "0*0*0*0*0*0*0*0*0"
}

init = False
initValues = {}
HISTERESYS = 25

@app.route('/')
def index():
    global init
    global HISTERESYS
    global initValues

    if not init:
        data_obj['vin'] = random.randrange(800,5500)
        data_obj['tem'] = random.randrange(-2000,8500)
        data_obj['ds1'] = random.randrange(-550 , 1250)
        init = True
        initValues['tem'] = data_obj['tem']
        initValues['vin'] = data_obj['vin']
        initValues['ds1'] = data_obj['ds1']
    else:
        data_obj['tem'] = random.randrange(initValues['tem'] - HISTERESYS, initValues['tem'] + HISTERESYS)
        data_obj['vin'] = random.randrange(initValues['vin'] - HISTERESYS, initValues['vin'] + HISTERESYS)
        data_obj['ds1'] = random.randrange(initValues['ds1'] - HISTERESYS, initValues['ds1'] + HISTERESYS)
    
    json_data = json.dumps(data_obj,indent=4)
    return json_data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)



