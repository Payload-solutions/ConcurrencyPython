import threading
import time

def thread_worker():
    # it is only at the point where the thread starts executing
    # that it's state goes from 'Runnable' to 'Running'
    # state
    print("My Thread has entered the 'Running' State")
    # if we call the time.sleep() method then our thread 
    # goes into a not-runnable state. We can do no further work
    # on this particular thread
    time.sleep(10)
    # thread then completes its tasks and terminates
    print("My Thread is terminating")


# At this poit in time, the thread has no state
# it hasn't been allocated any system resources
my_thread = threading.Thread(target = thread_worker)
# when we call my_thread to run and then calls the thread's
# run method. It goes from 'Starting' state to 'Runnable' but not running
my_thread.start()
# Here we join the thread and then this method is called
# our thread goes into a 'Dead' state. =t has finished the job
# that it was intended to do.
my_thread.join()
print("My Thread has entered a 'Dead' state")