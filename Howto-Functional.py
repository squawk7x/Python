# 2 Iterators

L = [1, 2, 3]
it = iter(L)
t = tuple(it)
t

L = [1, 2, 3]
iterator = iter(L)
a, b, c = iterator
a, b, c  # (1, 2, 3)

max(iter(L))

m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
     'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}

for key in m:
	print(key, m[key])

L = [('Italy', 'Rome'), ('France', 'Paris'), ('US', 'Washington DC')]
dict(iter(L))  # {'Italy': 'Rome', 'France': 'Paris', 'US': 'Washington DC'}

all = {1: 'eins', 2: 'zwei'}
for x, y in all.items():
	print(x)

# 3 Generator expressions and list comprehensions

# Generator expressions are surrounded by parentheses (“()”)
# List comprehensions are surrounded by square brackets (“[]”)
line_list = ['  line 1\n', 'line 2\n']
# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)
stripped_iter
# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
stripped_list


# 4 Generators

def generate_ints(N):
	for i in range(N):
		yield i


gen = generate_ints(10)
next(gen)

a, b, c = generate_ints(3)
a, b, c  # (0, 1, 2)


# 4.1 Passing values into a generator
# yield became an expression since Python 2.5


def counter(maximum):
	i = 0
	while i < maximum:
		val = (yield i)
	# If value provided, change counter
	if val is not None:
		i = val
	else:
		i += 1


it = counter(10)
next(it)
next(it)
it.send(8)
next(it)
next(it)


# 5 Built-in functions

# map(func, *iterables) --> map object
def upper(s):
	return s.upper()


list(map(upper, ['sentence', 'fragment']))
[upper(s) for s in ['sentence', 'fragment']]


# filter(function or None, iterable) --> filter object
def is_even(x):
	return (x % 2) == 0


list(filter(is_even, range(10)))
list(x for x in range(10) if is_even(x))

# enumerate
for item in enumerate(['subject', 'verb', 'object']):
	print(item)

# sorted(iterable, key=None, reverse=False)
import random

# Generate 8 random numbers between [0, 10000)
rand_list = random.sample(range(10000), 8)
rand_list
sorted(rand_list)
sorted(rand_list, reverse=True)

# any(iter) / all(iter)
any([0, 0, 0])
any([0, 1, 0])
all([0, 1, 1])
all([1, 1, 1])

# zip(iterA, iterB, ...)
list(zip(['a', 'b', 'c'], (1, 2, 3)))
list(zip(['a', 'b'], (1, 2, 3)))

# 6 The itertools module
# 6.1 Creating new iterators

import itertools
import os

itertools.count()
itertools.count(10)
itertools.count(10, 5)
itertools.cycle([1, 2, 3, 4, 5])
itertools.repeat('abc', 5)
itertools.chain(['a', 'b', 'c'], (1, 2, 3))
itertools.islice(range(10), 2, 8, 2)
itertools.tee(itertools.count())

# 6.2 Calling functions on elements
itertools.starmap(os.path.join,
                  [('/bin', 'python'), ('/usr', 'bin', 'java'),
                   ('/usr', 'bin', 'perl'), ('/usr', 'bin', 'ruby')])

# 6.3 Selecting elements

itertools.filterfalse(is_even, itertools.count())


def less_than_10(x):
	return x < 10


itertools.takewhile(less_than_10, itertools.count())
itertools.dropwhile(less_than_10, itertools.count())
itertools.dropwhile(is_even, itertools.count())
itertools.compress([1, 2, 3, 4, 5], [True, True, False, False, True])

# 6.4 Combinatoric functions
tuple(itertools.combinations([1, 2, 3, 4, 5], 2))
tuple(itertools.permutations([1, 2, 3, 4, 5], 2))
tuple(itertools.combinations_with_replacement([1, 2, 3, 4, 5], 2))

# 6.5 Grouping elements

city_list = [('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL'),
             ('Anchorage', 'AK'), ('Nome', 'AK'),
             ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ'),
             ]


def get_state(city_state):
	return city_state[1]


itertools.groupby(city_list, get_state)
('AL', ('Decatur', 'AL'), ('Huntsville', 'AL'), ('Selma', 'AL')),
('AK', ('Anchorage', 'AK'), ('Nome', 'AK')),
('AZ', ('Flagstaff', 'AZ'), ('Phoenix', 'AZ'), ('Tucson', 'AZ')),

# 7 The functools module

...

# 8 Small functions and the lambda expression

import functools

functools.reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
