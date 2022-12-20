#Sensor de flama
#Se importa el modulo de control de la interfaz de GPIO.
import RPi.GPIO as GPIO
#Se importa la función sleep de la biblioteca time.
from time import sleep
#Se configura el pin 4 como entrada.
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    while True:
        if GPIO.input(4):
            #Se imprime el valor leido del sensor.
            print(GPIO.input(4))
        
        else:
            #Se imprime el valor leido del sensor.
            print(GPIO.input(4))
        
        #Espera 1 segundo.
        sleep(1)
        
finally:
    #Limpia los puertos GPIO.
    print("Cleaning up..")
    GPIO.cleanup()
    
