import json
import message_queue
import pika


def my_worker(channel, method, properties, body):
    try:
        data = json.loads(body)
        print data

    except:
        print 'Error parsing body: %r' % body
        # return False to not acknowledge the message
        return False


if __name__ == '__main__':
    # Instantiate the AMQP adapter with the host configuration
    adapter = message_queue.AMQPAdapter(host='107.23.60.208')

    # Configurate queue
    adapter.configurate_queue(queue='python.publish.test')

    # Instantiate subscriber
    subscriber = message_queue.Subscriber(adapter)
    # Consume message
    subscriber.consume(my_worker)

