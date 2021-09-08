#!/usr/bin/python3

"""Another way to optimize algorithms, such 
binary search and the most commomly Fibonacci
"""
import time


class FiboIter:

    def __iter__(self):
        self.n1 = 0
        self.n2 = 1

    def __next__(self):
        pass





def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



def main():
    time_1 = time.time()
    print(fibonacci(8))
    # print(fibonacci(50))
    time_2 = time.time()

    print(f"The time to execute the query is {round(time_2 - time_1, 7)} seconds")




if __name__ == "__main__":
    main()