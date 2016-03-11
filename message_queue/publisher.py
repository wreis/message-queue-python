class Publisher:
    """Message Queue Publisher.

    """
    def __init__(self, adapter):
        """Create a new publisher with an Adapter instance.

        :param message_queue.adapters.BaseAdapter adapter: Connection Adapter

        """
        self.adapter = adapter

    def publish(self, message):
        """Publish a message message.

        :param message_queue.Message message: Message to publish in the channel

        """
        self.adapter.send(message)

