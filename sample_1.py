from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(comm.size)
print("comm: ", comm.Get_name())
print("rank: ", rank)
if rank == 0:
    data = {'key1' : [7, 2.72, 2+3j],
            'key2' : ( 'abc', 'xyz')}
else:
    data = None
data = comm.bcast(data, root=0)
print(data)