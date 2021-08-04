#!/usr/bin/python3
import threading
import time


def our_thread(i_val: int):
    print("Thread {} started\n".format(i_val))
    time.sleep(i_val*2)
    print("Thread {} finished\n".format(i_val))


def main():
    thread_1 = threading.Thread(target=our_thread, args=(1,))
    thread_1.start()
    print("Is thread 1 finished?")
    thread_2 = threading.Thread(target=our_thread, args=(2,))
    thread_2.start()
    thread_2.join()
    print("Thread 2 is definitely finished")


if __name__ == "__main__":
    main()
