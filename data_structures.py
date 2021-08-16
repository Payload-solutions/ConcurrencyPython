#!/usr/bin/python3.9

"""
:author Arturo Negreiros
:description Linear datastructures course
"""


def sorting_datastructures():
    pass



def pyramid_sum(lower, upper, margin=0) -> int:
    blanks = " "* margin
    print(blanks, lower, upper)

    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result

def main():
    # fruits = ["Apple", "kiwi", "Berry", "Grape", "Orange"]
    # print(fruits)
    # fruits.sort()
    # print(fruits)

    pyramid_sum(1, 4)

    # pop delete the las elements
    # fruits.pop()

if __name__ == "__main__":
    main()
