Publisher
=========

Example::

  from message_queue import AMQPAdapter
  from message_queue import Publisher
  from message_queue import Message

  adapter = AMQPAdapter(host='0.0.0.0')
  publisher = Publisher(adapter)

  message = Message({ 'id': 1 })

  publisher.publish(message)


.. automodule:: message_queue.publisher
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:

