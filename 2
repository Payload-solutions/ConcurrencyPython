#!/usr/bin/python3

import threading
import time



def condition(*args, **kwargs):
    """Factory function that returns a new condition variable object.
    A condition variable allows one or more threads to wait until they are
    notified by another thread.
    If the lock argument is given and not None, it must be a Lock or RLock
    object, and it is used as the underlying lock, otherwise, a new RLock object
    is created and used as the underlying lock."""
    pass

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



def main():
    try:
        work = MyWorker()
        work.modify_both()
    except KeyboardInterrupt as e:
        print("\n[*] Exiting...")


if __name__ == "__main__":
    main()
