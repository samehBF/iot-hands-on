#!/usr/bin/python

import Adafruit_DHT
import mosquitto
import json, urlparse, time

# Sensor should be set to Adafruit_DHT.DHT11
sensor = Adafruit_DHT.DHT11
sensor_id = 1

# Example using a Raspberry Pi with DHT sensor
# connected to GPIO23.
sensor_pin = 23

# MQTT client setup
mqttc = mosquitto.Mosquitto()
url_str = "mqtt://jxhnfzti:feCowLGfSWA7@m20.cloudmqtt.com:12753"
url = urlparse.urlparse(url_str)
mqttc.username_pw_set(url.username, url.password)
mqttc.connect(url.hostname, url.port)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = mqttc.loop()
    # Try to grab a sensor reading. Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, sensor_pin)

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).  
    # If this happens try again!
    if humidity is not None and temperature is not None:
	temp_fmt = round(temperature, 1)
	hum_fmt = round(humidity, 1)
	print 'Temp=%s*C  Humidity=%s%%' % (temp_fmt, hum_fmt)		
	# publish data to broker
	data = json.dumps({"sensor_id": sensor_id, "temperature": temp_fmt, "humidity": hum_fmt})
	if mqttc.publish("rasp_sensor", data):
		print "Data published to broker: " + str(data)
	else:
		print "Failed to publish data to broker"
    else:
	print 'Failed to get reading. Try again!'
    time.sleep(30)

print("rc: " + str(rc))


