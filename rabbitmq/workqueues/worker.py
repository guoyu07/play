#!/usr/bin/env python

import pika
import time


def callback(ch, method, properties, body):
    print 'received:%s' %(body, )
    time.sleep(5)
    print 'done'
    ch.basic_ack(delivery_tag = method.delivery_tag)

conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()

channel.queue_declare(queue = 'task_queue')

channel.basic_consume(callback, queue = 'task_queue')

print "Ctrl + c to stop..."

channel.start_consuming()



