import time
import requests
import base64
import json
import urllib.request
import random
from urllib3.exceptions import InsecureRequestWarning

url_scm = 'https://fa-eseu-saasfademo1.ds-fa.oraclepdemos.com/'
credentials = "SCM_IMPL:bCE5q#5%"
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def Connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host, timeout=5)  # Si usas Python 2.x coloca: urllib.urlopen()
        return True
    except:
        return False


def ResponseTransaction(json_transaction):
    try:
        jsonDeserializer = json.loads(json_transaction)  # load json para archivos y loads json para cadenas
        if jsonDeserializer['ErrorsExistFlag'] == "true":
            print(f"Transaction {jsonDeserializer['MaterialTransactionDetail'][0]['InventoryItemNumber']} Error. "
                  f"{jsonDeserializer['MaterialTransactionDetail'][0]['ErrorMessages']}")
        else:
            print(f"Transaction {jsonDeserializer['MaterialTransactionDetail'][0]['InventoryItemNumber']} Success. "
                  f"ID: {jsonDeserializer['MaterialTransactionDetail'][0]['InvTransactionId']} - "
                  f"Date: {jsonDeserializer['MaterialTransactionDetail'][0]['TransactionDate']}")
    except:
        print("Ocurrio un error al leer datos JSON")


def WOMaterialTransaction(item, quantity):
    auth = base64.b64encode(bytes(credentials, 'utf-8')).decode("ascii")
    headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}

    json_request = json.dumps({
        "SourceSystemType": "EXTERNAL",
        "MaterialTransactionDetail": [
            {
                "InventoryItemNumber": item,
                "OrganizationCode": "002",
                "SubinventoryCode": "Stores",
                "TransactionQuantity": quantity,
                "TransactionTypeCode": "MATERIAL_ISSUE",
                "TransactionUnitOfMeasure": "Ea",
                "SecondaryTransactionQuantity": 0,
                "WoOperationSequenceNumber": "30",
                "WorkOrderNumber": "WO-002-1054"
            }
        ]
    })
    send_data = requests.post(url=url_scm + "fscmRestApi/resources/11.13.18.05/materialTransactions",
                              headers=headers, data=json_request, verify=False)

    print(f"Response {item}: {send_data.text}")
    ResponseTransaction(send_data.text)


if Connect():
    WOMaterialTransaction("CM60019", 10)
    print("************************************")
else:
    print("Sin conexión a internet.")
