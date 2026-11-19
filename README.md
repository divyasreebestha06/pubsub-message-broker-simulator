# 📨 pubsub-message-broker-simulator

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Event Driven](https://img.shields.io/badge/Architecture-Event_Driven-orange?style=for-the-badge)](broker/)

Asynchronous In-Memory Publish-Subscribe Message Broker with Topic Fanout and Consumer Groups.

## Architecture
- **Topic-Based Routing:** Decoupled publisher-subscriber topology.
- **Fanout Distribution:** Broadcast single message to $N$ registered consumer queues.
- **Thread-Safe Locks:** Concurrency guards for parallel publish and subscription events.
