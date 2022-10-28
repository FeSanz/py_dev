import usb.core
import usb.util
import time

IDVENDOR = 0x0590
IDPRODUCT = 0x005B

dev = usb.core.find(idVendor = IDVENDOR, idProduct = IDPRODUCT)

if dev is None:
    raise ValueError('Dispositivo no encontrado')
else:
    print('Dispositivo encontrado')


endpoint_in = dev[0][(0, 0)][0]
endpoint_out = dev[0][(0, 0)][1]

while True:
    try:
        # data += dev.read(endpoint_in.bEndpointAddress, endpoint_in.wMaxPacketSize, timeout=20)
        print(dev.read(endpoint_in.bEndpointAddress, endpoint_in.wMaxPacketSize, timeout=20))
        time.sleep(0.01)
    except usb.core.USBError as e:
        print(e.strerror)

def ReadUSBData():
    #data = []
    while True:
        try:
            #data += dev.read(endpoint_in.bEndpointAddress, endpoint_in.wMaxPacketSize, timeout=20)
            print(dev.read(endpoint_in.bEndpointAddress, endpoint_in.wMaxPacketSize, timeout=20))
            time.sleep(0.01)
        except usb.core.USBError as e:
            print(e.strerror)            

dev = usb.core.find(idVendor=USB_VENDOR, idProduct=USB_PRODUCT)

endpoint = dev[0][(0,0)][0]

if dev.is_kernel_driver_active(USB_IF) is True: dev.detach_kernel_driver(USB_IF)

usb.util.claim_interface(dev, USB_IF)

while True: control = None

#try: control = dev.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize, USB_TIMEOUT) print control except: pass

time.sleep(0.01)
