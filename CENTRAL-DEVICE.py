from machine import UART, Pin
import time
import re

broadcast_addr = "00:00:00:00:00:00"
rx_pin = Pin(1, Pin.IN)
tx_pin = Pin(0, Pin.OUT)
re_de_pin = Pin(2, Pin.OUT)
led = Pin('LED', Pin.OUT)

# Initialize UART
uart0 = UART(0,9600, parity=None, stop=1, rx=1, tx=0, timeout=500)
uart1 = UART(1, 115200, rx=5, tx=4)



access_map = {
    "a2:3f:c8:7b:9d:05": {"7B00614E7D"},
    
}


def check_access(mac_address, tag_id):
    tags = access_map.get(mac_address)
    if tags and tag_id in tags:
        return True
    return False


def is_valid_mac_format(data):
    # Check if the length of the string is exactly 17 characters
    if len(data) != 17:
        return False
    
    # Check if ":" is at positions 2, 5, 8, 11, 14 in the string
    positions = [2, 5, 8, 11, 14]
    for pos in positions:
        if data[pos] != ":":
            return False
    
    return True





def parse_received_message(data, field):
    try:
        # Decode the received data
        decoded_data = data.decode('utf-8')
    except UnicodeError:
        # If decoding fails, return None
        return None

    # Split the decoded data into lines
    lines = decoded_data.split('\n')

    # Initialize the variable to store the extracted info
    extracted_info = None

    # Iterate over the lines to extract the desired field
    for line in lines:
        if line.startswith(field):
            extracted_info = line.split(': ')[1].strip()
            break  # Stop searching after finding the field

    return extracted_info

def send_data(data):
    if re_de_pin.value() is not 1:
        re_de_pin.value(1)
        time.sleep(0.3)
    uart0.write(data)


def read_data():
    if re_de_pin.value() is not 0:
        re_de_pin.value(0)
    data = uart0.read()
    return data

def device_info_recv(uart):
    received_data = read_data()
    name = parse_received_message(received_data, "Device: ")
    mac = parse_received_message(received_data, "MAC Address: ")
    info = parse_received_message(received_data, "info: ")
    return name, mac, info
        
def device_info_send(uart0, uart1):
    name, mac, info = device_info_recv(uart0)
    data=name + "/" + mac + "/" + info
    re_de.value(1)
    uart0.write(data)
    led.toggle()
    
def request_self_introduction():
    send_data(broadcast_addr)
    led.toggle()

def listen_for_respond(uart, timeout_sec=5):
    if re_de_pin.value() is not 0:
        re_de_pin.value(0)
    start_time = time.time()  # Get the current time
    while time.time() - start_time < timeout_sec:  # Loop until timeout
        if uart.any():  # Check if there's incoming data
            return True  # Return the received data
        time.sleep(0.1)  # Wait for a short time before checking again
    return False  # Return None if no data received within timeout


def check_access_listen(uart):
    if re_de_pin.value() is not 0:
        re_de_pin.value(0)
        time.sleep(0.1)
    while True:
        if uart.any():  
            check_address_mac = uart.read(17)
            print(check_address_mac)
            check_address_mac = check_address_mac.decode('utf-8')
            if is_valid_mac_format(check_address_mac):
                check_tag = uart.read(10)
                check_tag = check_tag.decode('utf-8')
                if(check_access(check_address_mac, check_tag) == True):
                    send_data("True")
                    print("sent true")
                    break
                else:
                    send_data("False")
                    print("sent false")
                    break 

while True:
    request_self_introduction()
    temp = listen_for_respond(uart0)
    if temp is True:
        info = bytearray()
        info=device_info_recv(uart0)
        if(not all(element is None for element in info)):
            print(info)
            break
        else:
            pass
    else:
        pass

while True:
    check_access_listen(uart0)
    time.sleep(0.1)
    



