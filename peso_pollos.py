import time
import requests
import base64
import json
import random
from urllib3.exceptions import InsecureRequestWarning
from colorama import Fore, Back, Style

device_id = "LEC01"
peso_ideal = 0
peso_actual = 0

dias = 1

dia_aleatorio = random.randint(9, 37)

while True:
    if dias == 1:
        print(f"{Fore.GREEN}Día de desviación: {dia_aleatorio}")
        peso_ideal = 42
        peso_actual = 42
    if dias >= 2 and dias <= 7: # ideal 268
        peso_ideal += 37.6
        peso_actual += 37.6
    if dias >= 8 and dias <= 14: # ideal 618
        peso_ideal += 50
        if dias >= dia_aleatorio:
            peso_actual += round(random.uniform(39.99, 49.99), 2)
        else:
            peso_actual += 50
    if dias >= 15 and dias <= 21: # ideal 1118
        peso_ideal += 71.42
        if dias >= dia_aleatorio:
            peso_actual += round(random.uniform(61.42, 71.41), 2)
        else:
            peso_actual += 71.42
    if dias >= 22 and dias <= 28:  # ideal 1718
        peso_ideal += 85.71
        if dias >= dia_aleatorio:
            peso_actual += round(random.uniform(75.71, 85.70), 2)
        else:
            peso_actual += 85.71
    if dias >= 29 and dias <= 35:  # ideal 2818
        peso_ideal += 157.14
        if dias >= dia_aleatorio:
            peso_actual += round(random.uniform(147.14, 157.13), 2)
        else:
            peso_actual += 157.14
    if dias >= 36 and dias <= 39:  # ideal 3500
        if dias != 39:
            peso_ideal += 170.5
        else:
            peso_ideal = 3500
        if dias >= dia_aleatorio:
            peso_actual += round(random.uniform(160.5, 170.4), 2)
        else:
            peso_actual += 170.5


    json_data = json.dumps({
        #"id": device_id,
        "peso_ideal": round(peso_ideal, 2),
        "peso_actual": round(peso_actual,2)
    })

    if dias >= dia_aleatorio:
        print(f"{Fore.RED}Día {dias} -> {json_data}")
    else:
        print(f"{Fore.RESET}Día {dias} -> {json_data}")

    if dias == 39:
        dia_aleatorio = random.randint(9, 37)
        peso_ideal = 0
        peso_actual = 0
        dias = 0

    dias += 1

    time.sleep(1)