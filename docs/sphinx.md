# Using Sphinx to Test Your Drone

We used Sphinx, the official Parrot drone simulation software to test our flights in a virtual environment. This guide will help you set up the drone objects that interact with your environment.

## Installation

Information about installing Sphinx can be found on it's installation page here:
[Sphinx Installation](https://developer.parrot.com/docs/sphinx/installation.html)

## Launching Your Drone
### Initialization
Firmwared is required to start Sphinx. It is installed by default on Linux distros that come with [systemd](https://en.wikipedia.org/wiki/Systemd). Start the service by running:
```
sudo systemctl start firmwared.service
```
You must restart the service every time the computer is booted.

To confirm that this service started, run:
```
fdc ping
```
You should receive a ```PONG``` response.

### Network Configuration
Locate the .drone file (based on the device you are simulating) in ```/opt/parrot-sphinx/usr/share/sphinx/drones```.
It is an xml file used to locate and download drone schematics. You can use it to customize attributes of the drone.

If you are connecting to the drone with your phone or controller through the laptop's wireless access point, the ```<stolen_interface>``` tag must equal the laptop's WAP. Identify the active WAP by using ```iwconfig```. The ```<stolen_interface>``` tag is used to override a WAP, it can be commented out if you do not need to connect to the drone.

**NOTE**: If the laptop's WAP is used, it will not be able to connect to the internet.
