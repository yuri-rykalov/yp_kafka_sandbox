from confluent_kafka import Consumer

# consumer configurations
consumer_config = {
    "bootstrap.servers":"localhost:9092", # Адрес брокера Kafka
    "group.id":"my-group",                # Уникальный идентификатор группы
    "auto.offset.reset": "earliest",      # Начало чтения с самого начала
    "enable.auto.commit": True,           # Автоматический коммит смещений
    "session.timeout.ms": 6_000           # Время ожидания активности от консьюмера - тут 6 сек
}

# consumer cretaion
consumer = Consumer(consumer_config)

# subscribe consumer to a topic
consumer.subscribe(["some-topic"])

# reading messages
try:
    while True:
        # get message
        msg = consumer.poll(0.1) # in ms

        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue

        key = msg.key().decode("utf-8")
        value = msg.value().decode("utf-8")
        print(f"message received: {key=}, {value=}, offset={msg.offset()}")
finally:
    # closing consumer
    consumer.close()
