#!/usr/bin/python



import threading
import time
import random

def my_thread(i_val):
    print("Thrad {}: Started".format(i_val))
    time.sleep(random.randint(1,5))
    print("Thread {}: finished".format(i_val))


def main():
    for i in range(4):
        thread = threading.Thread(target = my_thread, args = (i,))
        thread.start()

    print("Enumerating: {}".format(threading.enumerate()))

if __name__ == "__main__":
    main()

