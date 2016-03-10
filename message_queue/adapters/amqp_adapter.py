"""AMQP 0.9.1 Adapter to connect to RabbitMQ using pika
"""

import pika
import message_queue
from message_queue import logger
from message_queue.adapters import BaseAdapter

LOGGER = logger.get(__name__)


class AMQPAdapter(BaseAdapter):
    NAME = 'amqp'

    def __init__(self, host='localhost', port=5672, user='guest', password='guest', vhost='/'):
        """Create the connection credentials and parameters then connect.

        :param string host: Server host
        :param int port: Server port
        :param string user: Server server user
        :param string password: Server server password
        :param string vhost: Server virutal host

        """
        self.queue = None
        self._host = host
        self._credentials = pika.PlainCredentials(user, password)
        self._parameters = pika.ConnectionParameters(host, port, vhost, self._credentials)

        self.connect()

    def configurate_queue(self, **kwargs):
        """Configurate the queue.

        :param int prefetch_count: Specifies a prefetch window in terms of whole messages
        :param string queue: Queue name to connect
        :param bool passive: Only check to see if the queue exists
        :param bool dureble: Survive reboots of the broker
        :param bool exclusive: Only allow access by the current connection
        :param bool auto_delete: Delete after consumer cancels or disconnects
        :param bool arguments: Custom key/value arguments for the queue

        """
        if not self.queue:
            self.queue = kwargs.get('queue', '')
            self.basic_ack = kwargs.get('basic_ack', True)
            self.prefetch_count = kwargs.get('prefetch_count', 0)

            self.channel.queue_declare(
                queue       = self.queue,
                passive     = kwargs.get('passive', False),
                durable     = kwargs.get('durable', True),
                exclusive   = kwargs.get('exclusive', False),
                auto_delete = kwargs.get('auto_delete', False),
                arguments   = kwargs.get('arguments'),
            )

            if self.prefetch_count > 0:
                self.channel.basic_qos(prefetch_count=self.prefetch_count)

    def connect(self):
        """Connect usgin BlockingConnection.
        """
        try:
            self.connection = pika.BlockingConnection(self._parameters)
            self.channel = self.connection.channel()

        except:
            self.connect()


    def close(self):
        """Close connection and channel.
        """
        self.channel.close()
        self.connection.close()

        self.queue = self.connection = self.channel = None

    def send(self, message):
        """Publish a message in the queue.

        :param string queue: Queue name
        :param Message message: Message to publish in the channel

        """
        amqp_message = self.format_message(message.get_content())
        self.channel.basic_publish(**amqp_message)

    def format_message(self, message):
        """Format message to AMQP format.

        :param dict message: Message to format
        """
        exchange = message['properties'].get('exchange', '')
        delivery_mode = message['properties'].get('delivery_mode', 2)

        _message = {}
        _message['body'] = message['body']
        _message['routing_key'] = self.queue
        _message['exchange']   = exchange
        _message['properties'] = pika.BasicProperties(
            content_type='application/json',
            delivery_mode=delivery_mode,
        )

        LOGGER.debug('AMQP Message: %r ', _message)

        return _message

    def consume(self, consumer):
        """Consume message from the queue.

        :param Consumer consumer:

        """
        self.channel.basic_consume(consumer.work, self.queue)

        try:
            self.channel.start_consuming()

        except KeyboardInterrupt:
            self.channel.stop_consuming()
            self.close()

