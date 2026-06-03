from confluent_kafka import Producer

# Producers configuration
producer_config = {
    "bootstrap.servers": "localhost:9092",
}

# producer creation
producer = Producer(producer_config)

# sending message
producer.produce(
    topic="my-test-topic",
    key="key-1",
    value="message-1"
)

# waiting till all the messages will be sent
producer.flush()