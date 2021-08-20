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

print("""
'########:::::'###::::'########:::::'###::::'##:::::::'########:'##:::::::'##:::::::'####::'######::'##::::'##:
 ##.... ##:::'## ##::: ##.... ##:::'## ##::: ##::::::: ##.....:: ##::::::: ##:::::::. ##::'##... ##: ###::'###:
 ##:::: ##::'##:. ##:: ##:::: ##::'##:. ##:: ##::::::: ##::::::: ##::::::: ##:::::::: ##:: ##:::..:: ####'####:
 ########::'##:::. ##: ########::'##:::. ##: ##::::::: ######::: ##::::::: ##:::::::: ##::. ######:: ## ### ##:
 ##.....::: #########: ##.. ##::: #########: ##::::::: ##...:::: ##::::::: ##:::::::: ##:::..... ##: ##. #: ##:
 ##:::::::: ##.... ##: ##::. ##:: ##.... ##: ##::::::: ##::::::: ##::::::: ##:::::::: ##::'##::: ##: ##:.:: ##:
 ##:::::::: ##:::: ##: ##:::. ##: ##:::: ##: ########: ########: ########: ########:'####:. ######:: ##:::: ##:
..:::::::::..:::::..::..:::::..::..:::::..::........::........::........::........::....:::......:::..:::::..::

    Team:
        Solorzano Ricardo
        Negreiros Arturo
        Hernández José
        Pin Anthony
        Puente Joselyn
""")


lock = Lock()
print("Esta es la cantidad de cpu's que tengo {}".format(cpu_count()))
list_vals = [randint(1, 25) for _ in range(10)]
print(list_vals)

sum_array = 0


def sum_vector(shr_name):
    global sum_array
    existing_shm = shared_memory.SharedMemory(name=shr_name)
    for x in list_vals:
        sum_array += x
    lock.acquire()
    # np_array[:] = np_array[0] + 1
    lock.release()
    # time.sleep(5)
    print("Este es el procesador actual: ", current_process().name)
    time.sleep(3)
    print("id del proceso donde se ejecuta: ", os.getpid())
    time.sleep(3)
    print("suma: ", sum_array)
    time.sleep(3)
    # print("suma de las 10 posiciones: ", sum_array)
    existing_shm.close()

def create_shared_block():
    shm = shared_memory.SharedMemory(create=True, size=20)

    return shm

def main():

    if current_process().name == "MainProcess":
        print("Creado bloque compartido...")
        shr = create_shared_block()

        processes = list()

        for _ in range(cpu_count()):
            _process = Process(target=sum_vector, args=(shr.name, ))
            processes.append(_process)
            _process.start()


        for _process in processes:
            _process.join()

        shr.close()
        shr.unlink()

if __name__ == "__main__":
    main()
