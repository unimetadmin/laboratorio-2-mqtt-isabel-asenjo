import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
from publicador import pot_temp

def temp(client, temp):
	payload = {"temperatura-olla" : str(temp)}
	if temp >= 100:
    	    payload['message'] = "El agua ya hirvio."
	client.publish('casa/cocina/olla',json.dumps(payload),qos=0)
	print(payload)
	time.sleep(1/60)

def on_connect(client, userdata, flags, rc):
	print('conectado publicador olla')

def main():
	client = paho.mqtt.client.Client("Isabel", False)
	client.qos = 0
	client.connect(host='localhost')
	'''meanEntrada = 500
	stdEntrada = 50
	cantTorniquetes = 20
	horaBase= datetime.datetime.now().replace(minute=0, second=0)
	personasPorHora = np.random.normal(meanEntrada, stdEntrada)
	horaBase = horaBase + datetime.timedelta(hours=1)
	while(personasPorHora>0):
		hora = horaBase + datetime.timedelta(minutes=np.random.uniform(0,60))				
		torn = int(np.random.uniform(1, cantTorniquetes))
		payload = {
			"fecha": str(hora),
			"torniquete": str(torn)
		}
		client.publish('casa/cocina/nevera',json.dumps(payload),qos=2)		
		personasPorHora-=1
		print(payload)
		time.sleep(0.5)'''
	while True:
		temp(client, pot_temp())

		
if __name__ == '__main__':
	main()
	sys.exit(0)