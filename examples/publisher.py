import message_queue
import pika


if __name__ == '__main__':
    # Instantiate the AMQP adapter with the host configuration
    adapter = message_queue.AMQPAdapter(host='192.168.99.100')

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
    for i in xrange(10000):
        publisher.publish(message)

