import json


class Message:
    """Create messages to publish in the queue.
    """

    def __init__(self, content, **kwargs):
        """Create a new message.

        :param dict content: Content of the message
        :param dict kwargs: Extra parameters for the message
        """
        self._message = {}
        self._message['body'] = self.to_json(content)
        self._message['properties'] = kwargs

    def to_json(self, content):
        """Convert content to json.

        :param dict content: Content to encode in json format
        :return string

        """
        return json.JSONEncoder().encode(content)

    def get_content(self):
        """Get the message content.

        :return dict
        """
        return self._message

