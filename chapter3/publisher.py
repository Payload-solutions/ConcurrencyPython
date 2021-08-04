#!/usr/bin/python3

import threading
import time
import random
import sys

class Publisher(threading.Thread):

    def __init__(self, integers, condition) -> None:
        self.condition = condition
        self.integers = integers
        threading.Thread.__init__(self)

    def run(self):

        while True:
            integer = random.randint(0, 1000)
            self.condition.acquire()
            print("Condition Acquired by Publisher: {}".format(self.name))
            self.integers.append(integer)
            self.condition.notify()
            print("Condition Released by Publisher: {}".format(self.name))
            self.condition.release()
            time.sleep(1)

class Suscriber(threading.Thread):

    def __init__(self, integers, condition) -> None:
        self.integers = integers
        self.condition = condition
        threading.Thread.__init__(self)

    def run(self):
        while True:
            self.condition.acquire()
            print("Condition Acquired by consumer: {}".format(self.name))
            while True:
                if self.integers:
                    integer = self.integers.pop()
                    print("{} Popped from list by Consumer: {}".format(integer, self.name))
                    break
                print("Condition Wait by {}".format(self.name))
                self.condition.wait()
            print("Consumer {} Releasing Condition".format(self.name))
            self.condition.release()





def main():
    try:
        integers = list()
        condition = threading.Condition()

        # Our publisher
        publ = Publisher(integers, condition)
        publ.start()

        # Our suscribers
        sub1 = Suscriber(integers, condition)
        sub2 = Suscriber(integers, condition)

        sub1.start()
        sub2.start()

        # Joning our threads
        publ.join()
        sub1.join()
        sub2.join()

    except KeyboardInterrupt as e:
        print("\n[*] Exiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()
