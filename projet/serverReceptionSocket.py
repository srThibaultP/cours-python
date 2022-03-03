# -*- coding: utf-8 -*-
# @Author: Thibault PECH
# @Date:   2022-01-27 09:43:03
# @Last Modified by:   Thibault PECH
# @Last Modified time: 2022-02-01 18:09:01
import socket
import threading
import mysql.connector
import json

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mydb = mysql.connector.connect(
    host="192.168.43.197",
    user="caiomi",
    database="supervisionpython"
)

mycursor = mydb.cursor()

def serveur():
    socket.bind(('', 8080))
    print("Serveur lancé")
    while True:
        socket.listen(5)
        client, temp = socket.accept()

        response = client.recv(510)
        if response != "":
            dataagent = json.loads(response.decode("utf8"))
            print(dataagent)
            sql = "INSERT INTO info_pc (hostname, OS_NAME, uptime, kernel, CPUname, CPUfrequency, datetime, total, used, free, CPUmin, CPUmax) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            val = (dataagent["hostname"], dataagent["OS_NAME"], dataagent["uptime"], dataagent["kernel"], dataagent["CPUname"],
            dataagent["CPUfrequency"], dataagent["datetime"], dataagent["total"], dataagent["used"], dataagent["free"], dataagent["CPUmin"], dataagent["CPUmax"])
            print(val)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
    client.close()
    socket.close()


tS = threading.Thread(name='serveur', target=serveur)

tS.start()




