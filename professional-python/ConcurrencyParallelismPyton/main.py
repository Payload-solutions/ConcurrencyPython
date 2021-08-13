#!/usr/bin/python3

# from mpi4py import MPI
import threading
import time
import random

counter = 1

def workerA():
    global counter
    while counter < 1000:
        counter += 1
        print("Worker A is incrementing counter to {}".format(counter))
        sleep_time = random.randint(0,1)
        time.sleep(sleep_time)

def workerB():
    global counter
    while counter > -1000:
        counter -= 1
        print("Worker B is decrementing counter to {}".format(counter))
        sleep_time = random.randint(0,1)
        time.sleep(sleep_time)

def main():

    t_0 = time.time()

    try:

        thread_1 = threading.Thread(target = workerA)
        thread_2 = threading.Thread(target = workerB)
        
        thread_1.start()
        thread_2.start()

        thread_1.join()
        thread_2.join()

        t_1 = time.time()
        
        print("Execution time {}".format(t_1 - t_0))

    except KeyboardInterrupt as ke:
        print(str(ke))

if __name__ == "__main__":
    main()
