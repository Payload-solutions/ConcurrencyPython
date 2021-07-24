#!/usr/bin/pyhon3


import os

def child():
    print("We are in the child process with PID = %d"%os.getpid())


def parent():
    print("We are in the parend process with PID= %d"%os.getpid())

    new_reference = os.getpid()
    if new_reference == 0:
        child()
    else:
        print("We are in the parent proess and our child process has PID= %s"%new_reference)

parent()
