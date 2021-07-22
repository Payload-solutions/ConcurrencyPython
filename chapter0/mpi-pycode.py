#!/usr/bin/python3

from mpi4py import MPI

"""Import the respective module and initialize MPI
do computing using MPI communications between process and 
shut down MPI
"""

def object_communicator():

    """This object is the communicator. It's methods will be used
    to carry out communications between processes."""
    comm = MPI.COMM_WORLD



def first_implementation():
    comm = MPI.COMM_WORLD
    my_rank = comm.Get_rank()
    p = comm.Get_size()

    if my_rank != 0:
        message = "Hello world from %s"%str(my_rank)
        comm.send(message, dest = 0)
    else:
        for procid in range(1, p):
            message = comm.recv(source = procid)
            print("Process 0 receives message for process {}:{}".format(procid, message))



def main():
    first_implementation()

if __name__ == "__main__":
    main()
