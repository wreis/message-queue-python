import message_queue
import pika


if __name__ == '__main__':
    # Instantiate the AMQP adapter with the host configuration
    adapter = message_queue.AMQPAdapter(host='107.23.60.208')

    # Configurate queue
    adapter.configurate_queue(queue='python.publish.test')

    # Instantiate publisher
    publisher = message_queue.Publisher(adapter)

    # Publish message
    for i in xrange(10000):
        message = message_queue.Message({
            'id': i,
            'message': 'test publish'
        })

        publisher.publish(message)

