# -*- coding: utf-8 -*-
# @Author: Thibault PECH
# @Date:   2022-02-21 10:30:18
# @Last Modified by:   Thibault PECH
# @Last Modified time: 2022-02-21 12:10:55
import platform
import socket
import cpuinfo
import mysql.connector
import psutil
import time
import shutil


def seconds_elapsed():
    return time.time() - psutil.boot_time()

mydb = mysql.connector.connect(
    host="192.168.43.197",
    user="caiomi",
    database="supervisionpython"
)

mycursor = mydb.cursor()

sql = "INSERT INTO info_pc (hostname, OS_NAME, uptime, kernel, CPUname, CPUfrequency) VALUES (%s, %s, %s, %s, %s, %s);"
val = (str(socket.gethostname()), str(platform.system()), float(seconds_elapsed()), str(platform.release()), str(cpuinfo.get_cpu_info()["brand_raw"]), float(str(cpuinfo.get_cpu_info()["hz_actual_friendly"])[:4]))
print(val)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


platform.system()
socket.gethostname()
cpuinfo.get_cpu_info()
platform.release()
socket.gethostbyname(socket.gethostname())
platform.version()
platform.machine()

total, used, free = shutil.disk_usage("/")

print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))
