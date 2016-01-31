# XKE IoT Hands On

This hands-on aims at setting up a mini IoT system in 2 hours, using Raspberry 
Pi and sensors available.

## Prerequisite

### Materials

Every group disposes following materials:

- 1 Raspberry Pi Model B+ with 1 power adapter
- 1 screen
- 1 keyboard
- 1 mouse
- 1 Ethernet cable
- 1 HDMI cable
- 1 temperature & humidity sensor (TBD)
- 1 micro SD card
- 1 breadboard
- Electronic jumpers
- Plus: Wifi keys (if you guys want to play with the wifi)

### Technologies

In order to succeed this Hands-on, you’ll need:
- a CloudMQTT (https://www.cloudmqtt.com/) account
- an AWS account
- basic knowledge of Node.js
- basic knowledge of Python

## Step 1: Prepare your Raspberry Pi

### Install OS for your Pi

- [Set up your Raspberry Pi with Noobs](https://www.raspberrypi.org/help/noobs-setup/)

### Set up development environment

- Update and Upgrade you PI firmware:
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

- Install python environment:
```
$ sudo apt-get install build-essential python-dev
```

- Install [Adafruit Python DHT library](https://github.com/adafruit/Adafruit_Python_DHT) 
which will be used to read the value of the temperature & humidity sensor.

- Install [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt/1.1) Lib:
```
$ sudo pip install paho-mqtt
```

## Step 2: Read data from the sensor

### Wire the sensor

Every group possesses a digital temperature and humidity sensor. Before starting 
wiring the jumbers, get to know the Raspberry Pi's [GPIO (General Purpose Input/Output) pins](https://www.raspberrypi.org/documentation/usage/gpio/) 
or with some more interactive [Pinout map](http://pinout.xyz/).

Once you are ready, plug the sensor to your Raspberry Pi:

- VCC to Pin 2
- GND to Pin 6
- Input to GPIO23 (Pin 16)

### Read the values



## Step 3: Build the pipeline

This part focus on explaining how we use MQTT and AWS IoT to build 
the data pipeline.

### MQTT

// TODO publish data to MQTT broker

### AWS IoT

// TODO subscribe to the MQTT broker to get the message published by the pi

## Step 4: Display your data

// TODO push data to dashboard
