# EPF: TP IoT

This hands-on aims at setting up a mini IoT system in 3 hours, using Raspberry 
Pi and sensors available.

## Prerequisite

### Materials

Every group disposes following materials:

- 1 Raspberry Pi 2 Model B+ with 1 power adapter
- 1 screen
- 1 keyboard
- 1 mouse
- 1 Ethernet cable
- 1 HDMI cable
- 1 DHT11 temperature & humidity sensor
- 1 micro SD card
- 1 breadboard
- Electronic jumpers
- Plus: Wifi keys (if you guys want to play with the wifi)

### Technologies

In order to succeed this Hands-on, you’ll need:
- a CloudMQTT (https://www.cloudmqtt.com/) account
- a MongoLab (https://mlab.com/home) account
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

- VCC to physical pin 2
- GND to physical pin 6
- Input to GPIO23 (physical pin 16)

### Step 2.3 Read the values

The sensor we provide is a [DHT11 type](https://www.adafruit.com/product/386) of digital temperature & humidity sensor. Install the [Adafruit Python DHT library](https://github.com/adafruit/Adafruit_Python_DHT) to read the value of the sensor.

You can either start coding directly on the raspberry pi or use ssh connection to edit the script from your own computer (configure your Pi to enable ssh connection). Refer to `/embedded/sensor.py` for reference:

```Python
import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT11
sensor_id = 1

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
sensor_pin = 23

# TODO read the sensor data

```

Launch your sensor script by

```
$ sudo python sensor.py
```

## Step 3: Build the pipeline

This part focus on explaining how we use different cloud services to build the data pipeline.

### 3.1 Publish to MQTT

One of the most popular open source MQTT broker is [Mosquitto](http://mosquitto.org/). The service [CloudMQTT](https://www.cloudmqtt.com/) we choose for this hands-on are managed Mosquitto servers in the cloud. 

Before pushbling data to the MQTT broker, you have to define:
- the topic name
- the data structure

#### Paho

As an MQTT client, you can use [Paho](https://www.eclipse.org/paho/clients/python/) which  is a good MQTT client. 

- Install the library:
```
$ sudo pip install paho-mqtt
```
- Initialize the MQTT client and publish data on the define topic:

```Python
import paho.mqtt.client as mqtt
import urlparse

# Init MQTT client
mqttClient = mqtt.Client()
# e.g. mqtt://username:password@m20.cloudmqtt.com:port
mqttConnectionString = ""
url = urlparse.urlparse(mqttConnectionString)
mqttClient.username_pw_set(url.username, url.password)
mqttClient.connect(url.hostname, url.port)

# TODO publish data

```

### 3.2 Subscribe to MQTT

To verify the data is well received by the MQTT broker. Create a simple node.js application using [mqtt.js](https://github.com/mqttjs/MQTT.js) to subscribe to the topic that you previously defined and listen to the message:

```Javascript
var mqtt = require('mqtt');
var mqttClient = mqtt.connect("");
mqttClient.on('connect', function () {
  console.log("MQTT connected.")
  // TODO subscribe to the topic
});
 
mqttClient.on('message', function (topic, message) {
  console.log("Topic: " + topic);
  console.log("Message: " + message.toString());
});

```

## Step 4: Store data

A very important part of IoT system is to collect data for future analysis. So now it's time to store them somewhere. In the example, we choose [MongoDB](https://mlab.com/home) to finish the simple data insertion and query:

```Javascript
var mongoClient = require('mongodb').MongoClient;
mongoClient.connect(mongodbUrl, function(err, db) {
  if(!err) {
    console.log('MongoDB connected');
    // TODO create collection & retrieve the db object
  }
});

mqttClient.on('message', function (topic, message) {
  console.log("Topic: " + topic);
  console.log("Message: " + message.toString());
  // TODO store data to database
});

var insertSensorData = function(db, data, cb) {
	// TODO insert data to db
};
var findLastSensorDataItem = function(db, cb) {
	// TODO fetch the last inserted data item
};
```

## Step 5: Display the data

For the data visualization part, we prepare a simple REST service that allows any type of dashboard to fetch data and display, using the [Express](http://expressjs.com/) framework.

```Javascript
var express = require('express');
var app = express();

// ....

// REST API
app.get('/sensor', function (request, response) {
  response.header('Access-Control-Allow-Origin', '*');
  response.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
  response.header('Access-Control-Allow-Headers', 'Content-Type');
  response.header('Content-Type', 'application/json');
  // TODO fetch data and send as response
});

app.listen(3000, function () {
  console.log('App listening on port 3000!');
});
```

