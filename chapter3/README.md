In the previous example we can explain how can interact the process
using the join() method

In our main function we've defined two threads, the first we aptly call
thread 1 and pass in a value of 1. As it sole argument

## Putting it together.

while the join method may be very useful and
provide you with a quick and clean way of ensuring
order within our code, it's also very important to
note that you could, potentially, undo all the gains
we've made by making our code multithreaded in the
first place.

## Locks.

Locks are an essential mechanism when trying to access
shared resources from multiple threads of execution.
The best way to picture this is to imagine you have
one bathroom and multiple flat mates--when you want to
freshen up or take the bathroom at the same time.

A lock in Python is a synchronization primitive that 
allows us to essentially lock our bathroom door. It
can be in either a "locked" or "unlocked" state,
and we can only acquire a lock while it's in an 
"unlocked" state.