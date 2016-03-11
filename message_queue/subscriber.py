class Subscriber:
    """Message Queue Subscriber.

    """
    def __init__(self, adapter):
        """Create a new subscriber with an Adapter instance.

        :param message_queue.adapters.BaseAdapter adapter: Connection Adapter

        """
        self.adapter = adapter

    def consume(self, worker):
        """Consume a queued message.

        :param function worker: Worker to execute when consuming the message

        """
        self.adapter.consume(worker)

