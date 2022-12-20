#Proyecto Seguridad de Eventos Catastróficos
#Generic Reed dem inputs (GPIO4)

#Se importan las bibliotecas para los puertos GPIO, MQTT, JSON, SLEEP, SMBUS y MLX60914.
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json

from time import sleep

from smbus2 import SMBus
from mlx90614 import MLX90614
#Se selecciona el bus 1.
bus = SMBus(1)
#Se asigna en una variable el bus y el puerto de donde se conectó el sensor.
sensor = MLX90614(bus, address=0x5A)
#Se configura los pines GPIO 4 y 17 como entradas.
GPIO.setmode(GPIO.BCM)
GPIO.setup (4, GPIO.IN)
GPIO.setup (17, GPIO.IN)
client = mqtt.Client()


try:
    while True:
        #Se realiza el JSON que contiene la información de los sensores y la identificación del hogar.
        datos = { #Modifición
    'casaID': 4,
    'temperatura':sensor.get_obj_temp(),
    'gas': GPIO.input(17),
    'flama':GPIO.input(4),
    'latitud':19.285070179736724,
    'longitud':-99.15826349505048,
    'direccion': 'Calz. de Tlalpan 3016/3058, Coapa, CIJ TLALPAN , Coyoacan, 04980 Ciudad de Mexico',
    
    }
        if GPIO.input(4):
            
            #print(GPIO.input(4),"Temperatura ambiente :", sensor.get_amb_temp())
            #Se conecta al broker utilizado.
            client.connect("3.124.62.105", 1883, 60)
            #Publica en el tema el JSON creado anteriormente.
            client.publish("SeguridadCatastrofes/Departamento/cocina",json.dumps(datos))           
            
        else:
            
            #print(GPIO.input(4),"Temperatura ambiente :", sensor.get_amb_temp())
            #Se conecta al broker utilizado.
            client.connect("3.124.62.105", 1883, 60)
            #Publica en el tema el JSON creado anteriormente.
            client.publish("SeguridadCatastrofes/Departamento/cocina",json.dumps(datos))
                     
        #Espera 1 segundo
        sleep(1)

            
finally:
    
    print("Cleaning up...")
    #GPIO.cleanup()
