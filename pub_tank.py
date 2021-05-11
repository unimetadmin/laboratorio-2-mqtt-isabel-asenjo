import ssl
import sys
import json
import random
import time
import paho.mqtt.client
import paho.mqtt.publish
import numpy as np
import datetime
from publicador import tank_empty, tank_fill

def water(client, water):
    payload = {"agua-en-tanque" : str(water)}
    if water == 0:
        payload['message'] = "No hay agua en el tanque."
    elif water <= 50:
        payload['message'] = "El tanque tiene la mitad o menos de agua."
    return water, payload

def on_connect(client, userdata, flags, rc):
	print('conectado publicador tanque')

def main():
    client = paho.mqtt.client.Client("Isabel", False)
    client.qos = 0
    client.connect(host='localhost')
    mins = 30
    wtr = 100
    while True:
        wtr,payload = water(client, tank_empty(wtr))
        if mins == 30:
            wtr,payload = water(client, tank_fill(wtr))
            mins=0
        mins+=10
	    
        client.publish('casa/banho/tanque',json.dumps(payload),qos=0)
        print(payload)
        time.sleep(1)

		
if __name__ == '__main__':
	main()
	sys.exit(0)