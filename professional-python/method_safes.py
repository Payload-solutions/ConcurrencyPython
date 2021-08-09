#!/usr/bin/python3

import multiprocessing
from random import randint
from threading import Lock
# def implementing_sum():

#     # 100 values
#     values = [randint(1, 100) for _ in range(10)]
#     print(values)


# def my_process():
#     print("Currently executing child  Process")
#     print("This process has it's own instance of the GIL")
#     print("Executing Main Process")
#     print("Creating child Process")


# def main():

#     elements = multiprocessing.Process(target=implementing_sum)
#     my_proc = multiprocessing.Process(target=my_process)
#     elements.start()
#     my_proc.start()

#     my_proc.join()
#     print("Child Process has terminated, terminating main process")

#     # elements.join()

# if __name__ == "__main__":
#     main()

def lock_class(methodnames, lockfactory):
    return lambda cls: make_threasafe(cls, methodnames, lockfactory)

def lock_method(method):
    if getattr(method, '__is_locked', False):
        raise TypeError("Method %r is already locked"%method)

def locked_method(self, *arg, **kwarg):
    with self._lock:
        return method(self, *arg, **kwarg)

    lock_method.__name__ = '%s(%s)'%('lock_method', method.__name__)
    lock_method.__is_locked = True
    return lock_method




def make_threasafe(cls, methodnames, lockfactory):
    init = cls.__init__
    def newinit(self, *arg, **kwarg):
        init(self, *arg, **kwarg)
        self._lock = lockfactory
    cls.__init__ = newinit

    for methodname in methodnames:
        oldmethod = getattr(cls, methodname)
        newmthod = lock_method(oldmethod)
        setattr(cls, methodname, newmthod)
    return cls


def lock(method):

    def new_method(self, *arg, **kwarg):
        with self._lock:
            return method(self, *arg, **kwarg)
    return new_method


class DecoratorLockedSet(set):
    def __init__(self, *arg, **kwarg) -> None:
        self._lock = Lock()
        super(DecoratorLockedSet, self).__init__(*args, **kwarg)

    @locked_method
    def add(self, *arg, **kwarg):
        return super(DecoratorLockedSet, self).add(elem)
    
    @locked_method
    def remove(self, *arg, **kwarg):
        return super(DecoratorLockedSet, self).remove(elem)

def main():
    pass


if __name__ == "__main__":
    main()