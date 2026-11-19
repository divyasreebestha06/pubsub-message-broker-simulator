import unittest
from broker.core import MessageBroker
from broker.queue_consumer import WorkerQueueConsumer

class TestMessageBroker(unittest.TestCase):
    def test_topic_subscription_and_delivery(self):
        broker = MessageBroker()
        received = []
        broker.subscribe("user.signup", lambda msg: received.append(msg.payload["user"]))
        broker.publish("user.signup", {"user": "divyasree"})
        self.assertEqual(len(received), 1)
        self.assertEqual(received[0], "divyasree")

    def test_multiple_subscribers_fanout(self):
        broker = MessageBroker()
        consumer1 = WorkerQueueConsumer()
        consumer2 = WorkerQueueConsumer()
        broker.subscribe("telemetry", consumer1.handle_message)
        broker.subscribe("telemetry", consumer2.handle_message)
        broker.publish("telemetry", {"temp": 72.5})
        self.assertEqual(consumer1.poll().payload["temp"], 72.5)
        self.assertEqual(consumer2.poll().payload["temp"], 72.5)

if __name__ == "__main__":
    unittest.main()
