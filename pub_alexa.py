import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
from publicador import ccs_temp

def city_temp(client, temp):
	payload = {"temperatura-ccs" : str(temp)}
	client.publish('casa/sala/alexa_echo',json.dumps(payload),qos=0)
	print(payload)
	time.sleep(1)

def on_connect(client, userdata, flags, rc):
	print('conectado publicador alexa')

def main():
	client = paho.mqtt.client.Client("Isabel", False)
	client.qos = 0
	client.connect(host='localhost')
	while True:
		city_temp(client, ccs_temp())

		
if __name__ == '__main__':
	main()
	sys.exit(0)