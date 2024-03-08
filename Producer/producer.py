from Producer.utils.produce_messages import produce_messages
from utils.topicos import verificar_topicos
import threading
from dotenv import load_dotenv
import os

load_dotenv()
DISPOSITIVOS = int(os.environ['DISPOSITIVOS'])
bootstrap_server = os.environ['BOOTSTRAP_SERVER'].split(',')

def Producer():
    # Crear hilos y ejecutar la función
    dispositivos = []
    threads = []
    for i in range(DISPOSITIVOS):
        print("CREANDO DISPOSITIVO NUMERO ",i+1," DE ",DISPOSITIVOS,".\n")
        name = input("Ingrese nombre del dispositivo {}: ".format(i+1))
        delay = float(input("ingrese delay del dispositivo {}: ".format(name)))
        size = input("Ingrese tamaño en bytes de los mensajes para el dipositivo {}:".format(name))
        size = eval(size)
        dispositivo = {
            "name":str(name),
            "delay":delay,
            "size":size
        }
        dispositivos.append(dispositivo)
        print("Dispositivo {} creado existosamente!".format(name))
        print("\n")

    for dispositivo in dispositivos:
        thread = threading.Thread(target=produce_messages,args=(dispositivo["name"],bootstrap_server,dispositivo["size"],dispositivo["delay"]))
        thread.start()
        threads.append(thread)
    # Esperar a que todos los hilos terminen
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    #Creamos topicos
    verificar_topicos()
    
    Producer()
    #print(CONTADOR)