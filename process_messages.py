#!/usr/bin/python

import os
from multiprocessing import (
    current_process,
    Process,
    Lock,
    cpu_count,
    shared_memory
)
import time
import numpy as np
from random import randint

lock = Lock()
print("Esta es la cantidad de cpu's que tengo {}".format(cpu_count()))

def add_one(shr_name):

    existing_shm = shared_memory.SharedMemory(name=shr_name)
    np_array = np.ndarray((5000, 5000), dtype=np.int64, buffer=existing_shm.buf)
    lock.acquire()
    np_array[:] = np_array[0] + 1
    lock.release()
    # time.sleep(5)
    print("Este es el procesador actual: ", current_process().name)
    time.sleep(3)
    print(os.getpid())
    time.sleep(3)
    print("Added one")
    existing_shm.close()

def create_shared_block():

    list_vals = [randint(1, 25) for _ in range(10)]
    print(list_vals)
    a= np.ones(shape=(5000, 5000), dtype=np.int64) # start with an existing numpy

    shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
    np_array = np.ndarray(a.shape, dtype=np.int64, buffer=shm.buf)
    np_array[:] = a[:]
    return shm, np_array


def main():

    if current_process().name == "MainProcess":
        print("Creating shared block")
        shr, np_array = create_shared_block()

        processes = list()

        for i in range(cpu_count()):
            _process = Process(target=add_one, args=(shr.name, ))
            processes.append(_process)
            _process.start()


        for _process in processes:
            _process.join()

        print("Final array")
        print(np_array[:10])
        print(np_array[10:])

        shr.close()
        shr.unlink()

if __name__ == "__main__":
    main()
