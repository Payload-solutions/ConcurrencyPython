#!/usr/bin/python3


import threading
import time


def my_thread():
    print("Thread {} starting".format(threading.currentThread().getName()))
    time.sleep(10)
    print("Thread {} ending".format(threading.currentThread().getName()))

for i in range(4):
    thread_name = "Thread-"+str(i)
    thread = threading.Thread(name = thread_name, target = my_thread)
    thread.start()

print("{} ".format(threading.enumerate()))
