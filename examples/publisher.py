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

