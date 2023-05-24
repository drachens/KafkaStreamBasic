from kafka import KafkaConsumer
import threading
import subprocess
from Producer.funciones.globales import *
import random
import json
import sys

def consume_messages(consumer):
    for message in consumer:
        message_dict = json.loads(message.value)
        timestamp = message_dict["timestamp"]
        value = message_dict["value"]
        name = message_dict["name"]
        output = f"Dispositivo {name} enviando: Timestamp: {timestamp}, value: {value}"
        print(output)
# Crear los consumidores en hilos separados
group_id = 'tarea2_consumer'

threads = []
consumers = []
for i in range(num_consumidores):
    topic = random.choice(TOPICOS)
    consumer = KafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        group_id=group_id,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: x.decode('utf-8')
    )
    consumer.subscribe([topic])
    consumers.append(consumer)

for consumer in consumers:
    thread = threading.Thread(target=consume_messages, args=(consumer,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

for consumer in consumers:
    consumer.close()
