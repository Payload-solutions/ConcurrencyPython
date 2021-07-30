#!/usr/bin/python3


def is_prime(number: int) -> bool:

    element = [True if number % x != 0 else False for x in range(1, number)]
    return len(set(element)) == 1 and element[0] == True


def main():
    # print(is_prime(7))
    # print(is_prime(8))
    ##  print(is_prime(11))


    for x in range(0, 100):
        if is_prime(x):
            print(x)


if __name__ == "__main__":
    main()
