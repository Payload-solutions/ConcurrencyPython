#!/usr/bin/python3

import threading
import multiprocessing
from random import randint

def implement_sum():

    values = [randint(1, 1000) for _ in range(10)]
    print(values)
    cumulator = 0
    for x in values:
        cumulator += x
        print(cumulator)



def main():
    sum_process = multiprocessing.Process(target = implement_sum)
    sum_process.start()
    sum_process.join()


if __name__ == "__main__":
    main()


