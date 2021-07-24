#!/usr/bin/python3

from multiprocessing import Process
import time

def my_worker():
    t1 = time.time()
    print("Process sttarted at: {}".format(t1))

    time.sleep(20)

my_process = Process(target = my_worker)
print("Process {}".format(my_process))
my_process.start()
print("Terminating Process...")
my_process.terminate()
my_process.join()
print("Process terminated: {}".format(my_process))
