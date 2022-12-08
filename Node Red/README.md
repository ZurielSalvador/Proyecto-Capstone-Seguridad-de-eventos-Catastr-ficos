# Node Red
## Hacer una marca en el mapa
1.- Instalar nodos node-red-contrib-web-worldmap
2.- Importar el archivo ""
3.- Cambiar los datos del json del nodo "Marca" (De ser necesario)
4.- Apretar el nodo inject
5.- Ir a http://localhost:1880/worldmap/

## Recibir json mediante mqtt
1.- 

## Ejercicio completo
1.- Crear base de datos en MySQL
`CREATE TABLE casas (casaID INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, calle VARCHAR (32) NOT NULL, numero VARCHAR (16) NOT NULL, colonia VARCHAR (64) NOT NULL, delegacion VARCHAR (64) NOT NULL, latitud DECIMAL(9,6) NOT NULL, longitud DECIMAL(9,6) NOT NULL);`

2.- Insertar todas las casas que necesiten
`INSERT INTO casas (calle,numero,colonia,delegacion,latitud,longitud) VALUES ('Yuncas','Mz.21 Lt.22','2do Reacomodo tlacuitlapa','Álvaro Obregón',19.354509,-99.236450);`

3.- Recibimos el json con el siguiente formato por mqtt
`{"casaID":1,"temperatura":23,"gas":2000,"flama":0}'`

4.- {"casaID":1,"temperatura":23,"gas":2000,"flama":0,"latitud":19.354509,"longitud":-99.236450,"direccion":"Yuncas Mz.21 Lt22 Col. 2do Reacomodo Tlacuitlapa Del. Álvaro Obregón"}



## Pruebas 
#### Publicacion mqtt
mosquitto_pub -h 3.124.62.105 -t SeguridadCatastrofes/Departamento/cocina -m '{"casaID":1,"temperatura":23,"gas":2000,"flama":0,"latitud":19.354509,"longitud":-99.236450,"direccion":"Yuncas Mz.21 Lt22 Col. 2do Reacomodo Tlacuitlapa Del. Álvaro Obregón"}

#### JSON casa 1
{"casaID":1,"temperatura":23,"gas":2000,"flama":0,"latitud":19.354509,"longitud":-99.236450,"direccion":"Yuncas Mz.21 Lt22 Col. 2do Reacomodo Tlacuitlapa Del. Álvaro Obregón"}

#### JSON casa 2
{"casaID":2,"temperatura":100,"gas":2000,"flama":1,"latitud":19.442086,"longitud":-98.972768,"direccion":"Emiliano Zapata s/n, Transportistas, 56363 Chimalhuacán"}

#### JSON casa 3
{"casaID":3,"temperatura":100,"gas":2000,"flama":1,"latitud":19.312066,"longitud":-99.139903,"direccion":"Calz. de Tlalpan 3016/3058, Coapa, Ex-Hacienda Coapa, Coyoacán, 04980 Ciudad de México"}