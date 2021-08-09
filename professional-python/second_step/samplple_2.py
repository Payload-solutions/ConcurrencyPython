#!/usr/bin/python3



def make_gen():

    print("Hello Metallica")
    n = 0
    yield n

    print("Metallica rules!")
    n = 1
    yield n

    print("Hail Metallica")
    n = 2
    yield n





def main():
    gen = make_gen()
    try:
        print(next(gen))
        print(next(gen))
        print(next(gen))
        print(next(gen))
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
