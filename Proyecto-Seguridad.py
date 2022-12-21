#Proyecto Seguridad de Eventos Catastróficos
#Generic Reed dem inputs (GPIO4)


#Se importan las bibliotecas para los puertos GPIO, MQTT, JSON, SLEEP, SMBUS y MLX60914.
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json

from time import sleep

from smbus2 import SMBus
from mlx90614 import MLX90614


bus = SMBus(1)

#Se asigna en una variable el bus y el puerto de donde se conectó el sensor.
sensor = MLX90614(bus, address=0x5A)

#Se configura los pines GPIO 4 y 17 como entradas.
GPIO.setmode(GPIO.BCM)
GPIO.setup (4, GPIO.IN)
GPIO.setup (17, GPIO.IN)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

BUZZER_PIN = 5

GPIO.setup(BUZZER_PIN, GPIO.OUT)

client = mqtt.Client()


try:
    while True:

        #Se realiza el JSON que contiene la información de los sensores y la identificación del hogar.
        datos = { #Modifición
    'casaID': 1,
    'temperatura':sensor.get_obj_temp(),
    'gas': GPIO.input(17),
    'flama':GPIO.input(4),
    'latitud':19.285070179736724,
    'longitud':-99.15826349505048,
    'direccion': 'Renato Leduc, Puente de Piedra, TLALPAN, Coyoacan, 14040 Ciudad de Mexico',
    
    }
        if GPIO.input(17):
            
            #print(GPIO.input(4),"Temperatura ambiente :", sensor.get_amb_temp())
            #SeguridadCatastrofes/Departamento/cocina
            
            #Se conecta al broker utilizado.
            client.connect("18.197.95.2", 1883, 60)

            #Publica en el tema el JSON creado anteriormente.
            client.publish("SeguridadCatastrofes/Departamento/cocina",json.dumps(datos))
            GPIO.output(BUZZER_PIN, GPIO.LOW)
            sleep(1)
            
        else:
            
            #print(GPIO.input(4),"Temperatura ambiente :", sensor.get_amb_temp())
            client.connect("18.197.95.2", 1883, 60)
            client.publish("SeguridadCatastrofes/Departamento/cocina",json.dumps(datos))
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            sleep(1)
                     
            
        sleep(10)

            
finally:
    
    print("Cleaning up...")
    #GPIO.cleanup()
    
bus.close()
