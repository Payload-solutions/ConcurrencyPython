#!/usr/bin/python3

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


lock.Lock()


def add_one(shr_name):

    existing_shm = shared_memory.SharedMemory(name=shr_name)
    np_array = np.ndarray((5000, 5000), dtype=np.int64, buffer=existing_shm.buf)
    lock.acquire()
    np_array[:] = np_array[0] + 1
    lock.release()
    time.sleep(3)
    print("Added one")
    existing_shm.close()

print(current_process())
print(current_process().name)
