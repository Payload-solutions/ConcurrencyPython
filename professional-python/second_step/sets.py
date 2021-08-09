#!/usr/bin/python3



from random import randint



def remove_duplicates(some_list: list):
    return set(some_list)

def main():
    print(remove_duplicates([randint(1, 100) for _ in range(10000)]))


if __name__ == "__main__":
    main()
