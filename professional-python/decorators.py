#!/usr/bin/python3

from datetime import datetime



def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print("Has been passed {} seconds".format(time_elapsed.total_seconds()))

    return wrapper

@execution_time
def random_func():
    for _ in range(10000000):
        pass

@execution_time
def make_response(name="Arturo"):
    print(name)





def main():
    random_func()
    make_response("Francesco")



if __name__ == "__main__":
    main()
