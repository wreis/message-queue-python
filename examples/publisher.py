import sys
sys.path.append('../')

import amqp
import pika
import json

adapter = amqp.Adapter(host='107.23.60.208')
publisher = amqp.Publisher(adapter, queue='pythonlib:test')


body = {
    'id': 1,
    'message': 'Teste',
}

message = amqp.Message(delivery_mode=2,)
message.add_content(body)

publisher.publish(message)

