#!/usr/bin/python3.9


from random import choice

class Drunk:

    def __init__(self, name: str) -> None:
        self.name = name


class TraditionalDrunk(Drunk):

    def __init__(self, name: str) -> None:
        super().__init__(name)

    def walk():
        return choice([(0, 1), (0, -1), (1, 0), (-1, 0)])



def main():
    pass



if __name__ == "__main__":
    main()
