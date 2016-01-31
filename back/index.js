var mqtt  = require('mqtt');
var mqttClient = mqtt.connect('');
 
mqttClient.on('connect', function () {
	console.log("MQTT connected.")
  mqttClient.subscribe('rasp_sensor');
});
 
mqttClient.on('message', function (topic, message) {
	console.log("Topic: " + topic);
	console.log("Message: " + message.toString());
});