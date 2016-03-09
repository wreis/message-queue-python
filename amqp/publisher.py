import pika


class Publisher:
    def __init__(self, adapter, **kwargs):
        """Create a new publisher with an Adapter instance.

        :param Adapter adapter: Connection Adapter
        :param dictionary kwargs: Parameters to define the Queue
        """
        self.adapter = adapter
        self.define_queue(**kwargs)

    def __str__(self):
        return '<Publisher>'

    def define_queue(self, **kwargs):
        """Define the queue configuration.

        :param string queue: Queue name to connect
        :param bool passive: Only check to see if the queue exists
        :param bool dureble: Survive reboots of the broker
        :param bool exclusive: Only allow access by the current connection
        :param bool auto_delete: Delete after consumer cancels or disconnects
        :param bool arguments: Custom key/value arguments for the queue
        """
        self.queue = kwargs.get('queue', 'amqp.python')

        self.adapter.channel.queue_declare(
            queue       = self.queue,
            passive     = kwargs.get('passive', False),
            durable     = kwargs.get('durable', True),
            exclusive   = kwargs.get('exclusive', False),
            auto_delete = kwargs.get('auto_delete', False),
            arguments   = kwargs.get('arguments'),
        )

    def publish(self, message):
        """Publish message.

        :param Message message: Message to publish in the channel
        """
        self.adapter.send(self.queue, message)

