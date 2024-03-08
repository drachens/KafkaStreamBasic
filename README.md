# Implementación Kafka

## Descripción

Este proyecto es una implementación de un cluster de Apache Kafka para la mensajería de datos.
## Características

## Instalación
Como requisitos para la ejecución del proyecto se requiere:
1. Docker
2. Python
3. Pip
4. Git

Para instalar y ejecutar este proyecto siga los siguientes pasos:

1. Clona este repositorio: `git clone https://github.com/drachens/T2_sistemasDistribuidos.git`
2. Navega al directorio del proyecto: `cd T2_sistemasDistribuidos`
3. Instala las dependencias: `pip install .`
4. Crea un archivo `.env`
5. Navega a la carpeta Kafka: `cd Kafka`
6. Crea el entorno docker: `docker-compose up -d`
7. Abre una consola y navega hasta Consumer: `cd Consumer`
8. Ejecuta el consumidor: `python consumer.py`
9. Abre otra consola y navega hasta Producer: `cd Producer`
10. Ejecuta el productor: `python producer.py`

### Varibales globales
Agrega la configuración a tu archivo `.env` en la raiz del proyecto:
```
DISPOSITIVOS=4
NUM_CONSUMIDORES=8
MENSAJES_MAXIMOS=10
BOOTSTRAP_SERVER=localhost:9094,localhost:9095,localhost:9096
TOPICOS=sensor_1,sensor_2,sensor_3,sensor_4,sensor_5,senosor_6
```

| Variable | Descripcion | Tipo |
| --- | --- | --- |
| `DISPOSITIVOS` | Cantidad de dispositivos IoT a simular. | int |
| `NUM_CONSUMIDORES` | Cantidad de consumidores a simular. | int |
| `MENSAJES_MAXIMOS` | Cantidad de mensajes por dispositivo a simular. | int |
| `BOOTSTRAP_SERVER` | Direccion(es) del (los) broker(s) Kafka. | array(string) ej: 'ip_address:PORT' |
| `TOPICOS` | Nombre de los topicos a utilizar. | array(string) |


## Reinicio contenedores

Si quieres reiniciar los contenedores y los datos almacenados navega a la carpeta Kafka y escribe:
`docker-compose down -v`
Luego vuelve a levantar el entorno docker:
`docker-compose up -d`


