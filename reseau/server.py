# -*- coding: utf-8 -*-
# @Author: Thibault PECH
# @Date:   2022-01-27 09:43:03
# @Last Modified by:   Thibault PECH
# @Last Modified time: 2022-02-01 18:09:01
from tkinter import *
import socket
import threading

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def window():
    window = Tk()
    window.title('Serveur')

    global affichage
    affichage = StringVar()
    affichage.set("En attente d'une connexion")
    champ = Entry(window, textvariable=affichage, width=50)
    champ.pack()
    window.mainloop()


def serveur():
    socket.bind(('', 8080))

    while True:
        socket.listen(5)
        client, temp = socket.accept()

        response = client.recv(255)
        if response != "":
            affichage.set(response.decode("utf8"))
    client.close()
    socket.close()


tF = threading.Thread(name='window', target=window)
tS = threading.Thread(name='serveur', target=serveur)

tF.start()
tS.start()
