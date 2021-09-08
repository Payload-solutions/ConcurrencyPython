#!/usr/bin/python3

"""Another way to optimize algorithms, such 
binary search and the most commomly Fibonacci
"""
import time
from pprint import pprint


class FiboIter:
    """Fibonacci implementation to improve time execution"""
    def __init__(self, max: int) -> None:
        self.max = max

    def __iter__(self):

        """In short, defining __iter__ to return self is
        essentialy turning an iterator object into  an iterable
        quickly so that you can use it in a for loop. Recall that 
        an iterator is an object wuth a next method for the purpose
        of returning the next item in the process of performing a iteration"""

        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self

    def __next__(self) -> int:
        
        if self.counter == 0:
            self.counter += 1
            return self.n1
        elif self.counter == 1:
            self.counter += 1
            return self.n2
        else:
            if self.counter < self.max:
                self.aux = self.n1 + self.n2
                self.n1, self.n2 = self.n2, self.aux
                self.counter += 1
                return self.aux
            else:
                raise StopIteration


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



def prime_numbers(num_ran: int) -> list:
    
    numbers = list()
    counter = 0
    for x in range(2, num_ran):
        for y in range(2, x):

            if x % y == 0:
                counter += 1
        if counter >= 1:
            counter = 0
        else:
            counter = 0
            numbers.append(x)

    return numbers


class PrimeIter:
    
    def _check_prime_(self, number: int) -> bool:
        for seq in range(2, number):
            if number % seq == 0:
                return False

        return True

    def __init__(self, max):
        self.max = max
        self.primes = 0
        self.number = 1

    def __iter__(self):
        """In short, defining __iter__ to return self is
        essentialy turning an iterator object into  an iterable
        quickly so that you can use it in a for loop. Recall that 
        an iterator is an object wuth a next method for the purpose
        of returning the next item in the process of performing a iteration"""
        return self

    def __next__(self):
        self.number += 1
        if self.primes > self.max:
            raise StopIteration
        elif self._check_prime_(self.number):
            self.primes += 1
            return self.number
        else:
            return self.__next__()


def main():
    time_1 = time.time()
    primes = PrimeIter(20)
    for prime in primes:
        print(prime)
    time_2 = time.time()
    print(f"The time to execute the query is {round(time_2 - time_1, 7)} seconds")




if __name__ == "__main__":
    main()