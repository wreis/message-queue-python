import pika


class Consumer:
    def __init__(self):
        pass

    def acknowledge(self, channel, tag):
        """Acknowledge the message

        :param Channel channel: Channel to acknowledge the message
        :param int tag: Message tag
        """
        channel.basic_ack(delivery_tag=tag)

    def define_worker(self, worker):
        """Define the worker to consume the message

        :param method worker: Worker to consume the message
        """
        self._worker = worker

    def work(self, channel, method, properties, body):
        """Exectue the worker and acknowledge the channel
        """
        message = json.loads(body)

        self._worker(channel, method, properties, json)

        self.acknowledge(channel, method.delivery_tag)

