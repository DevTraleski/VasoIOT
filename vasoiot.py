import paho.mqtt.client as mqtt
import time

user = '6c6d5650-e6a4-11e8-810f-075d38a26cc9'
password = '713db477c813147b9b07cc2056b70d787e6aa709'
client_id = '68433c30-e6c6-11e8-810f-075d38a26cc9'
server = 'mqtt.mydevices.com'
port = 1883

publish = 'v1/' + user + '/things/' + client_id + '/data/'
subscribe = 'v1/' + user + '/things/' + client_id + '/cmd/'

def mensagens(client, userdata, msg):
	p = msg.payload.decode().split(',')
	client.publish(publish + '1', p[-1])

client = mqtt.Client(client_id)
client.username_pw_set(user, password)
client.connect(server, port)
client.on_message = mensagens
client.subscribe(subscribe + '1')

client.loop_start()

while(True):
	client.publish(publish + '0', 100)
	time.sleep(5)
	client.publish(publish + '0', 0)
	time.sleep(5)
