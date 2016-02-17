#!/usr/bin/env python

import pika

# connect to rabbitmq-server
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange = '',
                        routing_key = 'hello',
                        body = 'hello world!')

print 'Sent Hello World!'

conn.close()
