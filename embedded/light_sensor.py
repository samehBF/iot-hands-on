#!/usr/bin/python

import wiringpi2 as wiringpi  

sensor_value = 0
sensor_pin = 4

# setup GPIO
wiringpi.wiringPiSetupGpio()

# set GPIO 04 as input
wiringpi.pinMode(sensor_pin, 0)

# continue the network loop, exit when an error occurs
while True:
    try:
        # Read the sound level
        sensor_value = wiringpi.analogRead(sensor_pin)
        print sensor_value
        time.sleep(.5)
    except IOError:
        print "Error"