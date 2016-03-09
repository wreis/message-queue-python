import pika


class Adapter(object):
    def __init__(self, host='localhost', port=5672, user='guest', password='guest', vhost='/'):
        """Create the connection credentials and parameters.

        :param string host: Server host
        :param int port: Server port
        :param string user: Server server user
        :param string password: Server server password
        :param string vhost: Server virutal host
        """
        self._host = host
        self._credentials = pika.PlainCredentials(user, password)
        self._parameters = pika.ConnectionParameters(host, port, vhost, self._credentials)

        self.connect()

    def __str__(self):
        return '<Adapter host=%r>' % self._host

    def connect(self):
        """Connect usgin BlockingConnection.
        """
        self.connection = pika.BlockingConnection(self._parameters)
        self.channel = self.connection.channel()

    def close(self):
        """Close connection and channel.
        """
        self.channel.close()
        self.connection.close()

        self.connection = None
        self.channel = None

    def send(self, queue, message):
        """Publish the message in the queue

        :param string queue: Queue name
        :param Message message: Message to publish in the channel
        """
        message.set_queue(queue)
        self.channel.basic_publish(**message.get_content())

