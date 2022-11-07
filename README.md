# Proyecto-Capstone-Seguridad-de-eventos-Catastroficos
Este esté repositorio se encontrara el proyecto.



### Número de equipo	22


### Integrantes del equipo:


    Victor Zuriel Dominguez Salvador
    Eduardo Cabrera Mendoza
	José Ernesto Calvillo Lizárraga



### Descripción del proyecto	


Nuestro proyecto es un sistema de detección de siniestros que ocurren en departamentos que busca prevenir las muertes en estos eventos catastróficos, el sistema se basa en sensores que miden diferentes parámetros para determinar si el hogar esta incendiado (temperatura, CO2, etc.) y de acuerdo con ello proporcionar rutas de escape de acuerdo con el evento que se esté presentando, así mismo, avisar a los cuerpos de seguridad como son los bomberos, policías, paramédicos dependiendo el caso.    



### Roles de los miembros 


	

    Rol de Victor Zuriel Dominguez Salvador: Prototipo en físico (maqueta)/ Hardware/ Programación. 

    Rol de Eduardo Cabrera Mendoza: Prototipo en físico (maqueta)/ Hardware/Programación.

	Rol de José Ernesto Calvillo Lizárraga: Documentación/Programación.  


--------------------------------------------------------------------------------------------------------------------------------------


## Primer avance del proyecto.



### Implementación.



1. Se elaboró un programa de ejemplo para el sensor de flama- Sensor-ARD-364.



Para poder ver dicho código se encuentra en la carpeta Codigo-Sensores/Sensor-ARD-364


2. Se elaboró un ejemplo para enviar mensaje por Whatsapp mediante a Node-RED.



El archivo JSON se encuentra en la carpeta llamada: Notificación por whatsapp mediante Node-Red



3. Se elaboró un codigo del sensor mpu6050 dónde guarda los valores en la base de datos MySQL, posteriormente se gráfica en grafana, 


Esta información es muy importante debido se obtiene las lecturas de los sensores guardados y con ayuda de grafana podemos adquirir información sobre el estado que se encuentre dicho departamento, por lo tanto como primer avance se identifa como actúan los sensores con base a lo requerido para nuestra primera implementación.


La información obtenida del sensor mpu6050 se gráfica para ver el comportamiento de manera clara y de acuerdo a lo implementando de la base datos podemos tener un historial de información sobre la lectura del sensor.



### Evidencias del Primer Avance



#### Sensor mpu6050 Directo con la Raspberry.


[![Sensor-mpu6050.jpg](https://i.postimg.cc/3rf6kxbL/Sensor-mpu6050.jpg)](https://postimg.cc/c6YTj0WY)



#### Grafana


[![Grafana-mpu6050.jpg](https://i.postimg.cc/Pq6c1f5r/Grafana-mpu6050.jpg)](https://postimg.cc/QBT0337R)



#### Base de datos MySQL-Sensor mpu6050


[![base-de-datos-mysql.jpg](https://i.postimg.cc/902GMZH4/base-de-datos-mysql.jpg)](https://postimg.cc/vgP121BM)


[![base-de-datos-mysql2.jpg](https://i.postimg.cc/GmfGDZ1n/base-de-datos-mysql2.jpg)](https://postimg.cc/hX9XWZj2)



























