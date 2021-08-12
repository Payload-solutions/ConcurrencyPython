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





create_stack = [randint(1, 25) for _ in range(10)]
print("array %s created"%create_stack)



# instanciate a new Lock class
lock = Lock()

def add_stack(stack: list(int)) -> None:
    cumulator: int = 0

    for x in stack:
        cumulator += x
    
    print("We're in the %s "%current_process().name)
    print("The actual pid %s "%os.getpid())
    print(cumulator)

def main():
    array = Array("i", range(10))

    print(len(array))
    
    for x in array:
        print(x)



if __name__ == "__main__":
    main()
