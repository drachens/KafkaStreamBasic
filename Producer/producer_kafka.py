#Cada dispositivo es un productor. Cada dispositivo publica datos en Kafka.

from kafka.errors import KafkaError
from kafka import KafkaProducer
from utils.topicos import listar_topicos
import time
from datetime import datetime
import random
import secrets
import json
import os
from dotenv import load_dotenv

load_dotenv()
mensajes_maximos = int(os.environ['MENSAJES_MAXIMOS'])
bootstrap_server = os.environ['BOOTSTRAP_SERVER'].split(',')
#contador_mensajes = 0
def produce_messages(name_device, bootstrap_server,size,delay):
    contador_mensajes = 0
    topicos = listar_topicos()
    producer = KafkaProducer(bootstrap_servers=bootstrap_server)
    #tiempo_inicio = time.time()
    while contador_mensajes < mensajes_maximos: 
        topic = random.choice(topicos) 
        value = secrets.token_hex(size)
        now = datetime.now()
        data = {
            "timestamp":str(now) ,
            "value":{
                "data":value
            },
            "name":name_device,
            "topico":topic
        }
        json_data = json.dumps(data)
        try:
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
