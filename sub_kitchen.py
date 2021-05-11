import sys
import paho.mqtt.client
import psycopg2
import json

host='queenie.db.elephantsql.com'
user ='jtahrpyb'
password='icRhXKVz7o_tyHOEJ7gi5TPoadcT8VZK'
dbname='jtahrpyb'
conn = psycopg2.connect(host = host, user = user, password = password, dbname= dbname)


def create_table():
	query = """create table if not exists kitchen (ID SERIAL, device varchar(20) not null, message jsonb, date timestamp with time zone, primary key (ID));"""
	cur = conn.cursor()
	cur.execute(query)
	cur.close()
	conn.commit()


def insert_register(device, message):
    query = """INSERT INTO kitchen (device, message, date)
                VALUES (%s, %s, NOW());"""
    try:
        cur = conn.cursor()
        cur.execute(query, [device, message])
    except Exception as e:
        conn.commit()
        print('Error en el query:', e)
    else:
        conn.commit()
        cur.close()

def on_connect(client, userdata, flags, rc):
	print('connected (%s)' % client._client_id)
	client.subscribe(topic='casa/cocina/#', qos=2)

def on_message(client, userdata, message):
	print('------------------------------')
	print('topic: %s' % message.topic)
	print('payload: %s' % message.payload)
	print('qos: %d' % message.qos)
	insert_register(message.topic.split("/")[2], json.dumps(message.payload.decode("utf-8")))

def main():
	create_table()
	client = paho.mqtt.client.Client(client_id='kitchen-subs', clean_session=False)
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect(host='127.0.0.1', port=1883)
	client.loop_forever()

if __name__ == '__main__':
	main()

sys.exit(0)