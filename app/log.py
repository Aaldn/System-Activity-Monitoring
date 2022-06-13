#!/usr/bin/python3

import os
import socket
import datetime
import re
import psutil

# log informations for one row
current_date = datetime.datetime.now()
hostname = socket.gethostname()
cpu_load = psutil.cpu_percent()
ram_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage("/").percent

# set working directory, list and sort all files
os.chdir('/var/log/system_activity_monitoring')
files = os.listdir()
files.sort()

# last log file informations
last_file = files[-1]
file_name = "log-"
file_number = re.search(r"(\d)+", last_file).group(0)
file_extension = ".log"


# append log to the last log file
def append_log():
    log = open(file_name + file_number + file_extension, "a")
    log.write("[ " + current_date.isoformat() + " ] " + hostname + " - " +
              str(cpu_load) + "% ; " + str(ram_usage) + "% ; " + str(disk_usage) + "%\n")
    log.close()


# create new log file every 24 hours
def create_log():
    date_creation = datetime.datetime.fromtimestamp(
        os.path.getmtime(last_file))
    if date_creation <= current_date - datetime.timedelta(hours=24):
        open(file_name + str(int(file_number) + 1) + file_extension, "x")


# remove log file every 14 days
def remove_log():
    for file in files:
        date_creation = datetime.datetime.fromtimestamp(
            os.path.getmtime(file))
        if date_creation <= current_date - datetime.timedelta(days=14):
            os.remove(file)
