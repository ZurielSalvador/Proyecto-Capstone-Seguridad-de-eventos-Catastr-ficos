from mpu6050 import mpu6050
import time
import sys
import mysql.connector
import argparse
mpu = mpu6050(0x68)

#Parser
#parser = argparse.ArgumentParser()
#parser .add_argument("status")
#args = parser.parse_args()

#Conexión
cnx= mysql.connector.connect(user='joseernestolan', password='1234', host='192.168.1.93', database='codigoIoT')

#Cursor
cursor = cnx.cursor()

while True:
        temp = mpu.get_temp()
        accel_data = mpu.get_accel_data()
        acc_x = accel_data['x']
        acc_y = accel_data['y']
        acc_z = accel_data['z']
        gyro_data = mpu.get_gyro_data()
        gyro_x = gyro_data['x']
        gyro_y = gyro_data['y']
        gyro_z = gyro_data['z']
        
        print("Temp : " + str(mpu.get_temp()))
        print()
        
        print("Acc X : " + str(accel_data['x']))
        print("Acc Y : " + str(accel_data['y']))
        print("Acc Z : " + str(accel_data['z']))
        print()
        
        print("Gyro X : " + str(gyro_data['x']))
        print("Gyro Y : " + str(gyro_data['y']))
        print("Gyro Z : " + str(gyro_data['z']))
        print()
        
        query_insert = "INSERT INTO MPU6050 (nombre,ACC_X,ACC_Y,ACC_Z,GYR_X,GYR_Y,GYR_Z,TEMP) VALUES ('" + str("Sensor 1") + "','" + str(acc_x) + "','" + str(acc_y) + "','" + str(acc_z) + "','" + str(gyro_x) + "','" + str(gyro_y) + "','" + str(gyro_z) + "'," + str (temp) +");"
        print(query_insert)
        
        #Ejecutar cursor
        cursor.execute(query_insert)
        #ASegurrse de realizar la operacion en BD
        cnx.commit()
        print("Query ok")
        print("---------------------------------")
        time.sleep(1)
