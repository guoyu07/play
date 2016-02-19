#!/usr/bin/env python
import sys
import pika

message = ' '.join(sys.argv[1:]) or 'Hello World!'

# connect to rabbitmq-server
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue='task_queue')

channel.basic_publish(exchange = '',
                        routing_key = 'task_queue',
                        body = message,
                        properties = pika.BasicProperties(delivery_mode = 2, ))

print 'Sent message: %s' % (message, )

conn.close()
