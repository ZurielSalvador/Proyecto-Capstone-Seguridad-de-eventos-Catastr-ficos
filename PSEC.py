#Proyecto Seguridad de Eventos Catastróficos

#EQUIPO:
# Victor Zuriel Dominguez Salvador 
# Eduardo Cabrera Mendoza 
# José Ernesto Calvillo Lizárraga

#versión 2.

#Generic Reed dem inputs (GPIO4)
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json
import time # Biblioteca para funciones de tiempo

from time import sleep

from smbus2 import SMBus
from mlx90614 import MLX90614
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)  #i2c

GPIO.setmode(GPIO.BCM)
GPIO.setup (4, GPIO.IN)
client = mqtt.Client()

#Configuración de pines
GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 23
GPIO_ECHO    = 24


GPIO.setwarnings(False)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIGGER, False)


try:
    while True:
        
        GPIO.output(GPIO_TRIGGER,True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER,False)
        
        # Medir la señal de respuesta del sensor
        start = time.time()
        while GPIO.input(GPIO_ECHO)==0:
            start = time.time()
        while GPIO.input(GPIO_ECHO)==1:
            stop = time.time()
        
        # Calcular el periodo del pulso de respuesta del sensor
        elapsed = stop-start
        
        # Ecuación para calcular la distancia
        distance = (elapsed * 34300)/2
        
        
        
        datos = { #Modifición, aquí se modifcara con los datos necesarios que se se vayan a publicar en MQTT
          'casaID': 4,
          'temperatura':sensor.get_amb_temp(),
          'distancia': distance,
          'flama':GPIO.input(4),
          'latitud':19.285070179736724,
          'longitud':-99.15826349505048,
          'direccion': 'Calz. de Tlalpan 3016/3058, Coapa, CIJ TLALPAN , Coyoacan, 04980 Ciudad de Mexico',
    
    }
        if GPIO.input(4):
            
            #print(GPIO.input(4),"Temperatura ambiente :", sensor.get_amb_temp())
            
            client.connect("52.58.186.91", 1883, 60)                 #Address del Broker
            client.publish("codigoIoT/abc/prueba",json.dumps(datos)) #Tema a publicar, formato json        
            
        else:
            
            #print(GPIO.input(4),"Temperatura ambiente :", sensor.get_amb_temp())
            client.connect("52.58.186.91", 1883, 60)
            client.publish("codigoIoT/abc/prueba",json.dumps(datos))
                     
            
        sleep(1)
        
except KeyboardInterrupt:
    f.close
    
            
finally:
    
    print("Cleaning up...")
    #GPIO.cleanup()
    
bus.close()
