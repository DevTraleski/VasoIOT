import RPi.GPIO as gpio
import paho.mqtt.client as mqtt
import time

gpio.setmode(gpio.BCM)

#Sendor de umidade
gpio.setup(21, gpio.IN, pull_up_down = gpio.PUD_DOWN)
#Sensor de nivel
gpio.setup(20, gpio.IN, pull_up_down = gpio.PUD_DOWN)
#Motor
gpio.setup(4, gpio.OUT)
gpio.output(4, 0)

user = '6c6d5650-e6a4-11e8-810f-075d38a26cc9'
password = '713db477c813147b9b07cc2056b70d787e6aa709'
client_id = '68433c30-e6c6-11e8-810f-075d38a26cc9'
server = 'mqtt.mydevices.com'
port = 1883

publish = 'v1/' + user + '/things/' + client_id + '/data/'
subscribe = 'v1/' + user + '/things/' + client_id + '/cmd/'

def connect(server, port):
	try:
		print("Connecting...")
		client.connect(server, port)
	except:
		print("Could not connect")
		print("Trying again in 2 seconds...")
		time.sleep(2)
		connect(server, port)

client = mqtt.Client(client_id)
client.username_pw_set(user, password)

connect(server, port)
print("Connected!\n")

client.loop_start()

while(True):
	level = gpio.input(20)
	humidity = gpio.input(21)

	if(humidity == 0):
		client.publish(publish + '0', 1)
	elif(humidity == 1):
		client.publish(publish + '0', 0)

	if(level == 0):
		client.publish(publish + '1', 1)
	elif(level == 1):
		client.publish(publish + '1', 0)

	print("Humidity: " + str(humidity))
	print("Level: " + str(level))
	if(humidity == 1):
		#Start a pump cycle
		print("Starting pump cycle")
		gpio.output(4, 1)
		time.sleep(5)
		gpio.output(4, 0)
		print("Done. Resuming...")

	time.sleep(2)
