import threading
import uuid
from typing import Dict, List, Callable, Any

class Message:
    def __init__(self, topic: str, payload: Any):
        self.id = str(uuid.uuid4())
        self.topic = topic
        self.payload = payload

class MessageBroker:
    def __init__(self):
        self.subscribers: Dict[str, List[Callable[[Message], None]]] = {}
        self.message_history: List[Message] = []
        self.lock = threading.Lock()

    def subscribe(self, topic: str, handler: Callable[[Message], None]):
        with self.lock:
            if topic not in self.subscribers:
                self.subscribers[topic] = []
            self.subscribers[topic].append(handler)

    def publish(self, topic: str, payload: Any) -> Message:
        msg = Message(topic, payload)
        handlers_to_invoke = []
        with self.lock:
            self.message_history.append(msg)
            if topic in self.subscribers:
                handlers_to_invoke = list(self.subscribers[topic])
        for handler in handlers_to_invoke:
            handler(msg)
        return msg

    def get_topic_messages(self, topic: str) -> List[Message]:
        with self.lock:
            return [m for m in self.message_history if m.topic == topic]
