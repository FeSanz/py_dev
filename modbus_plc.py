#import easymodbus.modbusClient
#import time
import time
from pymodbus.client import ModbusTcpClient as ModbusClient

UNIT = 0x1
client = ModbusClient('192.168.100.38', port=502)

# conexion modbus
client.connect()

while True:
    try:
        if client.connected:
            # escribir valores a registro acorde variable
            client.write_register(4, 200)
            # obtener arreglo de datos de la la posición 15
            list_values = client.read_holding_registers(0, 4, unit=UNIT)

            for i in len(list_values):
                print(f"Valor {i + 1}:  {str(list_values[1])}")
        else:
            print("Intentando reconectar...")
            client.connect()
    except Exception as e:
        print(f"Error. {str(e)}")

    time.sleep(1)
else:
    # cierre de conexión modbus
    client.close()
