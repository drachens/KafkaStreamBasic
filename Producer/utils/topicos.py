from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError
#from conectar_kafka import conectar_kafka
from utils.conectar_kafka import conectar_kafka
import os
import time
from dotenv import load_dotenv

load_dotenv()
bootstrap_server = os.environ['BOOTSTRAP_SERVER'].split(',')
topicos_env = os.environ['TOPICOS'].split(',')
num_consumidores = int(os.environ['NUM_CONSUMIDORES'])
#Configuracion del administrador kafka

topic_config = {
    'replication_factor': 3
}

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para crear un topico

def crear_topic(topic, num_partitions, replication_factor):
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_server)
        topic = NewTopic(name=topic, num_partitions=num_partitions, replication_factor=replication_factor)
        admin_client.create_topics([topic])
        print("Topic creado:", topic.name)
        admin_client.close()
    except KafkaError as e:
        print("Error al crear el topic:", e)

#Funcion para evaluar la creacion de topicos
def verificar_topicos():
    topicos = listar_topicos()
    for topico in topicos_env:
        if topico in topicos:
            print("El topico ",topico," ya existe.\n")
            next
        else:
            try:
                crear_topic(topico,num_consumidores,3)
            except:
                print("Error al crear el topico ",topico,".")
    print("Finalizando creación de topicos...")
    time.sleep(5)
    clear_console()
    return

#Listar los topicos
def listar_topicos():
    admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_server)
    topics = admin_client.list_topics()
    #eliminar el topico __consumer_offset de la lista de topicos
    topics = [topic for topic in topics if topic != "__consumer_offsets"] 
    admin_client.close()
    return topics