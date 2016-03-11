"""Subscribe to a specific queue
and consume the messages.

"""

class Subscriber:
    def __init__(self, adapter):
        """Create a new subscriber with an Adapter instance.

        :param BaseAdapter adapter: Connection Adapter

        """
        self.adapter = adapter

    def consume(self, worker):
        """Consume a queued message.

        :param function worker: Worker to execute when consuming the message

        """
        self.adapter.consume(worker)

