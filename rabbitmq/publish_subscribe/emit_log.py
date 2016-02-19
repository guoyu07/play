#!/usr/bin/env python

import pika
import sys

conn = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = conn.channel()

channel.exchange_
