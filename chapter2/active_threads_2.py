#!/usr/bin/python3


import threading
import time

def thread_target():
    print("Curent thread: {}".format(threading.current_thread()))


threads = []
for i in range(10):
    thread = threading.Thread(target = thread_target)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
