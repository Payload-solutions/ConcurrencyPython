#!/usr/bin/python3


class Node:

    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

class TwoWayNode(Node):
    
    def __init__(self, data, previous=None, next=None) -> None:
        super().__init__(data, next=next)



def main():
    pass


if __name__ == "__main__":
    main()