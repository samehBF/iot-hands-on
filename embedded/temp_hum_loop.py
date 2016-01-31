#!/usr/bin/python

import Adafruit_DHT
import time
import paho.mqtt.client as mqtt
import json

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.DHT11

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
sensor_pin = 23

# mqtt client event callbacks
def on_connect(mosq, obj, rc):
	print("rc: " + str(rc))

def on_message(mosq, obj, msg):
	print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def on_publish(mosq, obj, mid):
	print("mid: " + str(mid))

def on_subscribe(mosq, obj, mid, granted_qos):
	print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(mosq, obj, level, string):
	print(string)

# mqtt set up
mqtt_broker_adress = "m20.cloudmqtt.com"
mqtt_broket_port = 16301

mqttClient = mqtt.Client()
mqttClient_username = "ksybowaf"
mqttClient_password = "i9npMQNy1Xhd"

mqttClient.username_pw_set(mqttClient_username, mqttClient_password)
mqttClient.connect(mqtt_broker_adress, port=mqtt_broket_port, keepalive=60, bind_address="")

#Loop to read data from sensor every 10 secondes
cpt = 0
while True:
	cpt = cpt +1
	time.sleep(10)


	# Try to grab a sensor reading.  Use the read_retry method which will retry up
	# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
	humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

	# TODO: add Arduino-like loop

	if humidity is not None and temperature is not None:
		print '------------------------'+ str(cpt) +'---------------------------'
		print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
		data_buffer = json.dumps({"temp": temperature, "hum": humidity})
		# publish data to broker
		if mqttClient.publish("sensor", data_buffer):
			print "data published to broker: " + str(data_buffer)
			print '----------------------------------------------------'

	else:
		print 'Failed to get reading. Try again!'

