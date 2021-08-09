#!/usr/bin/python3.9

from multiprocessing import (
    shared_memory,
    cpu_count
)
from random import randint


def main():
    print("That's the cpu number: ", cpu_count())
    list_vals = [randint(1, 100) for _ in range(10)]

    print(list_vals)

if __name__ == "__main__":
    main()