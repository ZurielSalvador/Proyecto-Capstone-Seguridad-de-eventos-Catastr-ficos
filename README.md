# Proyecto-Capstone-Seguridad-de-eventos-Catastroficos

[![Logo.png](https://i.postimg.cc/HWrnGPKQ/Logo.png)](https://postimg.cc/7byw0Xq6)



--------------------------------------------------------------------------------------------------------------------------------------

### Descripción

Sistema de seguridad para detectar posibles eventos catastróficos. Enfocado en ayudar y prevenir posibles accidentes de viviendas como incendios o anomalías con ayuda de la supervisión, monitoreo y detección de dichos eventos.


### Planteamiento del problema

Con base a los datos del Instituto Nacional de Estadística y Geografía (INEGI) podemos determinar que actualmente el país sufre de un sistema de control de incendios deficiente, este se debe a varios factores los cuales varían entre cada localidad, algo que siempre se comenta son las llamadas falsas o que no son emergencia al 911 y la falta de recursos en los cuerpos de bomberos para cubrir grandes distancias rápidamente y también se han presentado casos en los que a los cuerpos de emergencia se les complica identificar la ubicación del siniestro en áreas rurales.

### Justificación

De acuerdo con datos del Instituto Nacional de Estadística y Geografía (INEGI) en México se registran más de 95 mil incendios urbanos y no urbanos, dando un promedio de 260 incendios al día en todo el territorio nacional. El 21.7% de los incendios ocurren en viviendas, mientras que el 17.6% en comercios, el 12.2% en bodegas, un 11.2% en lotes baldíos y un 37.3% en otros sitios como escuelas, hospitales, etc. Entre las causas de incendio identificados, la acumulación de Gas LP toma la segunda posición por detrás de las fallas eléctricas. Estos siniestros ocasionan el 26.9% de la totalidad de la mortalidad asociada a humo, gases tóxicos, etc. Según la Encuesta Nacional de Salud y Nutrición (ENSANUT), en México 124 mil personas sufren quemaduras no fatales al año, y por cada fallecido, 220 personas quedan con secuelas de por vida.



<p align="center">
  <img width="449" height="354" src="https://github.com/ZurielSalvador/Proyecto-Capstone-Seguridad-de-eventos-Catastroficos/blob/main/Imagenes/Grafica%20sitios%20donde%20ocurren%20incendios.png">
</p>


#### Objetivo General

Supervisar en tiempo real las viviendas o empresas en caso de un posible incendio o fuga de gas para obtener una mayor seguridad.

#### Objetivos Particulares

     -Detectar un incendio de una determinada vivienda o departamento.

     -Asegurar a personas que puedan salir heridas.

### Resultados esperados

Se espera tener un sistema funcional, con las funciones necesarios para la detección, monitoreo y localización a tráves de símbolos de advertencia de acuerdo a la cantidad masiva de datos. Visualización de un mapa en tiempo real dónde se puedan ver las localizaciones de las casas que posiblemente sufran de algún evento catastrófico.



### Materiales Necesarios 

[![materiales.jpg](https://i.postimg.cc/V6tf74zj/materiales.jpg)](https://postimg.cc/9RWH0dRM)





### WorkFlow:


[![Diagrama-en-blanco.png](https://i.postimg.cc/mkHJ76NH/Diagrama-en-blanco.png)](https://postimg.cc/Wqs5v8yN)




### Instrucciones:


1. Primero instala en Raspberry Pi 4 mosquitto, con los siguientes comandos de manera ordenada:


     -sudo wget http://repo.mosquitto.org/debian/mosquitto-repo.gpg.key


     -sudo apt-key add mosquitto-repo.gpg.key


     -cd /etc/apt/sources.list.d/


     -sudo wget http://repo.mosquitto.org/debian/mosquitto-buster.list


     -sudo apt-get update


     -sudo apt-get install mosquitto


     -sudo apt-get install mosquitto-client



2. Ahora instalaremos la siguiente librería con ayuda del comando:


     -pip install paho-mqtt


     Esta librería nos permite publicar en MQTT programando en Python3.


3. Clona nuestro el repositorio, y corre el programa llamado Proyecto-Seguridad.py

   *Nota: EL programa debe ser modificado de acuerdo a tu ubicación de vivienda*


4. Arma el circuito

[![Untitled-Sketch-bb.png](https://i.postimg.cc/zXBM8vRQ/Untitled-Sketch-bb.png)](https://postimg.cc/V5x4FYg9)


5. Se diseña en Node-Red un flow capaz de recibir datos necesarios publicados en MQTT posteriormente da una alarma en el sistema y encuentra tu ubicación por lo cual esta encedará un símbolo dependiendo la detección de los sensores.


6. Finalmente Prueba el circuito.




## Desarrollado por:


**Victor Zuriel Dominguez Salvador**

**Eduardo Cabrera Mendoza**
     
**José Ernesto Calvillo Lizárraga**
     



























