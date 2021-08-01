#!/usr/bin/python3

def make_repeater(number: int):
    
    def repeater(string: str):
        assert type(string) == str, "only can be used strings"
        return string * number
    return repeater

def run():
    repeat_5 = make_repeater(5)
    print(repeat_5("hi"))

if __name__ == "__main__":
    run()