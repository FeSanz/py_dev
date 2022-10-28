import json
import requests

try:
    with open('NoOK.json', 'r') as json_file_r:

        jsonDeserializer = json.loads(json_file_r)  # load json para archivos y loads json para cadenas
        if jsonDeserializer['ErrorsExistFlag'] == "true":
            print(f"Transaction Error. {jsonDeserializer['MaterialTransactionDetail'][0]['ErrorMessages']}")
        else:
            print("Transaction Success")
            print(f"ID: {jsonDeserializer['MaterialTransactionDetail'][0]['InvTransactionId']}")
            print(f"Date: {jsonDeserializer['MaterialTransactionDetail'][0]['TransactionDate']}")
        json_file_r.close()
except:
    print("Ocurrio un error al leer datos JSON")
    json_file_r.close()
finally:
    json_file_r.close()




'''try:
    r = requests.get(url,timeout=3)
    r.raise_for_status()
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)'''