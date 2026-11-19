from queue import Queue
from broker.core import Message

class WorkerQueueConsumer:
    def __init__(self):
        self.queue = Queue()

    def handle_message(self, message: Message):
        self.queue.put(message)

    def poll(self, block=False, timeout=None):
        return self.queue.get(block=block, timeout=timeout)
