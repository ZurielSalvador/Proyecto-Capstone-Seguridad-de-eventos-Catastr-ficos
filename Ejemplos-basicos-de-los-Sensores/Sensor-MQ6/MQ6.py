#Sensor MQ6
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

try:
    while True:
        if GPIO.input(4):
            print(GPIO.input(4))
        
        else:
            print(GPIO.input(4))
        
        sleep(1)
        
finally:
    print("Cleaning up..")
    GPIO.cleanup()
    
