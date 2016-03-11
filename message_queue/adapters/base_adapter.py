"""Message Queue Base Adapter Interface.

"""
from abc import ABCMeta, abstractmethod


class BaseAdapter:
    __metaclass__ = ABCMeta
    __name__ = 'adapter'

    @abstractmethod
    def configurate_queue(self):
        """Define the queue configuration.

        """
        pass

    @abstractmethod
    def connect(self):
        """Connect to queue.

        """
        pass

    @abstractmethod
    def close(self):
        """Close connection.

        """
        pass

    @abstractmethod
    def send(self):
        """Publish a message to the queue.

        """
        pass

    @abstractmethod
    def format_message(self):
        """Format message to send to the queue.

        """
        pass

    @abstractmethod
    def consume(self):
        """Consume message from the queue.

        """
        pass

    @abstractmethod
    def consume_callback(self):
        """Callback method to execute in the consume.

        """
        pass

