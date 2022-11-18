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

def Almacen_Envasado():
    auth = base64.b64encode(bytes("Almacen_Envasado:CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "4Z169H0C1AJG": round(random.uniform(4.9, 5.9), 1), #temp
        "4Z169H141AJG": round(random.uniform(6.6, 6.7), 1), #ph
        "4Z169H0W1AJG": round(random.uniform(0.3, 0.9), 1), #flujo
        "4Z169H1C1AJG": random.randint(40,50), #conduc
        "sys_location": {
            "sys_altitude": 72,
            "sys_latitude": 37.39353247764676,
            "sys_longitude": -121.95359884794176
        },
        "4Z169H0M1AJG": random.randint(60,75) #presion
    })
    send_data = requests.post(url=url_iot + "Almacen_Envasado" + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Almacen_Envasado. {send_data.text}")

def Descarga_Filtro():
    auth = base64.b64encode(bytes("Descarga_Filtro:CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "4Z0XRZ8C1AJG": round(random.uniform(0.3, 0.9), 1), #flujo
        "4ZVZ5X341AJ0": {
            "4Z0R8DJ81AJ0": 50,
            "4Z0R8DJR1AJ0": 50
        },
        "4Z0XRZ701AJG": round(random.uniform(4.9, 5.9), 1), #temp
        "4Z0XRZ7W1AJG": random.randint(60,75), #pres
        "4Z0XRZ981AJG": random.randint(40,50), #conduc
        "4Z0XRZ8R1AJG": round(random.uniform(6.6, 6.7), 1), #ph
        "sys_location": {
            "sys_altitude": 72,
            "sys_latitude": 37.39353247764676,
            "sys_longitude": -121.95359884794176
        }
    })

    send_data = requests.post(url=url_iot + "Descarga_Filtro" + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Descarga_Filtro. {send_data.text}")

def Descremado_Entrada():
    auth = base64.b64encode(bytes("Descremado_Entrada:CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "4Z11HCH41AJG": round(random.uniform(0.3, 0.9), 1), #flujo
        "4Z11HCGM1AJG": random.randint(60,75), #presion
        "sys_location": {
            "sys_altitude": 72,
            "sys_latitude": 37.39353247764676,
            "sys_longitude": -121.95359884794176
        }
    })

    send_data = requests.post(
        url= url_iot + "Descremado_Entrada" + "/json",
        headers=headers, data=json_data, verify=False)

    print(f"Descremado_Entrada. {send_data.text}")

def Descremado_Cruda():
    auth = base64.b64encode(bytes("Descremado_Cruda:CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "4Z11HCH41AJG": round(random.uniform(0.3, 0.9), 1), #flujo
        "4Z11HCGM1AJG": random.randint(60,75), #presion
        "sys_location": {
            "sys_altitude": 72,
            "sys_latitude": 37.39353247764676,
            "sys_longitude": -121.95359884794176
        }
    })

    send_data = requests.post(
        url= url_iot + "Descremado_Cruda" + "/json",
        headers=headers, data=json_data, verify=False)

    print(f"Descremado_Cruda. {send_data.text}")

def Homogenizacion_Pasteurizacion():
    auth = base64.b64encode(bytes("Homogenizacion_Pasteurizacion:CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "4ZVK2YPM1AJ0": round(random.uniform(55.1, 99.9), 1), #temp_a
        "4ZVK2YQ01AJ0": round(random.uniform(100.1, 139.9), 1), #temp_b
        "sys_location": {
            "sys_altitude": 72,
            "sys_latitude": 37.39353247764676,
            "sys_longitude": -121.95359884794176
        }
    })

    send_data = requests.post(
        url= url_iot + "Homogenizacion_Pasteurizacion" + "/json",
        headers=headers, data=json_data, verify=False)

    print(f"Homogenizacion_Pasteurizacion. {send_data.text}")

def Tanque_Silo():
    auth = base64.b64encode(bytes("Tanque_Silo:CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_data = json.dumps({
        "4Z0R8DJ81AJ0": round(random.uniform(4.9, 5.9), 1), #temperatura
        "4Z0R8DJR1AJ0": 7000, #litros
        "sys_location": {
            "sys_altitude": 72,
            "sys_latitude": 37.39353247764676,
            "sys_longitude": -121.95359884794176
        }
    })
    send_data = requests.post(url=url_iot + "Tanque_Silo" + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Tanque_Silo. {send_data.text}")

def Tanque_Granja():
    '''
    if tanques[0] == 0:
        tanques[0] += round(random.uniform(10.5, 50.2), 2)
    elif 0 < tanques[0] < 10000:
        tanques[0] += round(random.uniform(10.5, 50.2), 2)
    elif'''

    auth = base64.b64encode(bytes("Tanque_Granja:CondorXR112", 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}
    json_data = json.dumps({
        "4Z0R8DJ81AJ0": round(random.uniform(4.9, 5.9), 1), #temperatura
        "4Z0R8DJR1AJ0": 5000, #litros
        "sys_location": {
            "sys_altitude": 72,
            "sys_latitude": 37.39353247764676,
            "sys_longitude": -121.95359884794176
        }
    })
    send_data = requests.post(url=url_iot + "Tanque_Granja" + "/json",
                              headers=headers, data=json_data, verify=False)

    print(f"Tanque_Granja. {send_data.text}")

while True:
    if Connect():
        Almacen_Envasado()
        Descarga_Filtro()
        Descremado_Entrada()
        Descremado_Cruda()
        Homogenizacion_Pasteurizacion()
        Tanque_Silo()
        Tanque_Granja()
        print("******************************")
    else:
        print("Sin conexión a internet.")
    time.sleep(10)
