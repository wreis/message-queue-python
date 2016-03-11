"""Message Queue Publisher.

"""

class Publisher:
    def __init__(self, adapter):
        """Create a new publisher with an Adapter instance.

        :param BaseAdapter adapter: Connection Adapter

        """
        self.adapter = adapter

    def publish(self, message):
        """Publish a message message.

        :param Message message: Message to publish in the channel

        """
        self.adapter.send(message)

