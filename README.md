# KafkaStreamBasic

## Descripción

Este proyecto es una implementación básica de un clúster de Apache Kafka para la mensajería de datos. Simula múltiples dispositivos IoT que generan mensajes, los cuales son enviados mediante un productor Kafka y consumidos por múltiples consumidores. Utiliza Docker para levantar el clúster y Python para el manejo de productor y consumidor.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Variables de Entorno](#variables-de-entorno)
- [Reinicio de Contenedores](#reinicio-de-contenedores)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Contacto](#contacto)

## Características

- Simulación de dispositivos IoT mediante un productor Kafka.
- Múltiples consumidores concurrentes.
- Configuración dinámica a través de un archivo `.env`.
- Levantamiento del clúster Kafka con Docker Compose.
- Soporte para múltiples tópicos y brokers.

## Instalación

### Requisitos

- Docker
- Python 3
- pip
- Git

### Pasos

1. Clona este repositorio:
   ```bash
   git clone https://github.com/drachens/KafkaStreamBasic.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd KafkaStreamBasic
   ```
3. Instala las dependencias de Python:
   ```bash
   pip install .
   ```
4. Crea un archivo `.env` en la raíz del proyecto con la configuración necesaria (ver [Variables de Entorno](#variables-de-entorno)).
5. Navega a la carpeta `Kafka`:
   ```bash
   cd Kafka
   ```
6. Levanta el entorno de Kafka con Docker:
   ```bash
   docker-compose up -d
   ```
7. Abre una terminal, navega a la carpeta `Consumer` y ejecuta el consumidor:
   ```bash
   cd ../Consumer
   python consumer.py
   ```
8. Abre otra terminal, navega a la carpeta `Producer` y ejecuta el productor:
   ```bash
   cd ../Producer
   python producer.py
   ```

## Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto y define los siguientes valores:

```env
DISPOSITIVOS=4
NUM_CONSUMIDORES=8
MENSAJES_MAXIMOS=10
BOOTSTRAP_SERVER=localhost:9094,localhost:9095,localhost:9096
TOPICOS=sensor_1,sensor_2,sensor_3,sensor_4,sensor_5,sensor_6
```

| Variable           | Descripción                                    | Tipo                          |
|--------------------|------------------------------------------------|-------------------------------|
| `DISPOSITIVOS`     | Cantidad de dispositivos IoT a simular.        | int                           |
| `NUM_CONSUMIDORES` | Cantidad de consumidores a simular.            | int                           |
| `MENSAJES_MAXIMOS` | Mensajes que enviará cada dispositivo.         | int                           |
| `BOOTSTRAP_SERVER` | Dirección(es) del/los broker(s) Kafka.         | Lista de strings (`ip:puerto`) |
| `TOPICOS`          | Tópicos que utilizarán los dispositivos.       | Lista de strings              |

## Reinicio de Contenedores

Si deseas reiniciar el entorno Kafka y eliminar los volúmenes (datos), ejecuta lo siguiente desde la carpeta `Kafka`:

```bash
docker-compose down -v
docker-compose up -d
```

## Tecnologías Utilizadas

- [Apache Kafka](https://kafka.apache.org/)
- [Docker & Docker Compose](https://www.docker.com/)
- [Python 3](https://www.python.org/)
- [Git](https://git-scm.com/)


## Contacto

Para preguntas o sugerencias, puedes contactarme a través de [github.com/drachens](https://github.com/drachens).



