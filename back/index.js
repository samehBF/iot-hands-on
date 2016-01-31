var express = require('express');
var socketio = require('socket.io');
var mqtt  = require('mqtt');
var mqttClient = mqtt.connect('mqtt://jxhnfzti:feCowLGfSWA7@m20.cloudmqtt.com:12753');

mqttClient.on('connect', function () {
	console.log("MQTT connected.")
  mqttClient.subscribe('rasp_sensor');
});
 
mqttClient.on('message', function (topic, message) {
	console.log("Topic: " + topic);
	console.log("Message: " + message.toString());
});

// Websocket service
var app = express();
app.set('port', (process.env.PORT || 5000));
var server = app.listen(app.get('port'), function () {
    console.log("Node app is running at localhost:" + app.get('port'))
});

var io = socketio.listen(server);
io.on('connection', function(client) {  
    console.log('Client connected...');
    client.on('join', function(data) {
        console.log(data);
    });

    // on message add timestamp and sensor id to message then index it in ES
    mqttClient.on('message', function (topic, message) {
    	jsonMessage = JSON.parse(message)
        client.emit('mqtt', jsonMessage);
    });
});