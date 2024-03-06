# Access Control System

## Introduction

**Project Description:**
The Access Control System is designed to provide secure and efficient access management to specified areas, such as buildings, rooms, or IT systems. The system addresses the issue of unauthorized access to protected areas, aiming to prevent theft, loss of sensitive data, and security threats.

**Project Objective and Expected Benefits:**
The project's goal is to create an access control system that enables precise access management through user authentication using RFID cards. Expected benefits include:

- Increased security levels through access control to protected areas.
- Optimization of access management through centralization of authentication and authorization processes.
- Facilitation of access monitoring and report generation using a mobile application.

## Requirements Analysis

**Detailed Functional System Requirements:**
1. User registration and permission assignment.
2. Access authorization through RFID.
3. Real-time access management.

**Detailed Non-functional System Requirements:**
1. High system availability.
2. Quick response to authorization requests.
3. User-friendly operation for both users and administrators.

## Project System

**System Architecture:**
- Central Device:
  - Raspberry Pi Pico
  - ESP8266
  - DC/DC Step-Down LM2596S 1 converter
  - MAX485 converter
- Access Controller:
  - Raspberry Pi Pico
  - RDM6300 card reader
  - MAX485 converter
  - DC/DC Step-Down LM2596S 1 converter
  - Electromagnetic lock
  - MOSFET transistor IRLML6246TR
- Mobile Application:
  - Android System
- TCP Server:
  - ESP8266

## Connections and Functionality

**Connection between Central Device and Access Controllers:**
- Data transmission between the central device and access controllers via RS485 bus.
- Outgoing data from Pico transmitted via UART0 interface.
- Data frames include device addresses and corresponding messages.
- Additional ground wire in the RS485 bus.

**Planned Communication between Central Device and ESP:**
- Planned communication between Pico and ESP for mobile application access.

![System Diagram](https://github.com/cypele/Access-Control-System/assets/124002511/f2d192b4-7f20-4fa1-8276-326d647c6095)

## Functionality

**Central Device Functionality:**
- Identifies connected devices.
- Attempts to send data to ESP (currently not functional).
- Listens for access requests and sends appropriate responses.

**Access Controller Functionality:**
- Identifies itself.
- Listens for card placement on the reader and requests access check from the central device.
- Opens the door upon access grant, otherwise signals lack of access.

**Mobile Application Functionality:**
- Provides real-time monitoring of access control devices.
- Connects to the TCP server and should collect data from ESP8266 (currently not functional).

![Mobile App Screenshots](https://github.com/cypele/Access-Control-System/assets/124002511/ba98a711-b073-4b02-bb04-8ab640dca01a)
![Mobile App Screenshots](https://github.com/cypele/Access-Control-System/assets/124002511/66d9b2a7-281d-47ec-8070-950cd9f1626a)

**TCP Server Functionality:**
- Facilitates communication between the access control system and the internet.
- Transmits information to the mobile application.

![TCP Server Diagram](https://github.com/cypele/Access-Control-System/assets/124002511/f18aa20a-be95-4d46-b6ed-de582b7bce3f)

## Testing

During testing, two battery packs were used to simulate power supply from the building power line.

![Testing](https://github.com/cypele/Access-Control-System/assets/124002511/009c4179-ea45-4d2e-938d-515d26c7f754)

## Summary and Conclusions

The project did not include the OSPF protocol as outlined due to the lack of a suitable card reader. Communication issues between ESP8266 and the central device hindered further development. The project can be continued by refining the mobile application, configuring Pico-ESP communication, establishing a process hierarchy, utilizing a server database, and ensuring data encryption.

## Sources

- [MAX485 Datasheet](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX1487-MAX491.pdf)
- [RDM6300 Datasheet](https://elty.pl/upload/download/RFID/RDM630-Spec.pdf)
- [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)

![System Diagram](https://github.com/cypele/Access-Control-System/assets/124002511/4915612b-c439-44f0-af01-b57a397788cc)
![System Diagram](https://github.com/cypele/Access-Control-System/assets/124002511/c3558108-4205-4349-a92d-35e6d7de6548)
