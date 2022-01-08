
# ------------------------------------------------------------
# ------------------------------------------------------------
# Function argument unpacking

def myfunc(x, y, z):
	print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)
#1, 0, 1

myfunc(**dict_vec)
#1, 0, 1
# ------------------------------------------------------------

# The standard string repr for dicts is hard to read:

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
#{'b': 42, 'c': 12648430. 'a': 23}


# The "json" module can do a much better job:

import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))

#{
#	"a": 23,
#	"b": 42,
#	"c": 12648430
#}


# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
json.dumps({all: 'yup'})
#TypeError: keys must be a string

# ------------------------------------------------------------

# The get() method on dicts
# and its "default" argument

name_for_userid = {
	382: "Alice",
	590: "Bob",
	951: "Dilbert",
}


def greeting(userid):
	return "Hi %s!" % name_for_userid.get(userid, "there")


greeting(382)
# "Hi Alice!"

greeting(333333)
# "Hi there!"

# ------------------------------------------------------------

# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator

sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# ------------------------------------------------------------

# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
	print('passed')

if 1 in (x, y, z):
	print('passed')

# These only test for truthiness:
if x or y or z:
	print('passed')

if any((x, y, z)):
	print('passed')

# ------------------------------------------------------------

# How to merge two dictionaries
# in Python 3.5+

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
z
# {'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
z = dict(x, **y)
z
# {'a': 1, 'c': 4, 'b': 3}

# In these examples, Python merges dictionary keys
# in the order listed in the expression, overwriting
# duplicates from left to right.
#
# See: https://www.youtube.com/watch?v=Duexw08KaC8
# ------------------------------------------------------------
# ------------------------------------------------------------
