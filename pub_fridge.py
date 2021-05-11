import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
from publicador import fridge_temp, fridge_ice

def temp(client, temp):
	'''
	Función para publicar la temperatura actual de la nevera.
	'''
	payload = {
	  "temperatura-nevera" : str(temp)
	}
	client.publish('casa/cocina/nevera',json.dumps(payload),qos=0)
	print(payload)

def ice(client, ice, payload):
	'''
	Función para publicar la capacidad de hacer hielo actual de la nevera.
	'''
	payload = {
	  "capacidad-generacion-hielo" : str(ice)
	}
	client.publish('casa/cocina/nevera',json.dumps(payload),qos=0)
	print(payload)

def on_connect(client, userdata, flags, rc):
	print('conectado publicador nevera')

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
	mins = 0
	while True:
		'''temp(client, fridge_temp())
		if mins == 0:
			ice(client, fridge_ice())
			mins=5
		else:
			mins=0
		time.sleep(0.5)'''

		payload = {
		  "temperatura-nevera" : str(fridge_temp())
		}
		if mins == 0:
			payload["capacidad-generacion-hielo"] = str(fridge_ice())
			mins=5
		else:
			mins=0
		
		client.publish('casa/cocina/nevera',json.dumps(payload),qos=0)
		print(payload)
		
		time.sleep(0.5)

		

		
if __name__ == '__main__':
	main()
	sys.exit(0)