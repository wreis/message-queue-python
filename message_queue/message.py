import json


class Message:
    def __init__(self, content, **kwargs):
        """Create a new message.
        """
        self._message = {}
        self._message['body'] = self.to_json(content)
        self._message['properties'] = kwargs

    def to_json(self, content):
        """Convert content to json.

        :parm dict content: Content to encode in json format
        """
        return json.JSONEncoder().encode(content)

    def get_content(self):
        """Get the message content.
        """
        return self._message

