#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
pika.ConnectionParameters(host='1401beec.ngrok.io', port='80'))
channel = connection.channel()

channel.queue_declare(queue='hello')

while(True):
	send = raw_input()
	channel.basic_publish(exchange='', routing_key='hello', body=send)
	print " [x] Sent " + send

connection.close()
