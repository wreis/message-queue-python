"""AMQP connection adapter.
"""

import logging
import pika

LOGGER = logging.getLogger(__name__)


class Adapter(object):
    def __init__(self, host='localhost', port=5672, user='guest', password='guest', vhost='/'):
        """
        Create the connection credentials and parameters.

        :param string host: Server host
        :param integer port: Server port
        :param string user: Server server user
        :param string password: Server server password
        :param string vhost: Server virutal host
        """
        self._setCredentials(user, password)
        self._connection_parameters = pika.ConnectionParameters(host, port, vhost, self._credentials)

    def _setCredentials(self, user, password):
        """
        Set connection credentials.

        :param string user: Credentials user
        :param string password: Credentials password
        """
        self._connection_credentials = pika.PlainCredentials(user, password)

    def connect(self):
        """
        Connect usgin pika BlockingConnection.
        """
        self.connection = BlockingConnection(self.connection_parameters)
        self.createChannel()

    def createChannel(self):
        """
        Create a connection channel.
        """
        self.channel = self.connection.channel()
        self.channel.queue_declare()

    def config_queue(**kwargs):
        """
        Configurate the queue

        :param string queue: Queue name to connect
        :param bool passive: Only check to see if the queue exists
        :param bool dureble: Survive reboots of the broker
        :param bool exclusive: Only allow access by the current connection
        :param bool auto_delete: Delete after consumer cancels or disconnects
        :param bool nowait: Do not wait for a Queue.DeclareOk
        :param bool arguments: Custom key/value arguments for the queue
        """
        self.connect()
        self.channel.queue_declare(
            queue       = kwargs.get('queue', 'amqp-python'),
            passive     = kwargs.get('passive', False),
            durable     = kwargs.get('durable', True),
            exclusive   = kwargs.get('exclusive', False),
            auto_delete = kwargs.get('auto_delete', False),
            nowait      = kwargs.get('nowait', False),
            arguments   = kwargs.get(arguments, None),
        )

    def close(self):
        """
        Close channel and connection
        """
        self.channel.close()
        self.connection.close()

        self.connection = None
        self.channel = None

