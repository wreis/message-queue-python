import sys
sys.path.append('../')

import message_queue
import pika

adapter = message_queue.AMQPAdapter(host='107.23.60.208')
publisher = message_queue.Publisher(adapter, queue='python.publish.test')

message = message_queue.Message({
    'id': 1234,
    'message': 'test publish'
})

publisher.publish(message)

