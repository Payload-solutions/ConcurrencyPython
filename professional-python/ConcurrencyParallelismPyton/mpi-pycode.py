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




def main():
    pass

if __name__ == "__main__":
    main()
