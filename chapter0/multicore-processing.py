#!/usr/bin/python3



"""
Pag: 99

In multi-core processors contain multiple independent processing units or "cores".
Each core contains everything it needs in order to execute a sequence of stored
instructions. These cores each follow their own cycle, which consistes of the following
processes:
    Fetch: This step invpñvers fetching instructions from the program memory.
    This is deictated by a program counter(PC), which identifies the location 
    of the next step to execute.

    Decode: The core convets the instructions that it has just fetched, and converts it into
    a series of signals that will trigger variou other parts of the CPU.

    Excute: Finally, we perform the execute step. This is where we run the instrucion that
    we have just fethced and decoded, and the results of this execution are then stored
    in a CPU register.
"""


