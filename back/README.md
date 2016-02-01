# Back 

The backend service will be in charge of following tasks:

- communicating with MQTT service to collect data
- persisting collected data in datastore
- exposing a REST API for data fetching
- exposing a Websocket to deliver data in real-time

## Tech stack

- Node.js
	- [Express](http://expressjs.com/)
	- [Socket.io](http://socket.io/)
- MongoDB
- MQTT Client to read data from broker