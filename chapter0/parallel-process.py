#!/usr/bin/python3



from mpi4py import MPI



def start_process():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0:
        data = {"a":7, "b": 3.14}
        comm.send(data, dest=1, tag=11)
    elif rank == 1:
        data = comm.recv(source = 0, tag = 11)


def main():
    start_process()
    

if __name__ == "__main__":
    main()