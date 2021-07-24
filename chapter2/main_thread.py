#!/usr/bin/python3


import threading
import time

def my_child_thread():
    print("Child Thread staring")
    time.sleep(5)
    print("Current thread ------")
    print(threading.current_thread())
    print("---------------------")
    print("Main thrad ----------")
    print(threading.main_thread())
    print("---------------------")
    print("Child Thread Ending")

child = threading.Thread(target = my_child_thread)
child.start()
child.join()
