"""Message Queue Publisher.
"""


class Publisher:
    def __init__(self, adapter, **kwargs):
        """Create a new publisher with an Adapter instance.

        :param Adapter adapter: Connection Adapter
        :param dictionary kwargs: Parameters to define the Queue
        """
        self.adapter = adapter
        self.adapter.configurate_queue(**kwargs)

    def publish(self, message):
        """Publish a message message.

        :param Message message: Message to publish in the channel
        """
        self.adapter.send(message)

