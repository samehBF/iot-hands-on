#!/usr/bin/python

import Adafruit_DHT
import paho.mqtt.client as mqtt
import json
import wiringpi2 as wiringpi  

wiringpi.wiringPiSetupGpio()

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
mqttClient_username = "jxhnfzti"
mqttClient_password = "feCowLGfSWA7"

mqttClient.username_pw_set(mqttClient_username, mqttClient_password)
mqttClient.connect(mqtt_broker_adress, port=mqtt_broket_port, keepalive=60, bind_address="")

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).  
# If this happens try again!
if humidity is not None and temperature is not None:
	temp_fmt = '{0:0.1f}'.format(temperature)
	hum_fmt = '{0:0.1f}'.format(humidity)
	print 'Temp=%s*C  Humidity=%s%%' % (temperature, humidity)
	
	data_buffer = json.dumps({"temperature": temp_fmt, "humidity": hum_fmt})
	# publish data to broker
	if mqttClient.publish("rasp_sensor", data_buffer):
		print "data published to broker: " + str(data_buffer)
else:
	print 'Failed to get reading. Try again!'
