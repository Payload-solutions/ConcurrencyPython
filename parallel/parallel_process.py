#!usr/bin/python

import time
from multiprocessing import (
    Lock,
    Process,
    current_process,
    shared_memory,
    cpu_count,
    Array,
    Value
)

import numpy as np
from random import randint
import os
from typing import List

lock = Lock()
time.sleep(0.05)
print("""
'########:::::'###::::'########:::::'###::::'##:::::::'########:'##:::::::'##:::::::'####::'######::'##::::'##:
 ##.... ##:::'## ##::: ##.... ##:::'## ##::: ##::::::: ##.....:: ##::::::: ##:::::::. ##::'##... ##: ###::'###:
 ##:::: ##::'##:. ##:: ##:::: ##::'##:. ##:: ##::::::: ##::::::: ##::::::: ##:::::::: ##:: ##:::..:: ####'####:
 ########::'##:::. ##: ########::'##:::. ##: ##::::::: ######::: ##::::::: ##:::::::: ##::. ######:: ## ### ##:
 ##.....::: #########: ##.. ##::: #########: ##::::::: ##...:::: ##::::::: ##:::::::: ##:::..... ##: ##. #: ##:
 ##:::::::: ##.... ##: ##::. ##:: ##.... ##: ##::::::: ##::::::: ##::::::: ##:::::::: ##::'##::: ##: ##:.:: ##:
 ##:::::::: ##:::: ##: ##:::. ##: ##:::: ##: ########: ########: ########: ########:'####:. ######:: ##:::: ##:
..:::::::::..:::::..::..:::::..::..:::::..::........::........::........::........::....:::......:::..:::::..::
""")


def receive_message(shr_mem):

    memory_shared = shared_memory.SharedMemory(name=shr_mem)
    lock.acquire()
    
    lock.release()
    


def send_message():
    list_vals = np.array([randint(1, 25) for _ in range(10)])
    memory_shared = shared_memory.SharedMemory(create=True, size=list_vals.nbytes)

    return list_vals, memory_shared




def main():

    if current_process().name == "MainProcess":

        processors = list()
    
        list_vals, memory_shared = send_message()

        for _ in range(cpu_count()):
            process = Process(target=receive_message, args=(memory_shared,))
            processors.append(Process)
            Process.start()

        for process in processors:
            process.join()

if __name__ == "__main__":
    main()
