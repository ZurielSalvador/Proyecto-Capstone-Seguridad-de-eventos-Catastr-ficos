# Proyecto-Capstone-Seguridad-de-eventos-Catastroficos

Este esté repositorio se encontrara el proyecto.


### Número de equipo	22


### Integrantes del equipo:

Eduardo Cabrera Mendoza
José Ernesto Calvillo Lizárraga
Victor Zuriel Dominguez Salvador


### Roles de los miembros 

Rol de Victor Zuriel Dominguez Salvador: Prototipo en físico (maqueta)/ Hardware/ Programación. 
Rol de Eduardo Cabrera Mendoza: Prototipo en físico (maqueta)/ Hardware/Programación.
Rol de José Ernesto Calvillo Lizárraga: Documentación/Programación.  


--------------------------------------------------------------------------------------------------------------------------------------

## Introducción

### Tematica del proyecto

El tema del proyecto es la creación de un sistema que ubique en un mapa en tiempo real donde se presenta algún incendio o una acumulación de gases.


### Planteamiento del problema

Con base a los datos del Instituto Nacional de Estadística y Geografía (INEGI) podemos determinar que actualmente el país sufre de un sistema de control de incendios deficiente, este se debe a varios factores los cuales varian entre cada localidad, algo que siempre se comenta son las llamadas falsas o que no son emergencia al 911 y la falta de recursos en los cerpos de bomberos para cubrir grandes distancias rapidamente y también se han presentado casos en los que a los cuerpos de emergencia se les complica identificar la ubicación del siniestro en áreas rurales.


### Justificación

De acuerdo con datos del Instituto Nacional de Estadística y Geografía (INEGI) en México se registran más de 95 mil incendios urbanos y no urbanos, dando un promedio de 260 incendios al día en todo el territorio nacional.
El 21.7% de los incendios ocurren en viviendas, mientras que el 17.6% en comercios, el 12.2% en bodegas, un 11.2% en lotes baldios y un 37.3% en otros sitios como escuelas, hospitales, etc. Entre las causas de incendio identificados, la acumulación de Gas LP toma la segunda posición por detras de las fallas eléctricas. Estos siniestros ocasionan el 26.9% de la totalidad de la mortalidad asociada a humo, gases tóxicos, etc.
Según la Encuesta Nacional de Salud y Nutrición (ENSANUT), en México 124 mil personas sufren quemaduras no fatales al año, y por cada fallecido, 220 personas quedan con secuelas de por vida.
![](https://github.com/ZurielSalvador/Proyecto-Capstone-Seguridad-de-eventos-Catastroficos/blob/main/Imagenes/Grafica%20sitios%20donde%20ocurren%20incendios.png)


### Planteamiento de la solución

Nuestro proyecto es un sistema de detección de siniestros que ocurren en departamentos que busca prevenir las muertes en estos eventos catastróficos, el sistema se basa en sensores que miden diferentes parámetros para determinar si el lugar sufre de una fuga de gas o de un incendio mediante parametros como la temperatura, CO2, etc. y de acuerdo con ello enviar una señal al servidor el cual identificará en un mapa la ubicación y el tipo de emergencia, además de reportar al dueño mediante un mensaje por Whatsapp y a los números de emergencia proporcionados por el dueño.


Este sistema se tiene planeado ofrecer a los cuerpos de emergencia con el fin de generar un sistema el cual sea capaz de identificar y reportar emergencias rapidamente antes de que pueda cobrar vidas.

Algunos obstaculos a superar serían de caracter politicos sociales, esto ya que evidentemente sería un servicio el cual requiera mantenimiento generando gastos públicos y para los usuarios que deseen instalarlos.

Una vez implementado se puede generar a futuro un gran sistema de emergencias el cual pueda llegar a ser un seguimiento capaz de representar varias emergencias y realizar un seguimiento en tiempo real la ubicación de los cuerpos de emergencia y trazar rutas para reducir tiempos de traslado.


### Objetivos

#### Generales

#### Particulares

### Grupo de enfoque


## Primer avance del proyecto.



### Implementación.



1. Se elaboró un programa de ejemplo para el sensor de flama- Sensor-ARD-364.



     Para poder ver dicho código se encuentra en la carpeta Codigo-Sensores/Sensor-ARD-364


2. Se elaboró un ejemplo para enviar mensaje por Whatsapp mediante a Node-RED.



     El archivo JSON se encuentra en la carpeta llamada: Notificación por whatsapp mediante Node-Red



3. Se elaboró un codigo del sensor mpu6050 dónde guarda los valores en la base de datos MySQL, posteriormente se gráfica en grafana.


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



























