import paho.mqtt.client as mqtt
import time

user = '6c6d5650-e6a4-11e8-810f-075d38a26cc9'
password = '713db477c813147b9b07cc2056b70d787e6aa709'
client_id = '68433c30-e6c6-11e8-810f-075d38a26cc9'
server = 'mqtt.mydevices.com'
port = 1883

client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)

while(True):
	client.publish('v1/6c6d5650-e6a4-11e8-810f-075d38a26cc9/things/68433c30-e6c6-11e8-810f-075d38a26cc9/data/0', 100)
	time.sleep(5)
	client.publish('v1/6c6d5650-e6a4-11e8-810f-075d38a26cc9/things/68433c30-e6c6-11e8-810f-075d38a26cc9/data/0', 0)
	time.sleep(5)
