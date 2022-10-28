import usb.core
import usb.util
import sys
from random import randint
import RPi.GPIO as GPIO

IDVENDOR = 0x0590
IDPRODUCT = 0x005B

dev = usb.core.find(idVendor=IDVENDOR, idProduct=IDPRODUCT)
if dev is None:
    raise ValueError('Device not found')

LED1_GPIO = 17
LED2_GPIO = 27
SWITCH1_GPIO = 18
SWITCH2_GPIO = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED1_GPIO, GPIO.OUT)
GPIO.setup(LED2_GPIO, GPIO.OUT)
GPIO.setup(SWITCH1_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SWITCH2_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(LED1_GPIO, GPIO.LOW)
GPIO.output(LED2_GPIO, GPIO.LOW)

endpoint_in = dev[0][(0, 0)][0]
endpoint_out = dev[0][(0, 0)][1]


def USBwrite(msg, revlen):
    x = 0
    cnt1 = 0
    cnt2 = 0
    data = []
    while (1):
        try:
            if x == 0:
                endpoint_out.write(msg)
                x = 1

            data += dev.read(endpoint_in.bEndpointAddress, endpoint_in.wMaxPacketSize, timeout=20)
            if len(data) == revlen:
                return data

        except usb.core.USBError as e:

            if e.strerror.find("error sending control message") >= 0:
                cnt1 += 1
                if cnt1 > 2:
                    raise ValueError('Over error sending control message')
                x = 0
                continue

            elif e.strerror.find("Connection timed out") >= 0:
                cnt2 += 1
                if cnt2 > 2:
                    raise ValueError('Over Connection timed out')
                continue

            else:
                raise ValueError(e.strerror)


def PLC_Run_Monitoring():
    write_array = [0xAB, 0x00, 0x11, 0x80, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    write_array.append(randint(1, 0xFF))
    write_array += [0x04, 0x01, 0xFF, 0xFF, 0x02]
    sumcheck = sum(write_array)
    sumHi = ((sumcheck >> 8) & 0xFF)
    sumLo = (sumcheck & 0xFF)
    write_array.append(sumHi)
    write_array.append(sumLo)
    res = USBwrite(write_array, 19)
    if len(res) == 19:
        sum1 = res[len(res) - 2] << 8 | res[len(res) - 1]
        res.pop()
        res.pop()
        sum2 = sum(res)
        if sum1 == sum2:
            revc = [171, 0, 16, 192, 0, 2, 0, 0, 251, 0, 0, 0, 4, 1, 0, 0]
            res.pop(12)
            if res == revc:
                print("PLC is Run Mode")
            else:
                print("PLC Run Mode Error")
        else:
            print("PLC Run Mode Error")
    else:
        print("PLC Run Mode Error")


def PLC_Run_Mode():
    write_array = [0xAB, 0x00, 0x11, 0x80, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    write_array.append(randint(1, 0xFF))
    write_array += [0x04, 0x01, 0xFF, 0xFF, 0x04]
    sumcheck = sum(write_array)
    sumHi = ((sumcheck >> 8) & 0xFF)
    sumLo = (sumcheck & 0xFF)
    write_array.append(sumHi)
    write_array.append(sumLo)
    res = USBwrite(write_array, 19)
    if len(res) == 19:
        sum1 = res[len(res) - 2] << 8 | res[len(res) - 1]
        res.pop()
        res.pop()
        sum2 = sum(res)
        if sum1 == sum2:
            revc = [171, 0, 16, 192, 0, 2, 0, 0, 251, 0, 0, 0, 4, 1, 0, 0]
            res.pop(12)
            if res == revc:
                print("PLC is Run Mode")
            else:
                print("PLC Run Mode Error")
        else:
            print("PLC Run Mode Error")
    else:
        print("PLC Run Mode Error")


def PLC_Program_Mode():
    write_array = [0xAB, 0x00, 0x10, 0x80, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    write_array.append(randint(1, 0xFF))
    write_array += [0x04, 0x02, 0xFF, 0xFF]
    sumcheck = sum(write_array)
    sumHi = ((sumcheck >> 8) & 0xFF)
    sumLo = (sumcheck & 0xFF)
    write_array.append(sumHi)
    write_array.append(sumLo)
    res = USBwrite(write_array, 19)
    if len(res) == 19:
        sum1 = res[len(res) - 2] << 8 | res[len(res) - 1]
        res.pop()
        res.pop()
        sum2 = sum(res)
        if sum1 == sum2:
            revc = [171, 0, 16, 192, 0, 2, 0, 0, 251, 0, 0, 0, 4, 2, 0, 0]
            res.pop(12)
            if res == revc:
                print("PLC is Run Mode")
            else:
                print("PLC Run Mode Error")
        else:
            print("PLC Run Mode Error")
    else:
        print("PLC Run Mode Error")


def D_Write(D_number, D_value):
    write_array = [0xAB, 0x00, 0x16, 0x80, 0x00, 0x2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    rdm = randint(1, 0xFF)
    write_array.append(rdm)
    write_array += [0x01, 0x02, 0x82]
    write_array.append(D_number >> 8);
    write_array.append(D_number & 0xFF);
    write_array += [0x00, 0x00, 0x01]
    write_array.append(D_value >> 8);
    write_array.append(D_value & 0xFF);
    sumcheck = sum(write_array)
    sumHi = ((sumcheck >> 8) & 0xFF)
    sumLo = (sumcheck & 0xFF)
    write_array.append(sumHi)
    write_array.append(sumLo)
    res = USBwrite(write_array, 19)
    if len(res) == 19:
        val1 = res.pop()
        val2 = res.pop()
        sum1 = val2 << 8 | val1
        sum2 = sum(res)
        if sum1 == sum2:
            rdm2 = res.pop(12)
            if rdm == rdm2:
                revc = [171, 0, 16, 192, 0, 2, 0, 0, 251, 0, 0, 0, 1, 2, 0, 0]
                if res == revc:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0


def D_Read(D_number):
    write_array = [0xAB, 0x00, 0x16, 0x80, 0x00, 0x2, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
    rdm = randint(1, 0xFF)
    write_array.append(rdm)
    write_array += [0x01, 0x04, 0x07, 0x00, 0x00, 0x00, 0x82]
    write_array.append(D_number >> 8);
    write_array.append(D_number & 0xFF);
    write_array += [0x00]
    sumcheck = sum(write_array)
    sumHi = ((sumcheck >> 8) & 0xFF)
    sumLo = (sumcheck & 0xFF)
    write_array.append(sumHi)
    write_array.append(sumLo)
    res = USBwrite(write_array, 24)
    if len(res) == 24:
        val1 = res.pop()
        val2 = res.pop()
        sum1 = val2 << 8 | val1
        sum2 = sum(res)
        if sum1 == sum2:
            rdm2 = res.pop(12)
            if rdm == rdm2:
                val1 = res.pop()
                val2 = res.pop()
                value = val2 << 8 | val1
                val1 = res.pop()
                val2 = res.pop()
                revc = [171, 0, 21, 192, 0, 2, 0, 0, 251, 0, 0, 0, 1, 4, 0, 0, 7]
                if res == revc:
                    return (1, value)
                else:
                    return (0, 0)
            else:
                return (0, 0)
        else:
            return (0, 0)
    else:
        return (0, 0)


# PLC_Run_Monitoring()
PLC_Run_Mode()
# PLC_Program_Mode()


while (1):
    # Read Value from D0 CP1l-L10 Omron PLC to Raspberry Pi
    val = D_Read(0)
    if val[0]:

        if (val[1] & 1):
            GPIO.output(LED1_GPIO, GPIO.HIGH)
        else:
            GPIO.output(LED1_GPIO, GPIO.LOW)

        if ((val[1] >> 1) & 1):
            GPIO.output(LED2_GPIO, GPIO.HIGH)
        else:
            GPIO.output(LED2_GPIO, GPIO.LOW)

    else:
        print("Read Error")

    # Write Value from Raspberry Pi to D2 CP1L-L10 Omron PLC
    valw = 0
    if not GPIO.input(SWITCH1_GPIO):
        valw = valw | 1 << 0
    if not GPIO.input(SWITCH2_GPIO):
        valw = valw | 1 << 3

    c = D_Write(2, valw)
    if not c:
        print("Write Error")
