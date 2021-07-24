#!/usr/bin/python3

import threading
import time
import random

def execute_thread(i):
    print("Thread {} started ".format(i))
    sleep_time = random.randint(1,10)
    time.sleep(sleep_time)

    print("Thread {} finished executing".format(i))

for i in range(10):
    thread = threading.Thread(target = execute_thread, args=(i,))
    thread.start()
    print("Active threads: ", threading.enumerate())



