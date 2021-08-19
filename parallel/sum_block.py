import multiprocessing
import numpy as np
import threading

class Sum: # again, this class is from ParallelPython's example code (I modified for an array and added comments)
    def __init__(self):
        self.value = np.zeros((1,512*512)) #this is the initialization of the sum
        self.lock = threading.Thread.allocate_lock()
        self.count = 0

    def add(self,value):
        self.count += 1
        self.lock.acquire() # lock so sum is correct if two processes return at same time
        self.value += value # the actual summation
        self.lock.release()

def computation(index):
    array1 = np.ones((1,512*512))*index #this is where the array-returning computation goes
    return array1

def summers(num_iters):
    pool = multiprocessing.Pool(processes=8)

    sumArr = Sum() # create an instance of callback class and zero the sum
    for index in range(num_iters):
        singlepoolresult = pool.apply_async(computation,(index,),callback=sumArr.add)

    pool.close()
    pool.join() #waits for all the processes to finish

    return sumArr.value


def summers(num_iters):
    pool = multiprocessing.Pool(processes=8)

    outputArr = np.zeros((num_iters,1,512*512)) # you wouldn't have to initialize these
    sumArr = np.zeros((1,512*512))              # but I do to make sure I have the memory

    outputArr = np.array(pool.map(computation, range(num_iters)))
    sumArr = outputArr.sum(0)

    pool.close() # not sure if this is still needed since map waits for all iterations

    return sumArr