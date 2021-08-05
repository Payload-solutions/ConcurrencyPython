#!/usr/bin/python3
from multiprocessing import Lock
import threading
import random
import time
import queue


def main():
    def my_subscriber(queue):
        while not queue.empty():
            item = queue.get()
            if item is None:
                break
            print("{} removed from the queue {}".format(threading.current_thread(), item))
            queue.task_done()
            time.sleep(1)

    my_queue = queue.Queue()
    for i in range(10):
        my_queue.put(i)

    print("Queue populated")
    threads = list()

    for i in range(4):
        thread = threading.Thread(target=my_subscriber, args=(my_queue,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()
