from broker.core import MessageBroker

def run_demo():
    broker = MessageBroker()
    broker.subscribe("orders.created", lambda m: print(f"Audit Log: Order {m.payload} created!"))
    broker.publish("orders.created", {"order_id": 101, "total": 299.99})

if __name__ == "__main__":
    run_demo()
