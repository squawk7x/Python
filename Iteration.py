"""

Checked builtin types which are containers:

(isinstance(object, collections.Container) returns True)

- Containers which have a __contains__ method defined:
    All builtin sequence types: Lists, bytearrays, strings, unicode strings and tuples,
    dictionaries.
    All builtin set types: sets and frozensets

- Containers which do not have a __contains__ method defined:
    xrange objects
    lambda expressions


sequence:

An iterable which supports efficient element access using integer indices via the
__getitem__() special method and defines a
__len__() method that returns the length of the sequence.

"""


T = 1, 2, 3
T
# (1, 2, 3)

dir(T)
# __contains__   T is container
# __getitem__    T is iterable / Sequence support
# __iter__      T is iterable / Iteration support
# NO __next__

T.__iter__()
# <tuple_iterator object at 0x7fc07c156790>

"""

iter(...)
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

Get an iterator from an object. In the first form, the argument must supply its own iterator, or be a sequence.
In the second form, the callable is called until it returns the sentinel.

"""

iter
# <built-in function iter>

dir(iter)
# NO __iter__
# NO __next__


it = iter(T)
it
# <tuple_iterator object at 0x7fc098162fd0>

dir(it)
# __iter__       # every iterator is also iterable!
# __next__

it.__next__()
# 1

it.__next__()
# 2

next
# <built-in function next>

"""
Signature: next(iterator[, default])
next(iterator[, default])

Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.

"""

next(it, "leider schon am Ende")
# 3

next(it, "leider schon am Ende")
# "leider schon am Ende"

# funktioniert wiederholt

"""
A container object (such as a list) produces a fresh new iterator each time you pass it to the iter() function or use it in a for loop.
"""
for i in T:
	print(i)

"""
Attempting this with an iterator will just return the same exhausted iterator object used in the previous iteration pass, making it appear like an empty container.
"""

it = iter(T)  # every iterator is also iterable!
# funktioniert nur 1x
for i in it:
	print(i)

##


"""
Signature: map(func, *iterables) --> map object
map(func, *iterables) --> map object

Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.
"""


def myfunc(value):
	return value ** 2


mymap = map(myfunc, range(11))

while True:
	print(next(mymap))
	print(mymap.__next__())







