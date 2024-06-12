from kafka import KafkaProducer
import json
import time

# Configurar el productor
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Enviar mensajes
for i in range(5):
    message = {'number': i}
    producer.send('test', value=message)
    print(f'Sent: {message}')
    time.sleep(1)

# Asegurarse de que todos los mensajes se han enviado
producer.flush()

# Cerrar el productor
producer.close()
