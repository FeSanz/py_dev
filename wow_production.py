import time
import requests
import base64
import json
import urllib.request
import random
from urllib3.exceptions import InsecureRequestWarning

url_iot = 'https://iotdemo00177.device.cna.phx.demoservices005.iot.oraclepdemos.com/direct/v1/schema/entities/'
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def Connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host, timeout=5)  # Si usas Python 2.x coloca: urllib.urlopen()
        return True
    except:
        return False

def AssamblyMachine(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5WZGKSRC12EH": random.randint(200,215),#weight
        "5WZGKSRC12EG": random.randint(25,30),#presure
            "5WZGKSR412EG":  random.randint(8,13),#voltage
        "5WZGKSRG12EG":  random.randint(500,700),#items
        "5WZGKSR012EG": random.randint(29,36) #temperarure
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"AssamblyMachine. {send_data.text}")

def PerformanceMachine(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5WZHVV9012EG": random.randint(29,36), #temperature
        "5WZHVV9412EG": random.randint(45,60), #frequency
        "5WZHVV8W12EG": performance, #performance
        "5WZHVV9812EG": inspection_performance  #inspection
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"PerformaceMachine. {send_data.text}")

def QualityMachine(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5WZJ76T01AA0": random.randint(29,36), #temperature
        "5WZJ76T41AA0": charger, #charge
        "5WZJ76T81AA0": inspection_quality, #inspection
        "5WZJ76SW1AA0": queality  #quality
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"QualityMachine. {send_data.text}")

def MonogramMachine(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5WZJJKRW1AA0": installation, #installation
        "5WZJJKS01AA0": launch, #launch
        "5WZJJKRR1AA0": extraction  #extraction
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"MonogramMachine. {send_data.text}")

performance = random.randint(0,30)
inspection_performance = random.randint(0,30)
queality = random.randint(0,30)
charger = random.randint(0,30)
inspection_quality = random.randint(0,30)
extraction = random.randint(0,30)
installation = random.randint(0,30)
launch = random.randint(0,30)


while True:
    if Connect():
        if performance <= 100:
            performance += random.randint(2,5)
        else:
            performance = 0

        if inspection_performance <= 100:
            inspection_performance += random.randint(2,5)
        else:
            inspection_performance = 0

        if queality <= 100:
            queality += random.randint(2,5)
        else:
            queality = 0

        if charger <= 100:
            charger += random.randint(2,5)
        else:
            charger = 0

        if inspection_quality <= 100:
            inspection_quality += random.randint(2, 5)
        else:
            inspection_quality = 0

        if extraction <= 100:
            extraction += random.randint(2, 5)
        else:
            extraction = 0

        if installation <= 100:
            installation += random.randint(2, 5)
        else:
            installation = 0

        if launch <= 100:
            launch += random.randint(2, 5)
        else:
            launch = 0

        AssamblyMachine("AssamblyMachine")
        PerformanceMachine("PerformanceMachine")
        QualityMachine("QualityMachine")
        MonogramMachine("MonogramMachine")
        print("******************************")
    else:
        print("Sin conexión a internet.")
    time.sleep(10)
