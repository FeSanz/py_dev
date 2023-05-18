import time
import requests
import base64
import json
import urllib.request
import random
from urllib3.exceptions import InsecureRequestWarning

url_scm = 'https://fa-etit-saasfademo1.ds-fa.oraclepdemos.com/fscmRestApi/resources/11.13.18.05/'
credentials = "SCM_IMPL:nTg3s?9^"
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def Connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host, timeout=5)  # Si usas Python 2.x coloca: urllib.urlopen()
        return True
    except:
        return False

def GetWOMaintenance(path):
    try:
        auth = base64.b64encode(bytes(credentials, 'utf-8')).decode("ascii")
        url = url_scm + "{0}".format(path)
        headers = {'Authorization': 'Basic %s' % auth, "Content-Type": "application/json"}
        response = requests.get(url=url, headers=headers)
        ResponseWOMaintenance(response.json())
    except:
        pass

def ResponseWOMaintenance(json_response):
    try:
        print(f"WO Pendientes: {json_response['count']}")
        for i in range(json_response['count']):
            print(f"{json_response['items'][i]['WorkOrderNumber']}")
    except:
        print("Ocurrio un error al leer datos JSON")


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
                "TransactionUnitOfMeasure": "Pz",
                "SecondaryTransactionQuantity": 0,
                "WoOperationSequenceNumber": "10",
                "WorkOrderNumber": "WO-002-1079"
            }
        ]
    })
    send_data = requests.post(url=url_scm + "fscmRestApi/resources/11.13.18.05/materialTransactions",
                              headers=headers, data=json_request, verify=False)

    # print(f"Response {item}: {send_data.text}")
    ResponseTransaction(send_data.text)


if Connect():
    GetWOMaintenance("maintenanceWorkOrders?q=WorkOrderStatusCode=ORA_UNRELEASED")
    print("************************************")
    #GetWOMaintenance("workOrders?q=WorkOrderStatusCode=ORA_RELEASED")
else:
    print("Sin conexión a internet.")
