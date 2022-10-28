import time
import requests
import base64
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import urllib.request
from urllib3.exceptions import InsecureRequestWarning

FIREBASE_HOST = "https://oracle-iot-pm-default-rtdb.firebaseio.com/"
HTTP_CONECTOR = "https://iotdemo00177.device.cna.phx.demoservices005.iot.oraclepdemos.com/cgw/CIS-URCobot-HTTP"

device_id = "CIS-URCobot"
base_current = 0
shoulder_current = 0
elbow_current = 0
wirst1_current = 0
wirst2_current = 0
wirst3_current = 0
base_temperature = 0
shoulder_temperature = 0
elbow_temperature = 0
wirst1_temperature = 0
wirst2_temperature = 0
wirst3_temperature = 0
cycle_counter = 0
program_state = 0


def Connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host, timeout=5)  # Si usas Python 2.x coloca: urllib.urlopen()
        return True
    except:
        return False

credentials_fb = credentials.Certificate('Key_OracleIoT.json')
firebase_admin.initialize_app(credentials_fb, {
    'databaseURL': FIREBASE_HOST
})

ref = db.reference('/OracleIoT/Credenciales')
json_fb = ref.get()
credentials_str = json_fb['User'] + ":" + json_fb['Password']

credentials_pm = base64.b64encode(bytes(credentials_str, 'utf-8')).decode("ascii")
headers = {'Authorization': 'Basic %s' % credentials_pm, "Content-Type": "application/json"}
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

while True:
    if Connect():
        json_data = json.dumps({
            "id": device_id,
            "base_current": base_current,
            "shoulder_current": shoulder_current,
            "elbow_current": elbow_current,
            "wirst1_current": wirst1_current,
            "wirst2_current": wirst2_current,
            "wirst3_current": wirst3_current,
            "base_temperature": base_temperature,
            "shoulder_temperature": shoulder_current,
            "elbow_temperature": elbow_current,
            "wirst1_temperature": wirst1_temperature,
            "wirst2_temperature": wirst2_temperature,
            "wirst3_temperature": wirst3_temperature,
            "cycle_counter": cycle_counter,
            "program_state": program_state
        })
        send_data = requests.post(url=HTTP_CONECTOR, headers=headers, data=json_data, verify=False)

        if send_data.text == 'Not authenticated':
            print(f"Reconectado. {send_data.text}")
            json_fb = ref.get()
            credentials_str = json_fb['User'] + ":" + json_fb['Password']
            credentials_pm = base64.b64encode(bytes(credentials_str, 'utf-8')).decode("ascii")
            headers = {'Authorization': 'Basic %s' % credentials_pm, "Content-Type": "application/json"}
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        else:
            print(f"Conectado. {send_data.text}")
    else:
        print("Sin conexión a internet.")

    time.sleep(10)
