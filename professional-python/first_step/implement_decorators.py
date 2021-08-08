#!/usr/bin/python3

"""
A decorators is a closure, or it's a function
that recive another function as parameter,
add more stuffs and return a different function
"""


def make_decorator(function):
    def wrapper():
        print("Arturo, this is a function inside the function :v")
        function()
    return wrapper



@make_decorator
def greeting():
    print("Hey...")


def main():
    greeting()


if __name__ == "__main__":
    main()
