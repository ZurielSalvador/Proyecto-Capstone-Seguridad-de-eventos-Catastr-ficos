#Bibliotecas
import mysql.connector

#Conexión
cnx = mysql.connector.connect(user='lalo', password='2907', host='127.0.0.1', database='codigoIoT')

#Query
query = ("SELECT * FROM casas;")

#Petición
cursor = cnx.cursor()
cursor.execute(query)
res = cursor.fetchall()

#Impresion del resultado
for x in res:
    print(x)

#Final de la conexión
cursor.close()
cnx.close()