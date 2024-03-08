from kafka import KafkaConsumer
import threading
import subprocess
from Producer.funciones.globales import *
#import Producer.funciones.globales.get_dipositivos as lolaso
#import ..Producer.funciones.globales
import random
import json
import sys
import os
import time
from dotenv import load_dotenv

load_dotenv()


def consume_messages(consumer,consumer_data):
    for message in consumer:
        message_dict = json.loads(message.value)
        #timestamp = message_dict["timestamp"]
        #value = message_dict["value"]
        name = message_dict["name"]
        consumer_name = consumer_data["name"]
        #output = f"Dispositivo {name} enviando: Timestamp: {timestamp}, value: {value}"
        output = f"Dispositivo {name} enviando: {message_dict} del consumidor:{consumer_name}"
        print(output)
# Crear los consumidores en hilos separados


if __name__ == '__main__':
    group_id = 'tarea2_consumer'
    topicos = os.environ['TOPICOS'].split(',')
    num_consumidores = int(os.environ['NUM_CONSUMIDORES'])
    bootstrap_server = os.environ['BOOTSTRAP_SERVER'].split(',')
    print(bootstrap_server)
    print(type(bootstrap_server))
    threads = []
    consumers = []
    #print(f"dispositivos":{TOPICOS})
    for i in range(num_consumidores):
        try:
            topic = random.choice(topicos)
            consumer = KafkaConsumer(
                bootstrap_servers=bootstrap_server,
                group_id=group_id,
                auto_offset_reset='earliest',
                value_deserializer=lambda x: x.decode('utf-8')
            )
            time.sleep(1)
            consumer.subscribe([topic])
            #ID consumer
            consumer_data = {
                "name": "consumer-"+str(i)
            }
            consumers.append([consumer,consumer_data])
            print(f"suscription:{consumer.subscription()} consumer_data:{consumer_data}")
            print(f"\ni:{i}")
        except KeyError as e:
            print(f"Error {consumer}")
    print("rer")
    for consumer in consumers:
        thread = threading.Thread(target=consume_messages, args=(consumer[0],consumer[1]))
        thread.start()
        threads.append(thread)

        #consumer[0].close()
        consumer_x = consumer[0]
        topics = consumer_x.topics()
        print(f"consumer:{consumer_x}\ntopics:{topics}")
    for thread in threads:
        try:
            thread.join(timeout=1)
        except RuntimeError as e:
            print(f"Error:{e}")
    print("sas")
    #for consumer in consumers:
        
    print("pip")