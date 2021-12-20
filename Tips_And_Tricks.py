'''
PYDOC

python -m pydoc <name>
python -m pydoc -k <keyword>
python -m pydoc -p 345 -> localhost:345
python -m pydoc -b -> The best!
python -m pydoc -w <name> -> create own documentation od <name>

'''

'''
INTERACTIVE HELP

'''
dir()
dir(__builtins__)
help(pow)


def empty_func():
	"""empty function"""
	pass


help(empty_func)

'''
DATETIME

'''

import datetime

dir(datetime)  # date, time, datetime

gvr = datetime.date(1956, 1, 31)
print(gvr)
print(gvr.strftime('%A, %B %d, %Y'))

message = 'GVR was born on {:%A, %B %d, %Y}.'
print(message.format(gvr))

'''
UNDERSCORE '_'

'''

# console: returns last output
# usable as variable which is never used

for _ in range(3):
	print("Hello")

'''
SETS

'''

example = {1, 'A', 'Hello'}
example.remove(1)
example.remove(2)  # KeyError: 2
example.discard(2)  # no KeyError: 2 message / silent

'''
DICTIONARY

item = key: value

'''

messages = {'one': 1, 'two': 2, 'three': 3}

messages.keys()  # dict_keys(['one', 'two', 'three'])
messages.values()  # dict_values([1, 2, 3])
messages.items()  # dict_items([('one', 1), ('two', 2), ('three', 3)])

for key in messages:
	print(key, '-->', messages.get(key))

for key in messages.keys():
	value = messages[key]
	print(key, '-->', value)

for key, value in messages.items():
	print(key, '-->', value)

'''
LIST <--> TUPLE

add         --
remove      --
change      --

mutable  immutable
		made quickly

'''

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tuple_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(f'List methods ({len(dir(list_numbers))}):')
print(dir(list_numbers))

print(f'Tuple methods ({len(dir(tuple_numbers))}):')
print(dir(tuple_numbers))

''' Lists occupy more memory than Tuples'''
import sys

print(dir(sys))  # 'getsizeof'
print(help(sys.getsizeof))  # Return the size of object in bytes.

print(f'list_numbers: {sys.getsizeof(list_numbers)} bytes')
print(f'tuple_numbers: {sys.getsizeof(tuple_numbers)} bytes')

'''Tuples can be made more quickly'''
import timeit

list_test = timeit.timeit(stmt="[1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="(1, 2, 3, 4, 5)", number=1000000)
print("List time: ", list_test)
print("Tuple time: ", tuple_test)
print(80 * "-")

'''
FUNCTIONS

'''


def f():
	pass


f  # <function __main__.f()>

'''
LAMBDA FUNCTION

'''

lambda x: 3 * x + 1  # Out[9]: <function __main__.<lambda>(x)>
g = lambda x: 3 * x + 1
g(5)

full_name = lambda fn, ln: fn.strip().title() + ' ' + ln.strip().title()
full_name("   leonhard ", "EULER")


def build_quadratic_function(a, b, c):
	'''Returns the function f(x) = ax^2 + bx +c'''
	return lambda x: a * x ** 2 + b * x + c


build_quadratic_function(2, 3, -5)(2)

f = build_quadratic_function(2, 3, -5)
f(2)

'''
MAP FUNCTION

'''

# map(func, *iterables) --> map object

list(map(lambda _: _ ** 2, (1, 2, 3, 4, 5)))

'''
FILTER FUNCTION

'''

import statistics

data = (1.3, 2.7, 0.8, 4.1, 4.3, -0.1)
avg = statistics.mean(data)
list(filter(lambda x: x > avg, data))

data = ['', 'zwei', '', 'vier']
list(filter(None, data))  # ['zwei', 'vier']
# False: "", 0, 0.0, 0j, [], (),{}, False, None, empty instances


'''
STRINGS

'''

'I\'m text'
"""I'm text"""
'''I'm text too'''

name = 'Python'
print(f'Hello {name} {[1, 2, 3]}')

string_plus = """I'm
	in "several" lines"""
print(string_plus)

'''
NUMBERS IN PYTHON3

	complex numbers
    floats
    (longs)
	ints

'''

int, float, complex

e = 2.7_1828_1828
type(e)  # float

c = 2 - 6.1j
type(c)  # complex
c.real
c.imag

hex(10)  # '0xa' (output is a string)
0xa  # 10 (output is a int)
type(0xa)
5 + True  # 6

'''
UNPACKING

'''

dic = {'a': 1, 'b': 2}
x, y = dic
print(x, y)
x, y = dic.values()
print(x, y)
x, y = dic.items()
print(x, y)

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}

print(z)

'''
MULTIPLE ASSIGNMENT / VALUE SWAP

'''
x, y = 1, 2

# swaping values
x, y = y, x

'''
COMPREHENSIONS

'''
x = [[0 for _ in range(5)] for _ in range(5)]
print(x)
# _ (underscore is used as variable, which is not used later

sentence = 'Count how often appear my chars'
x = {char: sentence.count(char) for char in set(sentence)}
print(x)

'''
TERNARY CONDITION (INLINE CONDITION)

'''

x = 1 if 2 > 3 else 0

'''
for else & while else

'''

search = [1, 2, 3, 4, 5, 6, 7]
target = 7  # 8

for element in search:
	if element == target:
		print('found')
		break
else:
	print('not found')

'''
SORT BY KEY

'''

lst = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]
lst.sort()  # by first element, no Python function for 2nd element -> lamda
print(lst)
lst.sort(key=lambda x: x[1])
print(lst)


def sort_func(x):
	return x[0] + x[1]


lst.sort(key=sort_func)
print(lst)

'''
SORTING

dict by value
'''


# How to sort a Python dict by value
# (== get a representation sorted by value)

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:

import operator
sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]


# -------------------------------------------------

data = [{'name': 'Max', 'age': 6},
        {'name': 'Lisa', 'age': 20},
        {'name': 'Ben', 'age': 9}]

# sort by name:

sorted_data = sorted(data, key=lambda x: x['age'])
print(sorted_data)

'''
if else

'''

condition = True
x = 1 if condition else 0
print(x)

# large numbers
num1 = 100_000_000_000
num2 = 10_000_000
total = num1 + num2
print(f'{total:,}')

# manually close file
f = open('test.txt', 'r')
file_contents = f.read()
f.close()

# automatic close file -> Contextmanager:
# also other ressources (threads, databases, ...)
with open('test.txt', 'r') as f:
	file_contents = f.read()

'''
INDEXES

'''

names = ['A', 'B', 'C', 'D']
index = 0
for name in names:
	print(index, name)
	index += 1
# better:
names = ['A', 'B', 'C', 'D']
for index, name in enumerate(names):
	print(index, name)
names = ['A', 'B', 'C', 'D']
heroes = ['W', 'X', 'Y', 'Z']
for index, name in enumerate(names):
	hero = heroes[index]
	print(f'{name} is actually {hero}')
# better with zip:
for name, hero in zip(names, heroes):
	print(f'{name} is actually {hero}')
universes = ['aaa', 'bbb', 'ccc', 'ddd']
for name, hero, universe in zip(names, heroes, universes):
	print(f'{name} is actually {hero} from {universe}')
for value in zip(names, heroes, universes):
	print(value)

'''
ENUMERATION

'''

list(enumerate(['a', 'b', 'c']))  # [(0, 'a'), (1, 'b'), (2, 'c')]

it = iter(enumerate(['a', 'b', 'c']))
next(it)

for i, item in enumerate(['a', 'b', 'c']):
	print(i, item)

list(enumerate(enumerate(['a', 'b', 'c'])))  # [(0, (0, 'a')), (1, (1, 'b')), (2, (2, 'c'))]

'''
UNPACKING

'''
a, b = (1, 2)
print(a)
# print(b)
a, _ = (1, 2)
print(a)
# a, b, c = (1, 2)  # Error
# a, b, c = (1, 2, 3, 4, 5)  # Error
a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)
# print(c)
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print(c)
print(d)

'''
ASSIGNING ATTRIBUTES

'''


class Person():
	pass


person = Person()
person.first = "A"
person.last = "O"

person = Person()
first_key = 'first'
first_val = 'A'
setattr(person, 'first', 'A')
setattr(person, first_key, first_val)
print(person.first)
first_val = getattr(person, first_key)
print(first_val)


class Person():
	pass


person = Person()
person_info = {'first': 'Corey', 'last': 'Schafer'}
for key, value in person_info.items():
	setattr(person, key, value)
for key in person_info.keys():
	print(getattr(person, key))

# input password
from getpass import getpass

username = input('Username: ')
password = getpass('Password: ')

# Konsole: python -m modulname

'''
ARGUMENT EVALUATION

Python evaluates default arguments only once
at the time the function is created and
not each time the function is called

'''


def add_name(name, name_list=[]):
	name_list.append(name)
	print(name_list)


add_name('A')  # ['A']
add_name('B')  # ['A', 'B']


def add_name2(name, name_list=None):
	if name_list is None:
		name_list = []
	name_list.append(name)
	print(name_list)


add_name2('A')  # ['A']
add_name2('B')  # ['B']

'''
SCOPE

LEGB -  Local, Enclosing, Global, Built-in
		Enclosing when using nested functions

'''


# x = 'Global x'

def test():
	global x
	x = 'local x'
	print(x)


test()
print(x)

import builtins

print(dir(builtins))

# -------------------------------------------------

x = 'global x'


def outer():
	x = 'outer x'
	
	def inner():
		nonlocal x
		x = 'inner x'
		print(x)
	
	inner()
	print(x)


outer()

'''
MAIN

'''

print("this module's name: {}".format(__name__))


def main():
	print('main()')


if __name__ == '__main__':
	main()

'''
EXCEPTIONS

'''

try:
	f = open('testfile.txt')
	if f.name == 'currupt_file.txt':
		raise Exception
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:  # if no exceptions in try block
	print(f.read())
	f.close()
finally:  # always executed
	print("Executing finally...")

'''
FIRST CLASS FUNCTION

'''


def square(x):
	return x * x


def cube(x):
	return x ** 3


f = square
f(5)


def my_map(func, arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result


my_map(square, [1, 2, 3, 4, 5])
my_map(cube, [1, 2, 3, 4, 5])

'''
CLOSURES

'''


def logger(msg):
	def log_message():
		print('Log:', msg)
	
	return log_message


log_hi = logger('Hi')
log_hi()


def html_tag(tag):
	def wrap_text(msg):
		print('<{0}>{1}</{0}>'.format(tag, msg))
	
	return wrap_text


print_h1 = html_tag('h1')
print(print_h1)  # <function html_tag.<locals>.wrap_text at 0x7f64ccc58820>

print_h1('Test Headline!')
print_h1('Another Headline!')

# ------------------------------------------------
'''
MUTABLE / IMMUTABLE

'''
# Strings are immutable

a = 'Corey'
print(a)
print('Adress of a is: {}'.format(id(a)))

a = 'John'
print(a)
print('Adress of a is: {}'.format(id(a)))  # different address

a[0] = 'c'  # TypeError

# List is mutable

a = [1, 2, 3, 4, 5]
print(a)
print('Adress of a is: {}'.format(id(a)))

a[0] = 6
print(a)
print('Adress of a is: {}'.format(id(a)))  # same address

# ------------------------------------------------

'''
MEMOIZATION

'''
import time

ef_cache = {}


def expensive_func(num):
	if num in ef_cache:
		print("from cache:")
		return ef_cache[num]
	print("Computing...")
	time.sleep(1)
	result = num * num
	ef_cache[num] = result
	return result


print(expensive_func(10))
print(expensive_func(4))
print(expensive_func(10))
print(expensive_func(4))

print(ef_cache)

# ------------------------------------------------

'''
COMBINATIONS & PERMUTATIONS

'''

import itertools

my_list = [1, 2, 3]

combinations = itertools.combinations(my_list, 2)
for c in combinations:
	print(c)

permutations = itertools.permutations(my_list, 3)
for p in permutations:
	print(p)

# ------------------------------------------------

my_list = [1, 2, 3, 4, 5, 6]
combinations = itertools.combinations(my_list, 3)
print([result for result in combinations if sum(result) == 10])

# ------------------------------------------------

word = 'sample'
my_letters = 'plmeas'

combinations = itertools.combinations(my_letters, 6)
permutations = itertools.permutations(my_letters, 6)

for p in permutations:
	print(p)
	if ''.join(p) == word:
		print('Match')
		break
	else:
		print('No Match')

# ------------------------------------------------

'''
IDEMPOTENCE

f(f(x)) = f(x)

'''

# f(x) = abs(x)

# f(f(x)) = f(x)

abs(abs(abs(-10))) == abs(-10)  # True

# ------------------------------------------------

'''
DRY- Don't repeat yourself
-> reducing repetition of information of all kinds

'''

# ------------------------------------------------
'''
STRING INTERPOLATION

'''

# String Concatenation:

name = 'Corey'
age = 28
# greeting = 'My name is ' + name + ' and I am ' + str(age) + ' years old'
# print(greeting)

# String Interpolation:
greeting = 'I am {age} years old and my name is {name}'.format(name=name, age=age)
print(greeting)

# ------------------------------------------------
'''
ITERATION

'''

my_dict = {'name': 'Bronx', 'age': '2', 'occupation': 'CoreyS Dog'}
for key, val in my_dict.items():  # iteritems()?
	print("My {} is {}".format(key, val))

# ------------------------------------------------
'''
GENERATORS

'''


def fib(num):
	a, b = 0, 1
	for i in range(1, num + 1):
		yield '{}: {}'.format(i, a)
		a, b = b, a + b


for item in fib(10):
	print(item)

