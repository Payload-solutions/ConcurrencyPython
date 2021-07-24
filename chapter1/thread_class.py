#!/usr/bin/python3

from threading import Thread


class MyWorkerThread(Thread):

    def __init__(self):
        print("Hello world")
        Thread.__init__(self)

    def run(self):
        print("Thread is now running")


def main():
    my_thread = MyWorkerThread()
    print("Created my thread object")
    my_thread.start()
    print("Started my thread")
    my_thread.join()
    print("My thread finshed")

if __name__ == "__main__":
    main()
