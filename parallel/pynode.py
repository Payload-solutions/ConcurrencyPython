#!/usr/bin/python3.9

# from random import randint
# import time
# from link_list import SingleLinkList

class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


"""
def main():

    node = None
    stack = [randint(1, 100) for _ in range(5)]
    print(stack)
    time.sleep(0.5)
    link = SingleLinkList()
    for x in stack:
        link.append(x)

    main_ = link.tail

    while main_:
        print(main_.data)
        main_ = main_.next
    # for x in range(1, len(stack)):
    #     node = Node(stack[x-1], node)

    # while node is not None:
    #     print(node.data)
    #     node = node.next

if __name__ == "__main__":
    main()
"""


