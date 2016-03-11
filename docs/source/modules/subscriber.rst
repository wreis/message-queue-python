Subscriber
==========

Example::

  from message_queue import AMQPAdapter
  from message_queue import Subscriber

  def worker(channel, method, properties, body):
    print body

  adapter = AMQPAdapter(host='0.0.0.0')
  subscriber = Subscriber(adapter)

  subscriber.consume(worker)


.. automodule:: message_queue.subscriber
  :members:
  :undoc-members:
  :inherited-members:
  :show-inheritance:

