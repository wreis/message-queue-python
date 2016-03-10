import sys
sys.path.append('../')

import message_queue
import pika

adapter = message_queue.AMQPAdapter(host='107.23.60.208')
adapter.configurate_queue(queue='python.publish.test')

subscriber = message_queue.Subscriber(adapter)

def my_worker(channel, method, properties, body):
    print body

subscriber.consume(my_worker)

