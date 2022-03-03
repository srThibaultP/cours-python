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

def seconds_elapsed():
    return time.time() - psutil.boot_time()

total, used, free = shutil.disk_usage("/")

with open('/home/caiomi/cours-python/projet/services.csv', 'r') as fd:
    reader = csv.reader(fd)
    for row in reader:
        # do something
        status = os.system('systemctl is-active --quiet ' + row[0])
        print(status)  # will return 0 for active else inactive.

senddata = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
senddata.connect(("localhost", 8080))
databdd = {'hostname' : socket.gethostname(), 
           'OS_NAME' : platform.system(),
           'uptime' : seconds_elapsed(),
           'kernel' : platform.release(),
           'CPUname' : cpuinfo.get_cpu_info()['brand_raw'],
           'CPUfrequency' : str(cpuinfo.get_cpu_info()['hz_actual_friendly'])[:4],
           'datetime' : time.strftime("%Y-%m-%d %H:%M:%S"),
           'total' : total // (2**30),
           'used' : used // (2**30),
           'free' : free // (2**30)
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


