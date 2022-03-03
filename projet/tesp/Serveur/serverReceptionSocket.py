# -*- coding: utf-8 -*-
# @Author: Thibault PECH
# @Date:   2022-01-27 09:43:03
# @Last Modified by:   Thibault PECH
# @Last Modified time: 2022-02-01 18:09:01
import socket
import threading
import mysql.connector
import json
import http.server

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connextion BDD
mydb = mysql.connector.connect(
    host="192.168.43.197",  # IP du serveur
    user="caiomi",  # Nom d'utilisateur
    database="supervisionpython"  # Nom de la base de données
)

mycursor = mydb.cursor()
#Partie serveur socket pour envoyer les données dans la BDD


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


def web():
    # Serveur
    PORT = 8888
    server_address = ("", PORT)

    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    handler.cgi_directories = ["/"]
    print("Serveur actif sur le port :", PORT)

    httpd = server(server_address, handler)
    httpd.serve_forever()


tS = threading.Thread(name='serveur', target=serveur)
tW = threading.Thread(name='web', target=web)

tS.start()
tW.start()
