AKADEMIA GÓRNICZO-HUTNICZA
Access Control System
Adam Cypliński


Introduction:
Project Description: The Access Control System aims to provide secure and efficient management of access to specified areas, such as buildings, rooms, or IT systems. The problem to be solved by this system is the limitation of unauthorized access to protected areas, preventing potential theft, loss of sensitive data, and security threats.
Project Objective and Expected Benefits: The project aims to create an access control system that enables precise access management through user authentication using RFID cards. Expected benefits include:
•	Increased security levels through access control to protected areas.
•	Optimization of access management through centralization of authentication and authorization processes.
•	Facilitation of access monitoring and report generation using a mobile application.
Requirements Analysis:
Detailed Functional and Non-functional System Requirements:
•	Functional:
1.	User registration and permission assignment.
2.	Access authorization through RFID.
3.	Real-time access management.
•	Non-functional:
1.	High system availability.
2.	Quick response to authorization requests.
3.	User-friendly operation for both users and administrators.

Project System:
System Architecture: The system comprises an RS485 bus, access controller, mobile application, tcp server and central device, which include:
•	Central Device:
•	Raspberry Pi Pico as the main unit handling all events.
•	ESP8266 providing mobile application access to system data via TCP/IP server.
•	DC/DC Step-Down LM2596S 1 converter for powering Raspberry Pi Pico and ESP8266.
•	MAX485 converter enabling communication between the main unit and access controllers via RS485 bus.
•	Access Controller:
•	Raspberry Pi Pico as the main unit handling all events.
•	RDM6300 card reader.
•	MAX485 converter enabling communication between the access controller and the central device via RS485 bus.
•	DC/DC Step-Down LM2596S 1 converter for powering Raspberry Pi Pico, MAX485 converter, and RFID card reader.
•	12V electromagnetic lock.
•	10k resistor.
•	Rectifier diode between power supply and lock load.
•	N MOSFET transistor IRLML6246TR for controlling the lock with a 3.3V voltage.

•	Mobile Application:
•	Android System

•	TCP Server:
•	ESP8266
Connections and Functionality:
Connection between Central Device and Access Controllers:
•	Data is transmitted between the central device (Raspberry Pi Pico) and access controllers.
•	Outgoing data from Pico is transmitted via UART0 interface, where GPIO 0 is configured as TX, GPIO 1 as RX, and GPIO 2 as RE/DE, both in the access controller and central device.
•	Pico's TX outputs are connected to the DI input of the MAX485 converter, while RX inputs are connected to RO.
•	The RE and DE pins on the converter are tied together and are high during transmission and low during reception, controlled by GPIO 2 on Pico.
•	The data frame for the central device consists of the device's address to which the message is sent (in UTF-8 format) and the corresponding message.
•	For the access controller, the data frame includes the address of the device from which the data was sent and the message (in UTF-8 format).
•	The RS485 bus has an additional wire for carrying ground between devices (depending on requirements, this can be eliminated by using terminators).
•	The RDM6300 reader is connected to power and its TX pin is connected to GPIO05 of the access controller (UART1, RX pin) and shares a common ground with Pico.

Planned Communication between Central Device and ESP:
•	Planned communication between Pico and ESP for mobile application access was not realized.
![image](https://github.com/cypele/Access-Control-System/assets/124002511/f2d192b4-7f20-4fa1-8276-326d647c6095)













Central Device Functionality:
•	The central device sends a message requesting identification of connected devices.
•	It then attempts to send this data to ESP (this functionality is not working).
•	Listens for requests to check access and sends back an appropriate response message containing the device address and "True" value if access is granted, or "False" otherwise.
Access Controller Functionality:
•	The access controller identifies itself.
•	Listens for whether a card has been placed on the reader. If so, it sends a request to check access to the central device.
•	If a "True" response is received, it opens the door using GPIO16 pin, whose signal controls the MOSFET transistor gate, otherwise, it signals lack of access by flashing the LED.




Mobile Application Functionality:
•	The application provides real-time monitoring of access control devices.
•	Upon opening the application, users can choose the device they are interested in. Then the application connects to the TCP server and should collect data from ESP8266 and display relevant device information. However, this functionality is not working due to communication issues between ESP8266 and Pico.


![image](https://github.com/cypele/Access-Control-System/assets/124002511/ba98a711-b073-4b02-bb04-8ab640dca01a)
![image](https://github.com/cypele/Access-Control-System/assets/124002511/66d9b2a7-281d-47ec-8070-950cd9f1626a)



















TCP Server Functionality:
•	The server aims to provide communication between the access control system and the internet, as well as transmitting information to the mobile application.

![image](https://github.com/cypele/Access-Control-System/assets/124002511/f18aa20a-be95-4d46-b6ed-de582b7bce3f)


Testing: During testing, I used two battery packs to simulate power supply from the building power line.

 ![image](https://github.com/cypele/Access-Control-System/assets/124002511/009c4179-ea45-4d2e-938d-515d26c7f754)





Summary and Conclusions: The final project did not include the OSPF protocol as outlined due to the lack of a suitable card reader. Unfortunately I was not able to establish communication between ESP8266 and central device. 
This problem resulted in no further development of the application.
The project can be continued by further developing the mobile application and properly configuring the Pico-ESP communication, establishing a process hierarchy, utilizing a database located on the server, and ensuring data encryption.


Sources:
MAX485 Datasheet https://www.analog.com/media/en/technical-documentation/data-sheets/MAX1487-MAX491.pdf

RDM6300 Datasheet https://elty.pl/upload/download/RFID/RDM630-Spec.pdf

Raspberry Pi Pico - https://www.raspberrypi.com/products/raspberry-pi-pico/
![image](https://github.com/cypele/Access-Control-System/assets/124002511/4915612b-c439-44f0-af01-b57a397788cc)
![image](https://github.com/cypele/Access-Control-System/assets/124002511/c3558108-4205-4349-a92d-35e6d7de6548)

 

