#!/usr/bin/python3

import threading
import time


class MyWorker:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.lock = threading.Lock()

    def modify_a(self):
        with self.lock:
            print("Modifying A: RLock Acquired: {}".format(self.lock._is_owned()))
            print("{}".format(self.lock))
            self.a += 1
            time.sleep(5)

    def modify_b(self):
        with self.lock:
            print("Modifying B: Lock Acquired: {}".format(self.lock._is_owned()))
            print("{}".format(self.lock))
            self.b += 1
            time.sleep(5)

    def modify_both(self):
        with self.lock:
            print("Lock acquired, modifying A and B")
            print("{}".format(self.lock))
            self.modify_a()
            print("{}".format(self.lock))
            self.modify_b()
        print("{}".format(self.lock))