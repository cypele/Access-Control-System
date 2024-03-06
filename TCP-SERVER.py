import network
import usocket as socket
from machine import Pin, UART

# Set up Wi-Fi connection
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("WIFI-SSID", "PASSWORD")
led = Pin(16, Pin.OUT)
uart0 = UART(0, 115200, tx=1, rx=3)



# Wait until connected
while not wifi.isconnected():
    pass
print("Connected to WiFi")
print("IP Address:", wifi.ifconfig()[0])

# Define server settings
SERVER_HOST = "0.0.0.0"  # Listen on all available interfaces
SERVER_PORT = 8080

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address and port
server_socket.bind((SERVER_HOST, SERVER_PORT))

# Start listening for incoming connections
server_socket.listen(1)
print("Server listening on {}:{}".format(SERVER_HOST, SERVER_PORT))
led.value(1)
# Accept incoming connections
while True:
    try:
        client_socket, client_address = server_socket.accept()
        print("Connection from:", client_address)

        # Initialize a counter for responses
        response_counter = 0

        # Stay connected with the client
        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                # If no data received, the client has closed the connection
                print("Client disconnected.")
                break

            print("Received data:", data)

            # Check if received data matches the expected data
            if data.strip().lower() == "quit":
                # If the client wants to quit, close the connection
                print("Client requested to quit.")
                break

            # Process received data (you can add your processing logic here)
            response_counter += 1
            response = "Hello from esp! Response number: {}\n".format(response_counter)

            # Send response back to the client
            client_socket.sendall(response.encode("utf-8"))
    except OSError as e:
        print("Error occurred:", e)
        # Close the connection in case of error
        if client_socket:
            client_socket.close()
        break

# Close the server socket
server_socket.close()




