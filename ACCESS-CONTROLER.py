from machine import Pin, UART
import time
received_data = b''



# Initialize UART
uart0 = UART(0, 9600, parity=None, stop=1, rx=1, tx=0, timeout=500)
uart1 = UART(1, 9600, tx=4, rx=5)
zaczep = Pin(16, Pin.OUT)
led = Pin('LED', Pin.OUT)
re_de_pin = Pin(2,Pin.OUT)

class Device:
    def __init__(self, mac_address=None, info=None, name=None):
        if mac_address:
            self.mac_address = bytearray.fromhex(mac_address.replace(':', ''))
        else:
            self.mac_address = None
        self.info = info
        self.name = name

    def __str__(self):
        mac_address_str = ':'.join('{:02x}'.format(byte) for byte in self.mac_address)
        return f"Device: {self.name}\nMAC Address: {mac_address_str}\ninfo: {self.info}"

mac_address = "a2:3f:c8:7b:9d:05"
zero_mac_address = "00:00:00:00:00:00"

info = "Controlling access to office main door"
name = "Device1"
device1 = Device(mac_address, info, name)
request = ""
#print (device1)


def open_door():
    zaczep.value(1)
    time.sleep(2)
    zaczep.value(0)
    time.sleep(0.3)


def send_data(data, uart):
    if re_de_pin.value() != 1:
        re_de_pin.value(1)
        time.sleep(0.1)
    uart.write(data)


def send_device_info(device, uart):
    if re_de_pin.value() != 1:
        re_de_pin.value(1)
        time.sleep(0.1)
    data = str(device).encode('utf-8')
    uart0.write(data)
    
def listen_for_self_introduction():
    if re_de_pin.value() != 0:
        re_de_pin.value(0)
        time.sleep(0.1)
    if uart0.any():
        request = uart0.read(17)
        if request == mac_address or zero_mac_address:
            for _ in range(10):
                led.toggle()
                time.sleep(0.1)
                led.toggle()
                time.sleep(0.1)
            return True
        else:
            return False
        
def listen_access():
    while True:
        if re_de_pin.value() != 0:
            re_de_pin.value(0)
            time.sleep(0.1)
        if uart0.any():
            req = uart0.read().decode('utf-8')
            print(req)
            if req == "True":
                open_door()
                break
            else:
                led.toggle()
                time.sleep(0.7)
                led.toggle()
                time.sleep(0.7)
                break
        else:
            pass


def rfid_reader(uart):
    while True:
        if re_de_pin.value() != 1:
            re_de_pin.value(1)
            time.sleep(0.1)    
        if uart.any():
            received_data = uart.read(14)
            start_index = received_data.find(b'\x02')
            end_index = received_data.find(b'\x03')

            if start_index != -1 and end_index != -1:
                cardID = received_data[start_index + 1: end_index-2]
                cardID_str = cardID.decode('utf-8')

                return cardID_str
                    
                    
            else:
                print("Start or end delimiter not found. Data:", received_data)
                received_data = b''
                return ""


        
while True:
    if listen_for_self_introduction() is True:
        send_device_info(device1, uart0)
        break
    else:
        pass
time.sleep(1)


while True:
    rfid = rfid_reader(uart1)
    message = mac_address + rfid
    print(message)
    send_data(message,uart0)
    time.sleep(0.1)
    listen_access()
    time.sleep(0.3)
    while True:
        if uart0.any() or uart1.any():
            uart1.read()
            uart0.read()
        else:
            break

