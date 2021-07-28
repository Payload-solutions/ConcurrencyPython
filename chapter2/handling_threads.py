#!/usr/bin/python3


import threading
import time
import random


def execute_thread(i_value):
    print("Thread {} started".format(i_value))
    sleep_time = random.randint(1,10)
    time.sleep(sleep_time)

    print("Thread {} finished executing".format(i_value))

for i in range(10):
    thread = threading.Thread(target = execute_thread, args = (i,))
    thread.start()
    print("Active Threads:", threading.enumerate())
