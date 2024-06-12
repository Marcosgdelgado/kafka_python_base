from kafka import KafkaConsumer
import json

# Configurar el consumidor
consumer = KafkaConsumer(
    'test',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

# Leer mensajes
for message in consumer:
    print(f'Received: {message.value}')
