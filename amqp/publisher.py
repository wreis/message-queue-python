# -*- coding: utf-8 -*-
import logging
import pika

LOGGER = logging.getLogger(__name__)


class Publisher:
    def __init__(self, adapter, **kwargs):
        """Create a new publisher with an Adapter instance.

        :param Adapter adapter: Connection Adapter
        :param dictionary kwargs: Parameters to define the Queue
        """
        self.adapter = adapter
        self.define_queue(kwargs)

    def define_queue(**kwargs):
        """Define the queue configuration.

        :param string queue: Queue name to connect
        :param bool passive: Only check to see if the queue exists
        :param bool dureble: Survive reboots of the broker
        :param bool exclusive: Only allow access by the current connection
        :param bool auto_delete: Delete after consumer cancels or disconnects
        :param bool nowait: Do not wait for a Queue.DeclareOk
        :param bool arguments: Custom key/value arguments for the queue
        """
        self.adapter.channel.queue_declare(
            queue       = kwargs.get('queue',       'amqp.python'),
            passive     = kwargs.get('passive',     False),
            durable     = kwargs.get('durable',     True),
            exclusive   = kwargs.get('exclusive',   False),
            auto_delete = kwargs.get('auto_delete', False),
            nowait      = kwargs.get('nowait',      False),
            arguments   = kwargs.get('arguments',   None),
        )

    def publish(self, message):
        """Publish message.
        """
        self.adapter.send(message)

