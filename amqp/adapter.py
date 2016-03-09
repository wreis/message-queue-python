# -*- coding: utf-8 -*-
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
        self._credentials = pika.PlainCredentials(user, password)
        self._parameters = pika.ConnectionParameters(host, port, vhost, self._credentials)

        self.connect()

    def connect(self):
        """Connect usgin BlockingConnection.
        """
        self.connection = BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()

    def close(self):
        """Close connection and channel.
        """
        self.channel.close()
        self.connection.close()

        self.connection = None
        self.channel = None

    def send(self, message):
        """Publish the message in the queue
        """
        self.channel.basic_publish(message)

