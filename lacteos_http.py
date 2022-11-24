import time
import requests
import base64
import json
import urllib.request
import random
from urllib3.exceptions import InsecureRequestWarning

url_iot = 'https://iotdemo00177.device.cna.phx.demoservices005.iot.oraclepdemos.com/direct/v1/schema/entities/'
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

tanques = {0,0}
status = {False, False}

def Connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host, timeout=5)  # Si usas Python 2.x coloca: urllib.urlopen()
        return True
    except:
        return False

def Almacen_Envasado(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5R30N7KR12EG": round(random.uniform(4.9, 5.9), 1), #temp
        "5R30N7M412EG": round(random.uniform(6.6, 6.7), 1), #ph
        "5R30N7M012EG": round(random.uniform(0.3, 0.9), 1), #flujo
        "5R30N7M412EH": random.randint(40,50), #conduc
        "5R30N7KW12EG": random.randint(60,75) #presion
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Almacen_Envasado. {send_data.text}")

def Almacen_Filtro(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5R30N7KR12EG": round(random.uniform(4.9, 5.9), 1),  # temp
        "5R30N7M412EG": round(random.uniform(6.6, 6.7), 1),  # ph
        "5R30N7M012EG": round(random.uniform(0.3, 0.9), 1),  # flujo
        "5R30N7M412EH": random.randint(40, 50),  # conduc
        "5R30N7KW12EG": random.randint(60, 75)  # presion
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Almacen_Filtro. {send_data.text}")

def Tanque_Planta(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5R1QVX1M1AA0": round(random.uniform(4.9, 5.9), 1), #temperatura
        "5R1QVX1R1AA0": 7000, #litros
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Tanque_Planta. {send_data.text}")

def Tanque_Granja(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5R1QVX1M1AA0": round(random.uniform(4.9, 5.9), 1),  # temperatura
        "5R1QVX1R1AA0": 7000,  # litros
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Tanque_Planta. {send_data.text}")

def Pasteurizacion(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5R2ZTG301AA0": random.randint(100,105), #estandarizacion
        "5R2ZTG381AA0": random.randint(140, 145), #esterilizacion
        "5R2ZTG2W1AA0": random.randint(70, 75), #suave
        "5R2ZTG341AA0": random.randint(135, 140) #uht
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Pasteurizacion. {send_data.text}")

def Desnatado(id):
    auth = base64.b64encode(bytes(id + ":CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "5R31NFS812EG": round(random.uniform(1.1, 1.5), 1), #semi
        "5R31NFSC12EG": round(random.uniform(0.1, 0.5), 1), #descremada
        "5R31NFS412EG": round(random.uniform(3.1, 3.5), 1) #entera
    })
    send_data = requests.post(url=url_iot + id + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Desnatado. {send_data.text}")

while True:
    if Connect():
        Almacen_Envasado("5R313B2812EG")
        Almacen_Filtro("5R30Z9HC12EG")
        Desnatado("5R31YTB412EG")
        Pasteurizacion("5R30T4XG12EG")
        Tanque_Granja("5R1SR4J01AA0")
        Tanque_Planta("5R2XVPBG12EG")
        print("******************************")
    else:
        print("Sin conexión a internet.")
    time.sleep(10)
