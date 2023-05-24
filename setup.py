import setuptools

setuptools.setup(
    name="KafkaConsumerProducer",
    version="1.0.0",
    author="Italo",
    description="Kafka producer-consumer Tarea 2",
    packages=setuptools.find_packages(),
    install_requires=[
        "kafka"  # Reemplaza X.X.X con la versión específica de la librería de Kafka que necesitas
    ],
    # Otras configuraciones y metadatos del paquete
)
