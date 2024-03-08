#CANTIDAD DE PRODUCTORES
def get_dispositivos():
    return(4)
_DISPOSITIVOS = 4
#CANTIDAD DE CONSUMIDORES
num_consumidores = 0
_CONS = 1
#Contador de mensajes
mensajes_maximos = 50+1
#PUERTOS LOCALES PARA BROKER1, BROKER2 Y BROKER3
bootstrap_servers = ['localhost:9094','localhost:9095','localhost:9096']
#TOPICOS
_TOPICOS = ["sensor_1","sensor_2","sensor_3","sensor_4","sensor_1"]
__all__ = ['_DISPOSITIVOS','TOPICOS']