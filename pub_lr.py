import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
from publicador import living_room_capacity

def people(client, people):
	payload = {"contador-personas" : str(people)}
	if people > 5:
    	    payload['warning'] = "Alerta! Hay mas de 5 personas en la sala."
	client.publish('casa/sala/contador_personas',json.dumps(payload),qos=0)
	print(payload)
	time.sleep(0.1)

def on_connect(client, userdata, flags, rc):
	print('conectado publicador contador sala')

def main():
	client = paho.mqtt.client.Client("Isabel", False)
	client.qos = 0
	client.connect(host='localhost')
	while True:
		people(client, living_room_capacity())

		
if __name__ == '__main__':
	main()
	sys.exit(0)