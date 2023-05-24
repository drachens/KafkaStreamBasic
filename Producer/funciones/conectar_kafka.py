from kafka import KafkaProducer, KafkaConsumer

def conectar_kafka(bootstrap_servers):
    # Establecer conexión con Kafka y devolver el cliente de Kafka
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
    consumer = KafkaConsumer(bootstrap_servers=bootstrap_servers)
    return producer, consumer

# Ejemplo de uso
#bootstrap_servers = 'localhost:9092'  # Dirección y puerto del servicio de Kafka
#producer, consumer = conectar_kafka(bootstrap_servers)

# Aquí puedes utilizar el objeto "producer" y "consumer" para interactuar con Kafka
