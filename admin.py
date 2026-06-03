from confluent_kafka import Producer
from confluent_kafka.admin import AdminClient, NewTopic


admin = AdminClient({"bootstrap.servers": "localhost:9094"})


# test topic configs
topic_new = NewTopic(
    "my-topic-1",                        # Имя топика
    num_partitions = 1,                  # Количество партиций
    replication_factor = 2,              # Фактор репликации
    config={"min.insync.replicas": "2"}, # Минимум 2 реплики должны подтвердить запись
)

# energy-consumption topic configs
topic_energy_consumpt = NewTopic(
    "energy-consumption",                        # Имя топика
    num_partitions = 1,                  # Количество партиций
    replication_factor = 2,              # Фактор репликации
    config={"min.insync.replicas": "2"}, # Минимум 2 реплики должны подтвердить запись
)

# create new topics
admin.create_topics([topic_new, topic_energy_consumpt])


