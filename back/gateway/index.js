var mqtt  = require('mqtt');
var mqttClient = mqtt.connect('mqtt://jxhnfzti:feCowLGfSWA7@m20.cloudmqtt.com:12753');
 
mqttClient.on('connect', function () {
  mqttClient.subscribe('rasp_sensor');
});
 
mqttClient.on('message', function (topic, message) {
	console.log("Topic: " + topic);
	console.log("Message: " + message.toString());
});