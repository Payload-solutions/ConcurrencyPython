#!/usr/bin/python3.9

import os
from time import time
import time
from multiprocessing import (
    cpu_count,
    shared_memory,
    current_process,
    Lock,
    Process,
)

from random import randint
import numpy as np


# the number of cpu's of currently machine
CORES_NUMBER = cpu_count()
# initialize the Lock process
lock = Lock()
adder = 0
list_values  = [randint(1, 25) for _ in range(10)]


print("This is the sum of the array {} : {}".format(list_values, sum(list_values)))

def init_process(shr_name):
    """[summary]

    Args:
        sh_mem ([type], optional): [shared memory type to get and set name]. Defaults to None.
        position ([type], optional): [the position in the list to be added to global adder]. Defaults to None.
    """
    time_1 = time.time()
    global adder
    
    existing_shm = shared_memory.SharedMemory(name=shr_name)
    adder = sum(existing_shm.buf)
    # print(len(existing_shm.buf))
    lock.acquire()
    lock.release()
    # time.sleep(3)

    print("Procesador {} ejecutandose".format(current_process().name))
    time_2 = time.time()
    existing_shm.close()


    print("la función sumó {} y tardó {:.7f} segundos en hacerlo".format(adder, (time_2 - time_1)))


def send_messages():

    size_buffer = np.array(list_values).nbytes
    # print(size_buffer)
    sh_mem = shared_memory.SharedMemory(create=True, size=size_buffer)
    # # print(sh_mem.buf)
    # sh_mem.buf[:6] = b'arturo'
    # print([x for x in sh_mem.buf])
    # # print(sum(sh_mem.buf))
    # print(bytes(sh_mem.buf[:6]))
    # sh_mem.buf[:len(list_values)] = list_values
    # sh_mem.buf[[x for x in list_values]]
    # lambda x,y: [sh_mem.buf[x] = y for x, y in enumerate(list_values)] 

    for x, y in enumerate(list_values):
        sh_mem.buf[x] = y
    
    print([x for x in sh_mem.buf])
    return sh_mem



def main():

    # indicamos si el procesador es el principal que se está ejecutando
    if current_process().name == "MainProcess":
        print("[*] Bloqueo creado...")

        # for i, j in enumerate(list_values):
        sh_men = send_messages()
    
        processes = list()

        for _ in range(CORES_NUMBER):
            process = Process(target=init_process, args=(sh_men.name,))
            processes.append(process)
            process.start()

        for process in processes:
            process.join()


        sh_men.close()
        sh_men.unlink()
    
if __name__ == "__main__":
    main()