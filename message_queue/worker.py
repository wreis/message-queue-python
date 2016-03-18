"""Worker interface to handle messages.

"""
import json


class Worker:
    def __init__(self, content, **kwargs):
        """Create a new worker.

        :param dict content: Content of the message
        :param dict kwargs: Extra parameters for the message

        """


    @staticmethod
    def parse_json(content):
        """Convert content to json.

        :param string content: Content to decode in json format
        :returns type: json

        """
        return json.loads(message)

