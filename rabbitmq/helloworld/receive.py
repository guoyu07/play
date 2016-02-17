#!/usr/bin/env python

import pika

def callback(ch, method, properties, body):
    print 'received:%s' %(body, )

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue = 'hello')

channel.basic_consume(callback, queue = 'hello', no_ack = True)

print "Ctrl + c to stop..."

channel.start_consuming()



