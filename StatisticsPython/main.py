#!/usr/bin/python3


"""
Memoitzation is a technique to save
preoviusly compute and avoid do again

Normally is currently used in dictionaries
whereas the queries can be do in O(1)

Switch time space
"""


# this implementation isn't efficient
# the time to calculate big fibonacci 
# numbers take a lot of time
def fibonacci_recursive(n: int) -> int:

    if n == 0 or n == 1:
        return 1
    return fibonacci_recursive(n-1)  +fibonacci_recursive(n-2)



def fibonacci_dinamic(n: int, memo = {}) -> int:
    if n == 0 or n == 1:
        return 1

    try:

        return memo[n]
    except KeyError:
        result = fibonacci_dinamic(n - 1, memo) + fibonacci_dinamic(n - 2, memo)
        memo[n] = result

        return result



def main():


    result = fibonacci_dinamic(55)
    print(result)




if __name__ == "__main__":
    main()
