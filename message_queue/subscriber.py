"""Message Queue Subscriber.
"""


class Subscriber:
    def __init__(self, adapter, **kwargs):
        """Create a new subscriber with an Adapter instance.

        :param Adapter adapter: Connection Adapter
        :param dictionary kwargs: Parameters to configure the Queue
        """
        self.adapter = adapter
        self.adapter.configurate_queue(**kwargs)

    def consume(self, consumer):
        """Consume a queued message.

        :param Consumer consumer: Consumer to execute a Work to consume the message
        """
        self.adapter.consume(consumer.work)

