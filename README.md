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

### Step 1.1 Install OS for your Pi

- [Set up your Raspberry Pi with Noobs](https://www.raspberrypi.org/help/noobs-setup/)

### Step 1.2 Set up development environment

- Update and Upgrade you PI firmware:
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

- Install python environment:
```
$ sudo apt-get install build-essential python-dev
```

## Step 2: Read data from the sensor

### Step 2.1 Get to know your Raspberry PI GPIOs

Every group possesses a digital temperature and humidity sensor. Before starting 
wiring the jumbers, get to know the Raspberry Pi's [GPIO (General Purpose Input/Output) pins](https://www.raspberrypi.org/documentation/usage/gpio/) 
or with some more interactive [Pinout map](http://pinout.xyz/).

### Step 2.2 Make your electronic schema

Once you are ready, plug the sensor to your Raspberry Pi:

- VCC to Pin 2
- GND to Pin 6
- Input to GPIO23 (Pin 16)

### Step 2.3 Read the values

The sensor we provide is a [DHT11 type](https://www.adafruit.com/product/386) of digital temperature & humidity sensor. Install the [Adafruit Python DHT library](https://github.com/adafruit/Adafruit_Python_DHT) to read the value of the sensor.

```
// TODO code snippet
```

## Step 3: Build the pipeline

This part focus on explaining how we use different cloud services to build the data pipeline.

### 3.1 Publish to MQTT

One of the most popular open source MQTT broker is [Mosquitto](http://mosquitto.org/). The service [CloudMQTT](https://www.cloudmqtt.com/) we choose for this hands-on are managed Mosquitto servers in the cloud. 

Before pushbling data to the MQTT broker, you have to define:
- the topic name
- the data structure

Then with the 2 options of MQTT clients we choose, you can now start to establish the connection between the Pi and the MQTT broker.

#### Mosquitto

[Mosquitto](http://mosquitto.org/documentation/python/) is considered as the most feature complete library.

- Install the library via pip:
```
$ sudo pip install mosquitto
```

```
// TODO code snippet
```

#### Paho

[Paho](https://www.eclipse.org/paho/clients/python/) is a good alternative. Install [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt/1.1) library:
```
$ sudo pip install paho-mqtt
```

```
// TODO code snippet
```

### 3.2 Subscribe to MQTT

To verify the data is well received by the MQTT broker. Create a simple node.js application using [mqtt.js](https://github.com/mqttjs/MQTT.js) to subscribe to the topic that you previously defined and listen to the message:

```
// TODO code snippt
```

## Step 4: Store data

A very important part of IoT system is to collect data for future analysis. So now it's time to store them somewhere. In the example, we choose [MongoDB](https://www.mongodb.com/) to finish the simple data insertion and query:

```
// TODO code snippet
```

## Step 5: Display the data

For the data visualization part, we prepare a simple REST service that allows any type of dashboard to fetch data and display, using the [Express](http://expressjs.com/) framework.

```
// TODO code snippet
```

## Going further

- Data aggregation: aggregate the data collected from the past period to generate more interesting visulization
- Websocket server to push data in realtime
- Deploy on the cloud service

