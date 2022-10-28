import requests
import time

TOKEN = "BBFF-3CoBoAybxtoLLRS2n9SAf9CgxmsOEA"
DEVICE = "pi_connect"
VARIABLE = "data01"
DELAY = 1

def GetData(device, variable):
    try:
        url = "http://industrial.api.ubidots.com/api/v1.6/devices/{0}/{1}/".format(device, variable)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        ubidots_response = requests.get(url=url, headers=headers)
        return ubidots_response.json()
    except:
        pass


def GetAllData(variableID):
    try:
        #http://industrial.api.ubidots.com/api/v1.6/variables/6233b0d61d84724b137f3c82/values/?token=BBFF-3CoBoAybxtoLLRS2n9SAf9CgxmsOEA
        url = "http://industrial.api.ubidots.com/api/v1.6/variables/{0}/values/".format(variableID)
        headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}
        ubidots_response = requests.get(url=url, headers=headers)
        return ubidots_response.json()
    except:
        pass

if __name__ == "__main__":
    while True:
        #print(GetData(DEVICE, VARIABLE))
        print(GetAllData("6233b0d61d84724b137f3c82")) #variable data01
        time.sleep(DELAY)