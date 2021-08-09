#!/usr/bin/python3

import multiprocessing
from random import randint




result_list = list()

def squared_my_list(my_list: list):
    """
    Squared given a list
    """
    global result_list
    # append squared if my list to global list result

    for num in my_list:
        result_list.append(num**2)

    print("Result (in process p1): {}".format(result_list))


def main():
    my_list = [randint(1, 100) for _ in range(10)]
    print(my_list)


    # creating a new process
    process_1 = multiprocessing.Process(target=squared_my_list, args=(my_list, ))

    # initializing process
    process_1.start()
    process_1.join()

    print("Result(in main program): {}".format(result_list))

if __name__ == "__main__":
    main()
