import pika
import json
from termcolor import colored


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


connection = pika.BlockingConnection(pika.ConnectionParameters('****'))
channel = connection.channel()
channel.queue_declare(queue='TaskOne')

channel.basic_consume(queue='TaskOne', auto_ack=True, on_message_callback=callback)
