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
4. Navega a la carpeta Kafka: `cd Kafka`
5. Crea el entorno docker: `docker-compose up -d`
6. Abre una consola y navega hasta Consumer: `cd Consumer`
7. Ejecuta el consumidor: `python consumer.py`
8. Abre otra consola y navega hasta Producer: `cd Producer`
9. Ejecuta el productor: `python producer.py`

Si quieres modificar las variables globales para definir el numero de productores, consumidores y topicos navega navega hasta el
archivo globales.py `cd Producer/funciones/globales.py` , abre con un editor de texto el archivo y guarda las nuevas configuraciones.

| Variable | Descripcion | Tipo |
| --- | --- | --- |
| `DISPOSITIVOS` | Cantidad de dispositivos IoT a simular. | int |
| `num_consumidores` | Cantidad de consumidores a simular. | int |
| `mensajes_maximos` | Cantidad de mensajes a simular. | int |
| `bootstrap_server` | Direccion(es) del (los) broker(s) Kafka. | array(string) ej: 'ip_address:PORT' |
| `TOPICOS` | Nombre de los topicos a utilizar. | array(string) |


## Reinicio contenedores

Si quieres reiniciar los contenedores y los datos almacenados navega a la carpeta Kafka y escribe:
`docker-compose down -v`
Luego vuelve a levantar el entorno docker:
`docker-compose up -d`


