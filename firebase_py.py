import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import requests

cred = credentials.Certificate('Key_OracleIoT.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://oracle-iot-pm-default-rtdb.firebaseio.com/"
})

ref = db.reference('/OracleIoT/Credenciales')
print(ref.get())