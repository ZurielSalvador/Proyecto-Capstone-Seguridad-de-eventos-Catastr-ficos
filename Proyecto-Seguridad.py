#Proyecto: Seguridad de Eventos Catastróficos
#Autores:
#Victor Zuriel Dominguez Salvador
#José Ernesto Calvillo Lizárraga
#Eduardo Cabrera Mendoza



#Se importan las bibliotecas GPIO, MQTT, JSON, SLEEP, SMBUS y MLX60914.
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json

from time import sleep

from smbus2 import SMBus
from mlx90614 import MLX90614


bus = SMBus(1)

#Se asigna en una variable bus y el puerto de dónde se conectó el sensor infrarrojo .
sensor = MLX90614(bus, address=0x5A)

#Se configura los pines GPIO 4 y 17 como entradas para el sensor de flama y Gas.
GPIO.setmode(GPIO.BCM)
GPIO.setup (4, GPIO.IN)
GPIO.setup (17, GPIO.IN)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BUZZER_PIN = 5    #Se asigana el pin de salida 5 para el Buzzer.

GPIO.setup(BUZZER_PIN, GPIO.OUT)

client = mqtt.Client()


try:
    while True:

        #Se realiza el JSON que contiene la información de los sensores y la  ubicacioón e identificación del hogar.
        datos = { #Modificación
    'casaID': 1,
    'temperatura':sensor.get_obj_temp(),
    'gas': GPIO.input(17),
    'flama':GPIO.input(4),
    'latitud':19.285070179736724,
    'longitud':-99.15826349505048,
    'direccion': 'Renato Leduc, Puente de Piedra, TLALPAN, Coyoacan, 14040 Ciudad de Mexico',
    
    }
        if GPIO.input(17): 
            
            
            #Se conecta al broker utilizado con ayuda de mqtt.Client.
            #El número 1883 es el puerto.
            #El número 60 es cada cuanto se intenta reconectar.
            client.connect("18.197.95.2", 1883, 60)

            #Se Publica en el tema el JSON creado anteriormente.
            #El tema a publicar es: SeguridadCatastrofes/Departamento/cocina
            client.publish("SeguridadCatastrofes/Departamento/cocina",json.dumps(datos))
            GPIO.output(BUZZER_PIN, GPIO.LOW) #Se apagará el buzzer si ya no detecta Gas.
            sleep(1)
            
        else:
            
            
            client.connect("18.197.95.2", 1883, 60)
            client.publish("SeguridadCatastrofes/Departamento/cocina",json.dumps(datos))
            GPIO.output(BUZZER_PIN, GPIO.HIGH) #Se prenderá el Buzzer al detectar Gas constantemente.
            sleep(1)
                     
            
        sleep(10)

            
finally:
    
    print("Cleaning up...")
    #GPIO.cleanup()
    
bus.close()
