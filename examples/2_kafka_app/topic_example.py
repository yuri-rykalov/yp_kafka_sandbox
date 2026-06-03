from confluent_kafka.admin import AdminClient, NewTopic

admin = AdminClient({"bootstrap.servers": "localhost:9094"})

new_topic = NewTopic(
    "my-topic-1",           # Название топика
    num_partitions = 1,     # Кол-во партиций
    replication_factor = 1, # Кол-во реплик
)

try:
    admin.create_topics([new_topic]) # Topics list as argument
    print("Topic created successfully!")
except Exception as e:
    print(e)