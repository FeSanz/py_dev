import socket

# IP y puerto de comunicación
HOST = '192.168.0.104'
PORT = 33330
#Tamaño del búfer de recepción
BUFFER_SIZE = 1024
# Crear socket
m_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Vincular el socket al host y al puerto
m_socket.bind((HOST, PORT))
while True:
    # Recibir BUFFER_SIZE bytes de datos(1.datos, 2.direccion)
    data = m_socket.recvfrom(BUFFER_SIZE)
    if data:
        #Imprime datos recibido
        print('Datos del cliente: ' , data)
        #print(data[1])
        # convertir a mayusculas para enviar a cliente
        m_socket.sendto(data[0], data[1])
# Cerrar conexión
s.close()