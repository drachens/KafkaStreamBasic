#Cada dispositivo es un productor. Cada dispositivo publica datos en Kafka.

from kafka.errors import KafkaError
from kafka import KafkaProducer, TopicPartition
from funciones.globales import *
from funciones.create_topic import crear_topicos
from funciones.create_topic import listar_topicos
import time
import random
import secrets
import json
contador_mensajes = 0
def produce_messages(name_device, bootstrap_servers,size,delay):
    global contador_mensajes
    topicos = listar_topicos()
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    tiempo_inicio = time.time()
    while contador_mensajes <= mensajes_maximos: 
        topic = random.choice(topicos) 
        value = secrets.token_hex(size)
        data = {
            "timestamp":time.time(),
            "value":{
                "data":value
            },
            "name":name_device
        }
        json_data = json.dumps(data)
        try:
            # Asignar partición basada en el valor del contador
            #partition = random.randint(0,num_consumidores)
            #topic_partition = TopicPartition(topic=topic,partition=partition)
            # Crear un objeto TopicPartition con el topic y la partición
            # Enviar el mensaje a la partición especificada
            producer.send(topic, json_data.encode('utf-8'))
            contador_mensajes += 1
            print("Se ha producido correctamente la data:",data," en el topico: ",topic)
            print(contador_mensajes)
        except KafkaError as e:
            print("Error al producir data:",e)
        time.sleep(delay)
    producer.flush()
    producer.close()
