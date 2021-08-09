#!/usr/bin/python3

"""
Implementin iterators in even number
"""

class EvenNumbers:

    def __init__(self, max=None):
        self.max = max

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            raise StopIteration


def main():
    pass



if __name__ == "__main__":
    main()
