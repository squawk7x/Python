# AN INFORMAL INTRODUCTION TO PYTHON

# 3.1.2 Strings

#print('C:\some\name')  # here \n means newline!
# C:\some
# ame
print(r'C:\some\name')  # raw string: note the r before the quote
# C:\some\name

print("""\
Usage: thingy [OPTIONS]
-h                          Display this usage message
-H hostname                 Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'
# 'unununium'

'Py' 'thon'
# 'Python'

text = ('Put several strings within parentheses '
        'to have them joined together.')

text
# 'Put several strings within parentheses to have them joined together.'

word = 'Python'

word[:]
# 'Python'
word[1:5]
# 'ytho'
word[-1]
# 'n'
# word[0] = 'J'
# TypeError: 'str' object does not support item assignment

word.__add__('A')
word.__dir__()
word.__getitem__(5)  # 'n'
word.__len__()  # 6
len(word)  # 6
word.__sizeof__()  # 55
word.__str__()  # 'Python'

# 3.1.3 Lists

squares = [1, 4, 9, 16, 25]
squares
# [1, 4, 9, 16, 25]
squares[:]
# [1, 4, 9, 16, 25]
squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 64  # replace the wrong value

cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes
[1, 8, 27, 64, 125, 216, 343]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
# ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = []
letters
# ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
# []

letters = ['a', 'b', 'c', 'd']
len(letters)
# 4

letters.extend(['e', 'f'])
letters
# ['a', 'b', 'c', 'd', 'e', 'f']
letters.reverse()
# ['f', 'e', 'd', 'c', 'b', 'a']

# nested list
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
# [['a', 'b', 'c'], [1, 2, 3]]
x[0]
# ['a', 'b', 'c']
x[0][1]
# 'b'


# 3.2 First Steps Towards Programming

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
	print(a)
	a, b = b, a + b

print()

a, b = 0, 1
while a < 100:
	print(a, end=',')
	a, b = b, a + b

i = 256 * 256
print('The value of i is', i)
# The value of i is 65536


# 4 MORE CONTROL FLOW TOOLS

# 4.1 if Statements

# x = int(input("Please enter an integer: "))
x = 42

if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

print()

# 4.2 for Statements

# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))
# cat 3
# window 6
# defenestrate 12


# 4.3 The range() Function

for i in range(5):
	print(i)

list(range(5, 10))
# [5, 6, 7, 8, 9]
list(range(0, 10, 3))
# [0, 3, 6, 9]
list(range(-10, -100, -30))
# [-10, -40, -70]

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
	print(i, a[i])

sum(range(4), 100)  # 0 + 1 + 2 + 3
# 106


# 4.4 break and continue Statements, and else Clauses on Loops

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n // x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
	print("Found an odd number", num)

# 4.5 pass Statements

while True:
	pass  # Busy-wait for keyboard interrupt (Ctrl+C)


class MyEmptyClass:
	pass


def initlog(*args):
	pass  # Remember to implement this!


# 4.6 Defining Functions

def fib(n):  ## write Fibonacci series up to n
	"""Print a Fibonacci series up to n."""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()


fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

fib
# <function fib at 0x7f42bc621e50>

f = fib
f(100)
# 0 1 1 2 3 5 8 13 21 34 55 89

fib(0)
print(fib(0))
# None

print(fib(10))


# 0 1 1 2 3 5 8
# None


def fib2(n):  # return Fibonacci series up to n
	"""Return a list containing the Fibonacci series up to n."""
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result


f100 = fib2(100)
print(f100)


# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# 4.7 More on Defining Functions

def ask_ok(prompt, retries=4, reminder='Please try again!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)


ask_ok('Do you really want to quit?')
ask_ok('OK to overwrite the file?', 2)
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

"""
The default values are evaluated at the point of function definition in the defining scope
"""

i = 5


def f(arg=i):
	print(arg)


i = 6

f()
# 5


"""
Important warning:
The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:

"""


def f(a, L=[]):
	L.append(a)
	return L


print(f(1))
print(f(2))
print(f(3))


# [1]
# [1, 2]
# [1, 2, 3]


def f(a, L=None):
	if L is None:
		L = []
	L.append(a)
	return L


print(f(1))
print(f(2))
print(f(3))


# [1]
# [2]
# [3]


# 4.7.2 Keyword Arguments

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.")
	print("-- Lovely plumage, the", type)
	print("-- It's", state, "!")


parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


def cheeseshop(kind, *arguments, **keywords):
	print("-- Do you have any", kind, "?")
	print("-- I'm sorry, we're all out of", kind)
	for arg in arguments:
		print(arg)
	print("-" * 40)
	for kw in keywords:
		print(kw, ":", keywords[kw])


cheeseshop(
	"Limburger",
	"It's very runny, sir.", "It's really very, VERY runny, sir.",
	shopkeeper="Michael Palin",
	client="John Cleese",
	sketch="Cheese Shop Sketch")

# -- Do you have any Limburger ?
# -- I'm sorry, we're all out of Limburger
# It's very runny, sir.
# It's really very, VERY runny, sir.
# ----------------------------------------
# shopkeeper : Michael Palin
# client : John Cleese
# sketch : Cheese Shop Sketch


# 4.7.3 Special parameters

"""

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      ----------     ----------     ----------
          |              |              |
          |      Positional or keyword  |
          |                             |
    Positional only                Keyword only

"""


def standard_arg(arg):
	print(arg)


def pos_only_arg(arg, /):
	print(arg)


def kwd_only_arg(*, arg):
	print(arg)


def combined_example(pos_only, /, standard, *, kwd_only):
	print(pos_only, standard, kwd_only)


standard_arg(2)
# 2
standard_arg(arg=2)
# 2

pos_only_arg(1)
# 1
pos_only_arg(arg=1)
# TypeError: pos_only_arg()

kwd_only_arg(3)
# TypeError: kwd_only_arg()
kwd_only_arg(arg=3)
# 3

combined_example(1, 2, 3)
# TypeError: combined_example() takes 2 positional arguments but 3 were given
combined_example(1, 2, kwd_only=3)
# 1 2 3
combined_example(1, standard=2, kwd_only=3)
# 1 2 3
combined_example(pos_only=1, standard=2, kwd_only=3)


# TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

def foo(name, **kwds):
	return 'name' in kwds


foo(1, **{'name': 2})


# TypeError: foo() got multiple values for argument 'name'

def foo(name, /, **kwds):
	return 'name' in kwds


foo(1, **{'name': 2})
# True


"""
Recap:

(Keyword parameters are also referred to as named parameters)

def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):

"""


# 4.7.4 Arbitrary Argument Lists

def write_multiple_items(file, separator, *args):
	file.write(separator.join(args))


def concat(*args, sep="/"):
	return sep.join(args)


concat("earth", "mars", "venus")
# 'earth/mars/venus'
concat("earth", "mars", "venus", sep=".")
# 'earth.mars.venus'


# 4.7.5 Unpacking Argument Lists

list(range(3, 6))
# [3, 4, 5]

args = [3, 6]
list(range(*args))
# [3, 4, 5]

list(range(args))
# TypeError: 'list' object cannot be interpreted as an integer

a = [1, 2, 3]
print(*a)


# 1 2 3


def parrot(voltage, state='a stiff', action='voom'):
	print("-- This parrot wouldn't", action, end=' ')
	print("if you put", voltage, "volts through it.", end=' ')
	print("E's", state, "!")


42
43
42
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# 4.7.6 Lambda Expressions

def make_incrementor(n):
	return lambda x: x + n


f = make_incrementor(42)

print(f(0))
print(f(1))
print(f(0))

# 42
# 43
# 42


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

pairs.sort(key=lambda pair: pair[1], reverse=False)

print(pairs)

mypairs = [('A', 1), ('C', 3), ('B', 2)]


def mytest():
	return lambda pair: pair[1]


mt = mytest()

print(mt(mypairs))
print(mt(mypairs[1]))
print(mt(mypairs[2]))


# 4.7.7 Documentation Strings

def my_function():
	"""Do nothing, but document it.

	No, really, it doesn't do anything.
	"""


pass

print(my_function.__doc__)


# 4.7.8 Function Annotations

# parameter annotations
#       parameter name: expression
# return annotation
#          -> expression

def f(ham: str, eggs: str = 'eggs') -> str:
	print("Annotations:", f.__annotations__)
	print("Arguments:", ham, eggs)
	
	return ham + ' and ' + eggs


f('spam')

# Intermezzo: Coding Style


# 5 DATA STRUCTURES

# 5.1 More on Lists

# LIFO

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting at position 4

fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()

# 5.1.1 Using Lists as Stacks

stack = [3, 4, 5]

stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop()
stack.pop()
print(stack)

# 5.1.2 Using Lists as Queues

# FIFO (list has bad performance -> deque)

from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

# 5.1.3 List Comprehensions

squares = []

for x in range(10):
	squares.append(x ** 2)

print(squares)
# x still exists

# or without side-effects:
squares = list(map(lambda x: x ** 2, range(10)))

# or:
squares = [x ** 2 for x in range(10)]

[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print()

combs = []
for x in [1, 2, 3]:
	for y in [3, 1, 4]:
		if x != y:
			combs.append((x, y))

print(combs)

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
[x * 2 for x in vec]
# [-8, -4, 0, 4, 8]
# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# [0, 2, 4]
# apply a function to all the elements
[abs(x) for x in vec]
# [4, 2, 0, 2, 4]
# call a method on each element
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
[weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit']
# create a list of 2-tuples like (number, square)
[(x, x ** 2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
# the tuple must be parenthesized, otherwise an error is raised


vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]

from math import pi

print([str(round(pi, i)) for i in range(1, 6)])

# 5.1.4 Nested List Comprehensions

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
]

# matrix'
[[row[i] for row in matrix] for i in range(4)]

# or like this:
transposed = []

for i in range(4):
	transposed.append([row[i] for row in matrix])

print(transposed)

transposed = []
for i in range(4):
	# the following 3 lines implement the nested listcomp
	transposed_row = []
	for row in matrix:
		transposed_row.append(row[i])
	transposed.append(transposed_row)

print(transposed)

matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12]
]

# Transposed matrix'
list(zip(*matrix))

# see help(zip)
list(zip('abcdefg', range(3), range(9)))
# [('a', 0, 0), ('b', 1, 1), ('c', 2, 2)]


# 5.2 The del statement

a = [-1, 1, 66.25, 333, 333, 1234.5]

del a[0]
print(a)
del a[2:4]
print(a)
del a[:]
print(a)
del a

# 5.3 Tuples and Sequencies

t = 12345, 54321, 'hello!'
t[0]
# 12345

t
# (12345, 54321, 'hello!')

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# Tuples are immutable:
# t[0] = 88888


# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v

empty = ()
singleton = 'hello',  # <-- note trailing comma
len(empty)
# 0
len(singleton)
# 1
singleton
# ('hello',)

# unpacking possible:
# x, y, z = t


# 5.4 Sets

# Note: to create an empty set you have to use set(), not {};

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)  # show that duplicates have been removed

# {'orange', 'banana', 'pear', 'apple'}

'orange' in basket
# True
'crabgrass' in basket
# False

a = set('abracadabra')
b = set('alacazam')

a
a - b
a | b
a & b
a ^ b  # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc'}

# 5.5 Dictionaries

# indexed by keys
# key:value
# {} creates empty dictionary

tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127

tel
# {'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
# 4098
del tel['sape']
tel['irv'] = 4127
tel
# {'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
# ['jack', 'guido', 'irv']
sorted(tel)
# ['guido', 'irv', 'jack']
'guido' in tel
# True
'jack' not in tel
# False


# Constructor
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

{x: x ** 2 for x in (2, 4, 6)}

# 
dict(sape=4139, guido=4127, jack=4098)

# 5.6 Looping Techniques

# looping through dictionaries:

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
	print(k, v)

# looping through sequence:

for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

# combining with zip() function:

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
	print('What is your {0}? It is {1}.'.format(q, a))

# reversed sequence:

for i in reversed(range(1, 10, 2)):
	print(i)

# sorted order (source stays unaltered)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

list(basket)

for f in sorted(list(basket)):
	print(f)

for f in sorted(set(basket)):
	print(f)

list(basket)

import math

raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

filtered_data = []

for value in raw_data:
	if not math.isnan(value):
		filtered_data.append(value)

print(filtered_data)

# 5.7 More on Conditions

a, b, c = 1, 2, 2

print(a < b == c)
# True

# priorities:
# A and not B or C is equivalent to (A and (not B)) or C

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

# 5.8 Compairing Sequencies and Other Types

(1, 2, 3) < (1, 2, 4)  # True
[1, 2, 3] < [1, 2, 4]  # True
'ABC' < 'C' < 'Pascal' < 'Python'  # True
(1, 2, 3, 4) < (1, 2, 4)  # True
(1, 2) < (1, 2, -1)  # True
(1, 2, 3) == (1.0, 2.0, 3.0)  # True
(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)  # True

# MODULES

import Fibonacci

# from fibo import *
# from fibo import fib, fib2

fibo.fib(1000)

fibo.fib2(100)

# 6.1 More on Modules

import Fibonacci

from Fibonacci import *  # This imports all names except those beginning with an underscore (_)

from Fibonacci import fib, fib2

import Fibonacci as fib

from Fibonacci import fib as fibonacci

# changes in module -> importlib.reload(modulename)

# 6.1.1 Executing modules as scripts

# adding this code at the end of your module

"""
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
"""

# 6.2 Standard Modules

import sys

print(sys.ps1)
print(sys.ps2)

# The dir() Function

dir(fibo)
dir(builtins)

# 6.4 Packages

"""
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
"""

"""
from . import echo
from .. import formats
from ..filters import equalizer
"""

# INPUT AND OUTPUT

# 7.1 Fancier Output Formatting

year = 2016;
event = 'Referendum'

f'Results of the {year} {event}'

yes_votes = 42_572_654;
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)

'{:-9} YES votes {:2.2%}'.format(yes_votes, percentage)

s = 'Hello, world.'
str(s)
# 'Hello, world.'

repr(s)
# "'Hello, world.'"

str(1 / 7)
# '0.14285714285714285'

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
# The value of x is 32.5, and y is 40000...

# The repr() of a string adds string quotes and backslashes:
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
# 'hello, world\n'

# The argument to repr() may be any Python object:
repr((x, y, ('spam', 'eggs')))
# "(32.5, 40000, ('spam', 'eggs'))"


# 7.1.1 Formatted String Literals

import math

print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

for name, phone in table.items():
	print(f'{name:10} ==> {phone:10d}')

animals = 'eels'

print(f'My hovercraft is full of {animals}.')
# My hovercraft is full of eels.

print('My hovercraft is full of {animals !r}.')
# My hovercraft is full of 'eels'


# 7.1.2 The String format() Method

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
# We are the knights who say "Ni!"

print('{0} and {1}'.format('spam', 'eggs'))
# spam and eggs
print('{1} and {0}'.format('spam', 'eggs'))
# eggs and spam


print('This {food} is {adjective}.'.format(
	food='spam', adjective='absolutely horrible'))
# This spam is absolutely horrible.

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
                                                   other='Georg'))
# The story of Bill, Manfred, and Georg.


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}

print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
# Jack: 4098; Sjoerd: 4127; Dcab: 8637678

for x in range(1, 11):
	print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# 7.1.3 Manual String Formatting

for x in range(1, 11):
	print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
	# Note use of 'end' on previous line
	print(repr(x * x * x).rjust(4))

'12'.zfill(5)
# '00012'
'-3.14'.zfill(7)
# '-003.14'
'3.14159265359'.zfill(5)
# '3.14159265359'


# 7.1.4 Old string formatting

import math

print('The value of pi is approximately %5.3f.' % math.pi)
# The value of pi is approximately 3.142.


# 7.2 Reading and Writing Files

f = open('workfile', 'r')
f.close()

with open('workfile') as f:  # 'with' automatically closes file after use !!! See page 67
	read_data = f.read()
f.closed
# True

f = open('workfile', 'r')
for line in f:
	print(line, end='')
f.closed

f = open('workfile', 'r')
list(f)
f.closed

f = open('workfile3', 'x')
f.write('This is a test\n')
f.closed

f.read

# 7.2.1 Methods of File Objects

f = open('workfile', 'r')
f.read()
f.read()
f.close()

f = open('workfile', 'r')
f.readline()
f.close()

f = open('workfile', 'r')
for line in f:
	print(line, end='')
f.close()

f = open('workfile2', 'w')
f.write('This is a test\n')
value = ('the answer', 42)
s = str(value)  # convert the tuple to string
f.write(s)
f.close()

f = open('workfile2', 'r')
f.tell()  # zeigt aktuelle postion in der Datei
# 0
f.readline()
f.tell()
# 15
f.close()
# To change the file object’s position, use f.seek(offset, from_what)

f = open('workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)  # Go to the 6th byte in the file
# 5
f.read(1)
# b'5'
f.seek(-3, 2)  # Go to the 3rd byte before the end
# 13
f.read(1)
# b'd'
f.close()

# 7.2.2 Saving structured data with json

import json

json.dumps([1, 'simple', 'list'])
# '[1, "simple", "list"]'

x = [1, 2, 4, 9]

f = open('workfilejason', 'w')
json.dump(x, f)
f.close()

f = open('workfilejason', 'r')
y = json.load(f)
f.close()

list(y)

# ERRORS AND EXCEPTIONS

# 8.1 Syntax Errors

while True:
	print('Hello world')

# 8.2 Exceptions

# 10 * (1/0)

# 4 + spam*3

# '2' + 2


# 8.3 Handling Exceptions

while True:
	try:
		x = list[input("Please enter a number: ")]
		break
	except ValueError:
		print("Oops! That was no valid number. Try again...")


#    except (RuntimeError, TypeError, NameError):
# pass


class B(Exception):
	pass


class C(B):
	pass


class D(C):
	pass


for cls in [B, C, D]:
	try:
		raise cls()
	except D:
		print("D")
	except C:
		print("C")
	except B:
		print("B")


class B(Exception):
	pass


class C(B):
	pass


class D(C):
	pass


for cls in [B, C, D]:
	try:
		raise cls()
	except B:
		print("B")
	except C:
		print("C")
	except D:
		print("D")

import sys

try:
	f = open('myfile.txt')
	s = f.readline()
	i = int(s.strip())
except OSError as err:
	print("OS error: {0}".format(err))
except ValueError:
	print("Could not convert data to an integer.")
except:
	print("Unexpected error:", sys.exc_info()[0])
	raise

for arg in sys.argv[1:]:
	try:
		f = open(arg, 'r')
	except OSError:
		print('cannot open', arg)
	else:
		print(arg, 'has', len(f.readlines()), 'lines')
		f.close()

try:
	raise Exception('spam', 'eggs')
except Exception as inst:
	print(type(inst))  # the exception instance
	print(inst.args)  # arguments stored in .args
	print(inst)  # __str__ allows args to be printed directly, but may be overridden in exception subclasses
	x, y = inst.args  # unpack args
	print('x =', x)
	print('y =', y)


# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs

def this_fails():
	x = 1 / 0


try:
	this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)
# Handling run-time error: division by zero


# 8.4 Raising Exceptions

raise NameError('HiThere')

raise ValueError
# shorthand for 'raise ValueError()'

try:
	raise NameError('HiThere')
except NameError:
	print('An exception flew by!')
# raise


# An exception flew by!


# 8.5 User-defined Exceptions

class Error(Exception):
	"""Base class for exceptions in this module."""
	pass


class InputError(Error):
	"""Exception raised for errors in the input.
Attributes:
	expression -- input expression in which the error   occurred
	message -- explanation of the error
	"""


def __init__(self, expression, message):
	self.expression = expression
	self.message = message


class TransitionError(Error):
	"""Raised when an operation attempts a state transition    that's not allowed.

	Attributes:
		previous -- state at beginning of transition
		next -- attempted new state
		message -- explanation of why the specific transition is not allowed
	"""


def __init__(self, previous, next, message):
	self.previous = previous
	self.next = next
	self.message = message


# 8.6 Defining Clean-up Actions

try:
	raise KeyboardInterrupt

finally:
	print('Goodbye, world!')


# Goodbye, world!


def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print("result is", result)
	finally:
		print("executing finally clause")


divide(2, 1)
# result is 2.0
# executing finally clause
divide(2, 0)
# division by zero!
# executing finally clause
divide("2", "1")
# executing finally clause

# 8.7 Predefined Clean-up Actions

for line in open("myfile.txt"):
	print(line, end="")

with open("myfile.txt") as f:
	for line in f:
		print(line, end="")
	#  the context manager will ensure correct closing of the file upon exiting the ``with`` statement, even if an exception was raised.

# CLASSES

spam = "initial spam"


# 9.2.1 Scopes and Namespaces Example

def scope_test():
	spam = "test spam"
	
	def do_local():
		spam = "local spam"
	
	def do_nonlocal():
		nonlocal spam
		spam = "nonlocal spam"
	
	def do_global():
		global spam  # would be created global if not there
		spam = "global spam"
	
	do_local()
	print("After local assignment:", spam)
	
	do_nonlocal()
	print("After nonlocal assignment:", spam)
	
	do_global()
	print("After global assignment:", spam)


print("In global scope:", spam)
scope_test()
print("In global scope:", spam)

# In global scope: initial spam
# After local assignment: test spam
# After nonlocal assignment: nonlocal spam
# After global assignment: nonlocal spam
# In global scope: global spam


import Scopetest

spam = "initial spam"

print("In global scope:", spam)
scope_test()
print("In global scope:", spam)


# 9.3.2 Class Objects

class MyClass:
	"""A simple example class"""
	i = 12345
	
	def __init__(self):
		self.data = []
	
	def f(self):  # class function object
		return 'hello world'


x = MyClass()

print(x.i)

# ---------------------------------------
print(x.f())  # instance method object
# calling a method with a list of n arguments is equivalent to calling the corresponding function with an argument list that is created by inserting the method’s instance object before the first argument.
MyClass.f(x)
# ----------------------------------------

print(x.__dict__)
print(x.__doc__)

x.counter = 1  # creates new 'instance data attribute'
while x.counter < 10:
	x.counter = x.counter * 2

print(x.counter)
del x.counter  # removes it


class Complex:
	
	def __init__(self, realpart, imagpart):
		self.r = realpart
		self.i = imagpart


x = Complex(3.0, -4.5)
x.r, x.i


# (3.0, -4.5)


# 9.3.5 Class and Instance Variables


class Dog:
	kind = 'canine'  # class variable shared by all instances
	
	def __init__(self, name):
		self.name = name  # instance variable unique to each instance


d = Dog('Fido')
e = Dog('Buddy')

d.kind
# 'canine'  # shared by all dogs
e.kind
# 'canine'  # shared by all dogs
d.name
# 'Fido'    # unique to d
e.name


# 'Buddy'   # unique to e


class Dog:
	tricks = []  # mistaken use of a class variable
	
	def __init__(self, name):
		self.name = name
	
	def add_trick(self, trick):
		self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks  # unexpectedly shared by all dogs


# ['roll over', 'play dead']


class Dog:
	
	def __init__(self, name):
		self.name = name
		self.tricks = []  # creates a new empty list for each dog
	
	def add_trick(self, trick):
		self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks
# ['roll over']
e.tricks


# ['play dead']


# 9.4 Random Remarks

class Warehouse:
	purpose = 'storage'
	region = 'west'


w1 = Warehouse()
print(w1.purpose, w1.region)
# storage west
w2 = Warehouse()
w2.region = 'east'  # same attribute name -> instance name has priority
print(w2.purpose, w2.region)


# storage east


# Function defined outside the class

def f1(self, x, y):
	return min(x, x + y)


class C:
	f = f1
	
	def g(self):
		return 'hello world'
	
	h = g


class Bag:
	
	def __init__(self):
		self.data = []
	
	def add(self, x):
		self.data.append(x)
	
	def addtwice(self, x):
		self.add(x)
		self.add(x)


# 9.5 Inheritance

"""

class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>

class DerivedClassName(modname.BaseClassName):


"""


# own example:

class Top:
	order = 0
	
	def __init__(self):
		self.data = []
		self.name = "Top Class"
		self.order = 0


class Sub(Top):
	def __init__(self):
		self.name = "Sub Class"
		self.order = Top.order + 1


class Subber(Sub):
	def __init__(self):
		self.name = "Subber Class"
		self.order = Sub.order + 1


top = Top()
sub = Sub()
subber = Subber()

# issubclass(Subber,Top)
# True
# isinstance(top,Top)
# True


# 9.5.1 Multiple Inheritance

"""

class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>

"""


class Side(Top):
	def __init__(self):
		self.name = "Side Class"
		self.order = Top.order + 1


class Subside(Sub, Side):
	def __init__(self):
		self.name = "Subside Class"
		self.order = Top.order + 2


# 9.6 Private Variables

class Mapping:
	
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)
	
	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)
	
	__update = update  # private copy of original update() method


class MappingSubclass(Mapping):
	
	def update(self, keys, values):
		# provides new signature for update()
		# but does not break __init__()
		for item in zip(keys, values):
			self.items_list.append(item)


# 9.7 Odds and Ends

class Employee:
	pass


john = Employee()
# Create an empty employee record
# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

# 9.8 Iterators

for element in [1, 2, 3]:
	print(element)
for element in (1, 2, 3):
	print(element)
for key in {'one': 1, 'two': 2}:
	print(key)
for char in "123":
	print(char)
for line in open("workfile"):
	print(line, end='')

# for behind the lines: iteration

s = 'abc'
it = iter(s)
it
# <str_iterator object at 0x7f88b866e310>
next(it)
# 'a'
next(it)
# 'b'
next(it)
# 'c'
next(it)


# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# next(it)
# StopIteration


class Reverse:
	"""Iterator for looping over a sequence backwards."""
	
	def __init__(self, data):
		self.data = data
		self.index = len(data)
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]


rev = Reverse('spam')
iter(rev)
# <__main__.Reverse object at 0x00A1DB50>
for char in rev:
	print(char)


# m
# a
# p
# s


# 9.9 Generators

def reverse(data):
	for index in range(len(data) - 1, -1, -1):
		yield data[index]


for char in reverse('golf'):
	print(char)

# f
# l
# o
# g


# 9.10 Generator Expressions

sum(i * i for i in range(10))  # sum of squares
# 285

xvec = [10, 20, 30]
yvec = [7, 5, 3]

print(zip(xvec, yvec))
sum(x * y for x, y in zip(xvec, yvec))  # dot product
# 260

data = 'golf'
list(data[i] for i in range(len(data) - 1, -1, -1))
# ['f', 'l', 'o', 'g']


# 10.1 Operating System Interface

import os

os.getcwd()
# Return the current working directory
# 'C:\\Python39'

dir(os)
