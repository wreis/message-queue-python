import sys
sys.path.append('../')

import message_queue
import pika

adapter = message_queue.AMQPAdapter(host='107.23.60.208')
adapter.configurate_queue(queue='python.publish.test')

publisher = message_queue.Publisher(adapter)

message = message_queue.Message({
    'id': 12345,
    'message': 'test publish'
})

publisher.publish(message)

