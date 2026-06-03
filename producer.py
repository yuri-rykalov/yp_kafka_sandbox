from confluent_kafka import Producer
from utils.energy_meters import EnergyConsumption


# Create Kafka Producer
producer_config = {
    "bootstrap.servers": "localhost:9094",
    "acks": "all",  # Параметр для синхронной репликации
    "retries": 3,   # Количество попыток при сбоях
}

producer = Producer(producer_config)

# produce data in energy-consumption topic
ec = EnergyConsumption()

for i in range(10):
    producer.produce(
        "energy-consumption",
        key = "ec",
        value = ec.gen_consumption_payload()
    )
producer.flush()