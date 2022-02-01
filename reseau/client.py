# -*- coding: utf-8 -*-
# @Author: Thibault PECH
# @Date:   2022-01-27 13:31:17
# @Last Modified by:   Thibault PECH
# @Last Modified time: 2022-02-01 17:59:17
import socket
import tkinter.messagebox as message
from tkinter import *

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def envoyerMessage():
    socket.connect((str(Eip.get()), int(Eport.get())))
    socket.send(bytes(Emsg.get(), 'utf8'))
    message.showinfo('Information', 'Message envoyé')


window = Tk()
window.title('Message à envoyer')

frame = Frame(window)

Lmsg = Label(window, text='Message:')
Lmsg.pack(padx=15, pady=5)

Emsg = Entry(window, bd=5)
Emsg.pack(padx=15, pady=5)
Emsg.focus_set()

Lip = Label(window, text='IP:')
Lip.pack(padx=15, pady=5)

Eip = Entry(window, bd=5)
Eip.pack(padx=15, pady=5)
Eip.insert(0, 'localhost')

Lport = Label(window, text='Port:')
Lport.pack(padx=15, pady=5)

Eport = Entry(window, bd=5)
Eport.pack(padx=15, pady=5)
Eport.insert(0, '15555')


btn = Button(frame, text='Envoyer un message', command=envoyerMessage)

btn.pack(side=RIGHT, padx=1)
frame.pack(padx=50, pady=25)


window.mainloop()
socket.close()
