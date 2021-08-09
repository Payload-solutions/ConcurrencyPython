#!/usr/bin/python3

import multiprocessing

def main(mylist: list, result: list, square_sum):
    """
    Function to square a give list
    """

    for idx, num in enumerate(mylist):
        result[idx] = num **2

    # square_sum value
    square_sum.value = sum(result)

    print("Result(in process p1): {}".format(result[:]))

    # print square sum_value

    print("Sum of squares (in process p1): {}".format(square_sum.value))


if __name__ == "__main__":

    my_list = [1, 2, 3, 4]

    # creating array of int data type with space for 4 integers
    result = multiprocessing.Array("i", 4)

    # creating valur of int data type
    square_sum = multiprocessing.Value("i")

    # creating new process
    p1 = multiprocessing.Process(target=main, args=(my_list, result, square_sum))

    p1.start()
    p1.join()

    print("Result (in main program): {}".format(result[:]))
    print("Sum of squares (in main program): {}".format(square_sum.value))




