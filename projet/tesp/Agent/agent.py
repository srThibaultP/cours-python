# -*- coding: utf-8 -*-
# @Author: Thibault PECH
# @Date:   2022-02-21 10:30:18
# @Last Modified by:   Thibault PECH
# @Last Modified time: 2022-02-21 12:10:55
import platform
import socket
import cpuinfo
import psutil
import time
import shutil
import os
import csv
import json

dirname = os.path.dirname(__file__) #Chemin relatif du script

def seconds_elapsed():  #Fonction qui renvoie le nombre de secondes écoulées depuis le lancement du script
    return time.time() - psutil.boot_time()

total, used, free = shutil.disk_usage("/")  #On récupère les informations sur le disque dur

with open(os.path.join(dirname, 'services.csv'), 'r') as fd:    #Cette partie permet de connaitre les services listées dans le fichier services.csv
    reader = csv.reader(fd)
    for row in reader:
        # do something
        status = os.system('systemctl is-active --quiet ' + row[0])
        if status == 0: #Si le service est actif
            print(row[0] + " est actif")
        else:   #Si le service est inactif
            print(row[0] + " est inactif")

senddata = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #On crée un socket
senddata.connect(("localhost", 8080))   #On se connecte au serveur - Changer ici l'adresse du serveur socket
#On prépare les données à envoyer au format json
databdd = {'hostname' : socket.gethostname(), 
           'OS_NAME' : platform.system(),
           'uptime' : seconds_elapsed(),
           'kernel' : platform.release(),
           'CPUname' : cpuinfo.get_cpu_info()['brand_raw'],
           'CPUfrequency': (psutil.cpu_freq().current*1000),
           'datetime' : time.strftime("%Y-%m-%d %H:%M:%S"),
           'total' : total // (2**30),
           'used' : used // (2**30),
           'free' : free // (2**30),
           'CPUmax': psutil.cpu_freq().max,
           'CPUmin': psutil.cpu_freq().min
           
           }
databdd = json.dumps(databdd)   #On convertit les données en json
senddata.sendall(bytes(databdd, 'utf8'))    #On envoie les données au serveur


