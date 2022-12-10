#Proyecto Seguridad de Eventos Catastróficos
#Generic Reed dem inputs (GPIO4)

import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json

from time import sleep

from smbus2 import SMBus
from mlx90614 import MLX90614
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)

GPIO.setmode(GPIO.BCM)
GPIO.setup (4, GPIO.IN)
GPIO.setup (17, GPIO.IN)
client = mqtt.Client()


try:
    while True:
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
            
            client.connect("3.124.62.105", 1883, 60)
            client.publish("SeguridadCatastrofes/Departamento/cocina",json.dumps(datos))           
            
        else:
            
            #print(GPIO.input(4),"Temperatura ambiente :", sensor.get_amb_temp())
            client.connect("3.124.62.105", 1883, 60)
            client.publish("SeguridadCatastrofes/Departamento/cocina",json.dumps(datos))
                     
            
        sleep(1)

            
finally:
    
    print("Cleaning up...")
    #GPIO.cleanup()
