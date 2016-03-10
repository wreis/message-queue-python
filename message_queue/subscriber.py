"""Message Queue Subscriber.
"""


class Subscriber:
    def __init__(self, adapter):
        """Create a new subscriber with an Adapter instance.

        :param Adapter adapter: Connection Adapter
        """
        self.adapter = adapter

    def consume(self, worker):
        """Consume a queued message.

        :param Consumer consumer: Consumer to execute a Work to consume the message
        """
        self.adapter.consume(worker)

