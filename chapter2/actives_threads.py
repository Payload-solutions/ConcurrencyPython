#!/usr/bin/python3


import threading
import time
import random



def my_thread(i_val):
    print("Thread {}: started".format(i_val))
    time.sleep(random.randint(1,5))


def main():
    for i in range(random.randint(2,50)):
        thread = threading.Thread(target = my_thread, args= (i,))
        thread.start()
    time.sleep(4)
    print("Total number of Active threads: {}".format(threading.active_count())) 


if __name__ == "__main__":
    main()
