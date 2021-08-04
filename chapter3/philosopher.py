#!/usr/bin/python3
import random
import threading
import time


class Philosopher(threading.Thread):

    def __init__(self, left_fork, right_fork):
        print("Our Philosopher has sat down at the table")
        threading.Thread.__init__(self)
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        print("Philosopher {} has started thinking".format(threading.current_thread()))

        while True:
            time.sleep(random.randint(1, 5))
            print("Philosopher {} has finished thinking".format(threading.current_thread()))
            self.left_fork.acquire()

            time.sleep(random.randint(1, 5))
            try:
                print("Philosopher {} has acquired the left fork".format(threading.current_thread()))
                self.right_fork.acquire()

                try:
                    print("Philosopher {} has attained both forks, currently threading".format(
                        threading.current_thread()))
                finally:
                    self.right_fork.release()
                    print("Philosopher {} has released right fork".format(threading.current_thread()))

            finally:
                self.left_fork.release()
                print("Philosopher {} has released the left fork".format(threading.current_thread()))
