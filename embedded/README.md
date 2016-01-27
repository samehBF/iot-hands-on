# Embedded

## Data format

The format of data that the raspberry Pi send to MQTT Broker.

```
{
	"sensor_id": 1,
	"label": "humidity",
	"value": 0.6,
	"ts_second": 1450184825
}
```

## Set up environment 

- Update and Upgrade you PI firmware:
```
$ sudo apt-get update
$ sudo apt-get upgrade
```

- Install python environment:
```
$ python -V 
$ sudo apt-get install python-dev python-pip python-setuptools
```

- Install [WiringPi](http://wiringpi.com/)'s python wrapper [WiringPi-Python](https://github.com/WiringPi/WiringPi-Python). 
It is used for reading from / writing to GPIO pins in a similar way to arduino, 
a good alternative to [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO).
```
$ sudo pip install wiringpi2
```

- After the installation, check if the library is well installed. In the python 
interactive shell, import module and check version. `piBoardRev()` should display
value `2`:

```
$ python
>> import wiringpi2 as wiringpi
>> wiringpi.piBoardRev()
```

- Install [Adafruit Python DHT library](https://github.com/adafruit/Adafruit_Python_DHT) 
which will be used to read the value of the temperature & humidity sensor.

- Install [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt/1.1) Lib:
```
$ sudo pip install paho-mqtt
```

- Sensor Installation. You can follow the [pin map for Pi 2 Model](http://www.element14.com/community/docs/DOC-73950/l/raspberry-pi-2-model-b-gpio-40-pin-block-pinout). In The source code we plug 
(Based on GPIO.BCM mode used by WiringPi2). The sensor is calibred for short 
distance detection: it outputs `1` if nothing is detected and `0` if and obstacle 
is detected:
	- VCC to Pin 2
	- GND to Pin 6
	- Input to GPIO23 (Pin 16)
 
> If you are looking for some pin map more interactive, [click here](http://pinout.xyz/)

## Read data from your sensor

// TODO

## Send data to your MQTT broker

// TODO
