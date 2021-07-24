#!/usr/bin/python3



import threading
from multiprocessing import Process
import time
import os

def my_task():
    print("Starting")
    time.sleep(2)

t_0 = time.time()
threads = list()

for i in range(10):
    thread = threading.Thread(target = my_task)
    thread.start()
    threads.append(thread)

t_1 = time.time()
print("Total time for Creating 10 threads: {}".format(t_1 - t_0))

for thread in threads:
    thread.join()

t_2 = time.time()
proces = list()

for i in range(10):
    process = Process(target = my_task)
    process.start()
    proces.append(process)


t_3 = time.time()
print("Total time for creating 10 Processes: {}".format(t_3 - t_2))

for proc in proces:
    proc.join()
