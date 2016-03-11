# Message Queue Python

Message Queue python library to publish and subscribe to queues with diferent types of adapters.


## Current supported adapters:
  - [RabbitMQ - AMQP 0.9.1](https://www.rabbitmq.com/tutorials/amqp-concepts.html)


## Install

```
$ pip install message-queue
```


## Examples:

Publish a message to the queue.

```python
import message_queue
import pika

if __name__ == '__main__':
    # Instantiate the AMQP adapter with the host configuration
    adapter = message_queue.AMQPAdapter(host='107.23.60.208')
    # Configurate queue
    adapter.configurate_queue(queue='python.publish.test')

    # Instantiate publisher
    publisher = message_queue.Publisher(adapter)

    # Create a new message
    message = message_queue.Message({
        'id': 12345,
        'message': 'test publish'
    })

    # Publish message
    publisher.publish(message)
```

Subscribe to messages in the queue.

```python
import json

import message_queue
import pika

# Create you worker method
def my_worker(channel, method, properties, body):
    print json.loads(body)

if __name__ == '__main__':
    # Instantiate the AMQP adapter with the host configuration
    adapter = message_queue.AMQPAdapter(host='107.23.60.208')
    # Configurate queue
    adapter.configurate_queue(queue='python.publish.test')

    # Instantiate subscriber
    subscriber = message_queue.Subscriber(adapter)
    # Consume message
    subscriber.consume(my_worker)
```

