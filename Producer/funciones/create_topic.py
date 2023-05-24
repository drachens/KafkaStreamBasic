from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError
#from conectar_kafka import conectar_kafka
from funciones.conectar_kafka import conectar_kafka
from .globales import *
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Configuracion del administrador kafka
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
topic_config = {
    'replication_factor': 3
}
# Función para crear un topico
def crear_topic(topic, num_partitions, replication_factor):
    try:
        topic = NewTopic(name=topic, num_partitions=num_partitions, replication_factor=replication_factor)
        admin_client.create_topics([topic])
        print("Topic creado:", topic.name)
    except KafkaError as e:
        print("Error al crear el topic:", e)

#Funcion para evaluar la creacion de topicos
def crear_topicos():
    topicos = TOPICOS
    topics = listar_topicos()
    for topic in topicos:
        if topic in topics:
            print("El topico ",topic," ya existe.\n")
            next
        else:
            try:
                crear_topic(topic,num_consumidores,3)
            except:
                print("Error al crear el topico ",topic,".")
    print("Finalizando creación de topicos...")
    time.sleep(5)
    clear_console()
    return

#Listar los topicos
def listar_topicos():
    topics = admin_client.list_topics()
    #eliminar el topico __consumer_offset de la lista de topicos
    topics = [topic for topic in topics if topic != "__consumer_offsets"] 
    return topics