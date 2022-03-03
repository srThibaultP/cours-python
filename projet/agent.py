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

dirname = os.path.dirname(__file__)

def seconds_elapsed():
    return time.time() - psutil.boot_time()

total, used, free = shutil.disk_usage("/")

with open(os.path.join(dirname, 'services.csv'), 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        # do something
        status = os.system('systemctl is-active --quiet ' + row[0])
        if status == 0:
            print(row[0] + " is active")
        else:
            print(row[0] + " is inactive")

senddata = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
senddata.connect(("localhost", 8080))
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
databdd = json.dumps(databdd)
senddata.sendall(bytes(databdd, 'utf8'))

# platform.system()
# socket.gethostname()
# cpuinfo.get_cpu_info()
# platform.release()
# socket.gethostbyname(socket.gethostname())
# platform.version()
# platform.machine()

# print("Total: %d GiB" % (total // (2**30)))
# print("Used: %d GiB" % (used // (2**30)))
# print("Free: %d GiB" % (free // (2**30)))


