#!/usr/bin/python


import time
import random
import threading

def calculate_prime_factors(n):
    prim_fac = list()
    d = 2
    while d*d <= n:
        while (n%d) == 0:
            prim_fac.append(d)
            n //= d
        d += 1

    if n > 1:
        prim_fac.append(n)

    return prim_fac

def execute_proc():

    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculate_prime_factors(rand))

def main():
    print("Starting number crunching")
    t_0 = time.time()

    threads = []

    for i in range(10):
        thread = threading.Thread(target = execute_proc)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    t_1 = time.time()

    print("Excution time: {}".format(t_1 - t_0))

if __name__ == "__main__":
    main()
