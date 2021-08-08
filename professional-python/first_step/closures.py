#!/usr/bin/python3



def make_repeater_off(n):

    def repeater(string):
        assert type(string) == str, "Only you can use strings"
        return string * n
    return repeater


def main():
    repeat_5 = make_repeater_off(5)
    print(repeat_5(5))



if __name__ == "__main__":
    main()
