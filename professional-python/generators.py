#!/usr/bin/pyrthon3


import time




def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    aux = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2

        elif aux >= max:
            # yield aux
            break

        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux



def main():
    fibonacci = fibo_gen(1000)
    try:
        for element in fibonacci:
            print(element)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("[!] Exiting")

if __name__ == "__main__":
    main()
