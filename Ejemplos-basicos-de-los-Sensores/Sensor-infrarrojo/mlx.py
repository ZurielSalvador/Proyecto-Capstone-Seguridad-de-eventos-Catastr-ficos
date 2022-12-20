#MLX90614
#es código para python 3
#Se importa la función SMBus de smbus2.
from smbus2 import SMBus
#Se importa la función MLX90614 de la biblioteca mlx90614.
from mlx90614 import MLX90614
#Se selecciona el Bus 1.
bus = SMBus(1)
#Se asigna en una variable el bus y el puerto de donde se conectó el sensor.
sensor = MLX90614(bus, address=0x5A)
#Se imprime la temperatura ambiente que detecta el sensor.
print ("Temperatura ambiente :", sensor.get_amb_temp())
#Se imprime la temperatura del objeto que se encuentra frente al sensor.
print ("Temperatura de Persona u objeto :", sensor.get_obj_temp())
#Se cierra el bus.
bus.close()
