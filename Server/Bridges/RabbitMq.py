import pika
import json
from termcolor import colored

connection = pika.BlockingConnection(pika.ConnectionParameters('chichiapp.ir'))
channel = connection.channel()
channel.queue_declare(queue='TaskOne')
channel.basic_publish(exchange='',
                      routing_key='TaskOne',
                      body=json.dumps({"TaskId":"includeamin"}))
print(" [x] Sent 'Hello World!'")
