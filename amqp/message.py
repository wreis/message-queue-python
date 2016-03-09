import pika
import json

class Message:
    def __init__(self, **kwargs):
        """Create a new message.
        """
        self._message = {}
        self.format_message(**kwargs)

    def define_porperties(self, delivery_mode=2):
        """Create basic message properties.

        :param int delivery_mode:
        """
        return pika.BasicProperties(
            content_type='application/json',
            delivery_mode=delivery_mode,)

    def set_queue(self, queue):
        """
        Set message queue
        """
        self._message['routing_key'] = queue

    def format_message(self, **kwargs):
        """Format mesasge content
        """
        properties = self.define_porperties(
            delivery_mode = kwargs.get('delivery_mode'),
        )

        self._message['exchange'] = kwargs.get('exchange', '')
        self._message['properties'] = properties

    def add_content(self, content):
        """Add content to the message

        :param dict content: Content of the message
        """
        self._message['body'] = self.to_json(content)

    def to_json(self, content):
        """Convert content to json.
        """
        return json.JSONEncoder().encode(content)

    def get_content(self):
        """Get the message content.
        """
        return self._message

