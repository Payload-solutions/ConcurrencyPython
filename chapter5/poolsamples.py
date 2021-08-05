from concurrent.futures import ProcessPoolExecutor
import os

def task(n):
    print("Processing{}".format(n))

def main():
    executor = ProcessPoolExecutor(max_workers=3)
    task_1 = executor.submit(task)
    task_2 = executor.submit(task)
    # task_1
    # task_2

if __name__ == "__main__":
    main()