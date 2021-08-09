#!/usr/bin/python3

# from multiprocessing import shared_memory



# def main():
#     memory = shared_memory.SharedMemory(create=True, size=10)
#     print(type(memory.buf))
#     print(len(memory.buf))

import ray
import time

ray.init()


@ray.remote
def f(x):
    time.sleep(1)
    return x


# start 4 tasks in paralell.
result_ids = []
for i in range(4):
    result_ids.append(f.remote(i))



def main():
    pass



if __name__ == "__main__":
    main()