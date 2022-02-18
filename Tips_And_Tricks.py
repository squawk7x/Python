'''
PYDOC

python -m pydoc <name>
python -m pydoc -k <keyword>
python -m pydoc -p 345 -> localhost:345
python -m pydoc -b -> The best!
python -m pydoc -w <name> -> create own documentation od <name>

'''
import socket

'''
INTERACTIVE HELP

'''
dir()
dir(__builtins__)
help(pow)

'''
DOCSTRINGS

'''


def empty_func():
	"""empty function"""
	pass


help(empty_func)


def myexpo(num1, num2):
	'''
	This function takes one number to the power of another number
	
	:param num1: This is the base
	:param num2: This is the exponent
	:return: The result num1 ** num2
	'''

	return num1 ** num2


print(myexpo(8, 2))

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
DICTIONARY

** keywords argument operator: passes a dict into another dict

'''

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 7, 'c': 4}

# dict1.update(dict2)
dict3 = dict1 | dict2
print(dict3)

# unpredictable 'b':
dict4 = dict(dict1.items() | dict2.items())
print(dict4)

dict5 = {**dict1, **dict2}
print(dict5)

'''
ZIP / UNZIP

'''

names = ('Mike', 'Bob', 'Anna')
ages = (20, 23, 27)

zipped = list(zip(names, ages))
print(zipped)
# [('Mike', 20), ('Bob', 23), ('Anna', 27)]

names, ages = zip(*zipped)
print(names)
print(ages)

# connect lists via zip
letters = ['b', 'd', 'a', 'c']
numbers = [3, 2, 4, 1]

data = sorted(zip(letters, numbers))
print(data)
# [('a', 4), ('b', 3), ('c', 1), ('d', 2)]

data = sorted(zip(numbers, letters))
print(data)
# [(1, 'c'), (2, 'd'), (3, 'b'), (4, 'a')]

letters, numbers = zip(*data)
print(letters)
print(numbers)

letters = ['b', 'd', 'a', 'c']
numbers = [3, 2, 4, 1]
# 2 list into dict
mydict = dict(zip(letters, numbers))
print(mydict)

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

list(map(lambda x: x ** 2, (1, 2, 3, 4, 5)))

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

string_plus = """I'm text
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

# swapping values
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
age = 20

adult = True if age >= 18 else False
print('You are an adult!' if adult else 'You are not an adult!')

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
lst.sort()  # by first element, no Python function for 2nd element -> lambda
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

data = [{'name': 'Max', 'age': 6}, {'name': 'Lisa', 'age': 20},
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
# also other resources (threads, databases, ...)
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

list(enumerate(enumerate(
	['a', 'b', 'c'])))  # [(0, (0, 'a')), (1, (1, 'b')), (2, (2, 'c'))]

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


class Person:
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

# ------------------------------------------------

'''
ENCAPSULATION

'''


class Person:

	def __init__(self, name, age, gender):
		self.__name = name
		self.__age = age
		self.__gender = gender

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, name):
		self.__name = name

	@staticmethod  # works without any object, no self!
	def mymethod():
		print('Hello World')


Person.mymethod()  # works in class directly

p1 = Person('Mike', 20, 'm')

print(p1.name)
p1.mymethod()  # but call by instance works as well

'''
TYPE HINTING

'''
import mypy  # -> restrictive


def myfunction(myparameter: int) -> str:
	# without mypy  :int works like comment, not restrictive
	return myparameter


myfunction('Hello World')

'''
FACTORY DESIGN PATTERN / OOP

'''

from abc import ABCMeta, abstractmethod


class IPerson(metaclass=ABCMeta):

	@abstractmethod
	def person_method(self):
		""" Interface Method """

	@abstractmethod
	def print_data(self):
		""" Implement child class """  # see singleton


class Student(IPerson):

	def __init__(self):
		self.name = 'Basic Student Name'

	def person_method(self):
		print('I am a student')


class Teacher(IPerson):

	def __init__(self):
		self.name = 'Basic Teacher Name'

	def person_method(self):
		print('I am a teacher')


class PersonFactory:

	@staticmethod
	def build_person(person_type):
		if person_type == 'Student':
			return Student()
		if person_type == 'Teacher':
			return Teacher()

		print('Invalid Type')
		return -1


if __name__ == '__main__':
	choice = input('What type of person to create?\n')
	person = PersonFactory.build_person(choice)
	person.person_method()

'''
PROXY DESIGN PATTERN / OOP

'''


# from abc import ABCMeta, abstractmethod

class Person(IPerson):
	def person_method(self):
		print('I am a person')


class ProxyPerson(IPerson):  # Proxy Middleman class

	def __init__(self):
		self.person = Person()

	def person_method(self):
		print('I am the proxy functionality')
		self.person.person_method()


p1 = Person()
p1.person_method()

p2 = ProxyPerson()
p2.person_method()

'''
SINGLETON DESIGN PATTERN / OOP

a class has only one instance = singleton

'''


# from abc import ABCMeta, abstractmethod

class PersonSingleton(IPerson):
	__instance = None  # singleton instance

	def person_method(self):
		print('I am a singleton')

	@staticmethod
	def get_instance():
		if PersonSingleton.__instance == None:
			PersonSingleton('Default Name', 0)
		return PersonSingleton.__instance

	def __init__(self, name, age):
		if PersonSingleton.__instance is not None:
			raise Exception('Singleton cannot be instantiated more than once')
		else:
			self.name = name
			self.age = age
			PersonSingleton.__instance = self

	@staticmethod
	def print_data():
		print(f'Name: {PersonSingleton.__instance.name}, Age: '
		      f'{PersonSingleton.__instance.age}')


p1 = PersonSingleton('Mike', 30)
print(p1)
p1.print_data()

p2 = PersonSingleton('Mike', 30)
print(p2)
p2.print_data()
# Exception: Singleton cannot be instantiated more than once


'''
COMPOSITE DESIGN PATTERN / OOP


'''


class IDepartment(metaclass=ABCMeta):

	@abstractmethod
	def __init__(self, employees):
		""" implement in child class """

	@abstractmethod
	def print_department(self):
		""" implement in child class """


class Accounting(IDepartment):

	def __init__(self, employees):
		self.employees = employees

	def print_department(self):
		print(f'Accounting Department: {self.employees}')


class Development(IDepartment):

	def __init__(self, employees):
		self.employees = employees

	def print_department(self):
		print(f'Development Department: {self.employees}')


class ParentDepartment(IDepartment):

	def __init__(self, employees):
		self.employees = employees
		self.base_employees = employees
		self.sub_depts = []

	def add(self, dept):
		self.sub_depts.append(dept)
		self.employees += dept.employees

	def print_department(self):
		print(f'Parent Department: {self.employees}')

		for dept in self.sub_depts:
			dept.print_department()

		print(f'Total number of employees: {self.employees}')


dept1 = Accounting(200)
dept2 = Development(170)

parent_dept = ParentDepartment(30)
parent_dept.add(dept1)
parent_dept.add(dept2)

parent_dept.print_department()
# ------------------------------------------------


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

x = 'Global x'


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


def outer_function(msg):
	def inner_function():
		print(msg)

	return inner_function()


hi_func = outer_function('Hi')
bye_func = outer_function('Bye')

hi_func()
bye_func()

'''
DECORATORS

'''


def decorator_function(original_function):
	def wrapper_function(*args, **kwargs):
		print('wrapper executed this before {}'.format(
			original_function.__name__))
		return original_function(*args, **kwargs)

	return wrapper_function


# without () waits until wrapper_function is executed

@decorator_function
def display():
	print('display function ran')


@decorator_function
def display_info(name, age):
	print('display_info runs with 2 arguments ({}, {}'.format(name, age))


# decorated_display = decorator_function(display)
# decorated_display()

display()
display_info('John', 25)


class decorator_class():

	def __init__(self, original_function):
		self.original_function = original_function

	def __call__(self, *args, **kwargs):
		print('call method executed this before {}'.format(
			self.original_function.__name__))
		return self.original_function(*args, **kwargs)


@decorator_class
def display():
	print('display function ran')


@decorator_class
def display_info(name, age):
	print('display_info runs with 2 arguments ({}, {})'.format(name, age))


display()
display_info('John', 25)

# ------------------------------------------------
# 3
from functools import wraps


# 2
def mapper(func):
	# 3
	@wraps(func)
	def inner(values):
		"""This is the inner()"""
		return [func(value) for value in values]

	return inner


@mapper
# 1
def camelcase(s: str):
	"""Turn strings_like_this into StringsLikeThis"""
	return ''.join([word.capitalize() for word in s.split('_')])


names = ['a_b', 'c_d', 'e_f']

print(camelcase(names))
print(camelcase.__doc__)
# This is the inner() -> functools
# after @wraps:
# Turn strings_like_this into StringsLikeThis

# ------------------------------------------------
# Caching decorator
# usable for pure functions (function has same result with same arguments)

from functools import wraps


def cache(func):
	saved = {}

	@wraps(func)
	def newfunc(*args):
		if args in saved:
			return newfunc(*args)
		result = func(*args)
		saved[args] = result
		return result

	return newfunc


# ------------------------------------------------
import random


def power_of(exponent):
	def decorator(func):
		def inner():
			return func() ** exponent

		return inner

	return decorator


@power_of(2)
def random_odd_digit():
	return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())

# ------------------------------------------------
import random


def power_of(arg):
	def decorator(func):
		def inner():
			return func() ** exponent

		return inner

	if callable(arg):
		exponent = 2
		return decorator(arg)
	else:
		exponent = arg
		return decorator


@power_of(2)
def random_odd_digit():
	return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())


# ------------------------------------------------

# class as decorator

class Elephant:

	def __init__(self, func):
		self._func = func
		self._memory = []

	def __call__(self):  # make elephant object instance callable
		retval = self._func()
		self._memory.append(retval)
		return retval

	def memory(self):
		return self._memory


@Elephant
def random_odd_digit():
	return random.choice([1, 3, 5, 7, 9])


print(random_odd_digit())
print(random_odd_digit.memory())
print(random_odd_digit())
print(random_odd_digit.memory())

'''
PROPERTY

'''


class Employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last

	# self.email = first + '.' + last + '@email.com'

	@property
	def email(self):
		return '{}.{}@email.com'.format(self.first, self.last)

	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	@fullname.setter
	def fullname(self, fn):
		first, last = fn.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None


emp_1 = Employee('John', 'Smith')
print(emp_1.fullname)
# print(emp_1.fullname()) -> @property: print(emp_1.fullname)
print(emp_1.email)

emp_1.first = 'Jim'
print(emp_1.first)
# John.Smith@email.com
# print(emp_1.email()) -> @property: print(emp_1.email
print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Corey Schafer'
print(emp_1.fullname)
print(emp_1.email)

del (emp_1.fullname)

# ------------------------------------------------
'''
MUTABLE / IMMUTABLE

'''
# Strings are immutable

a = 'Corey'
print(a)
print('Address of a is: {}'.format(id(a)))

a = 'John'
print(a)
print('Address of a is: {}'.format(id(a)))  # different address

a[0] = 'c'  # TypeError

# List is mutable

a = [1, 2, 3, 4, 5]
print(a)
print('Address of a is: {}'.format(id(a)))

a[0] = 6
print(a)
print('Address of a is: {}'.format(id(a)))  # same address

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

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n - 2) + fibonacci(n - 1)


for n in range(100):
	print(f'{n}: {fibonacci(n)}')
	print(f'ratio:', fibonacci(n) / fibonacci(n - 1))

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
greeting = 'I am {age} years old and my name is {name}'.format(name=name,
                                                               age=age)
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

import sys


def mygenerator(n):
	for x in range(n):
		yield x ** 3


values = mygenerator(1_000_000)
print(sys.getsizeof(values))

print(next(values))
print(next(values))
print(next(values))


def infinite_sequence():
	result = 1
	while True:
		yield result
		result *= 5


values = infinite_sequence()

print(next(values))
print(next(values))
print(next(values))
# ------------------------------------------------

'''
REGULAR EXPRESSIONS

'''
import re

text_to_search = 'abc deFGH IJ01 23456789 ._'

pattern = re.compile(r'\bI')

matches = pattern.finditer(text_to_search)
# matches = pattern.findall(text_to_search)

for match in matches:
	print(match)

'''
MULTIPROCESSING

'''

import time

NUMBERS = 50000, 50001, 50002, 50003


def factorial(n):
	""" great for multiprocessing:

	- CPU bound
	- referentially transparent n -> f(n)

	"""

	print('start: factorial({})'.format(n))
	f = 1
	for i in range(1, n + 1):
		f *= i
	print('done: factorial({})'.format(n))
	return f


# t0 = time.time()
# result = []
# for n in NUMBERS:
# 	result.append(factorial(n))
# t1 = time.time()
# print('Execution took {:.4f}'.format(t1 - t0))
#
# t0 = time.time()
# result = list(map(factorial, NUMBERS))
# t1 = time.time()
# print('Execution took {:.4f}'.format(t1 - t0))

import multiprocessing as mp

t0 = time.time()
with mp.Pool() as pool:
	result = pool.map(factorial, NUMBERS)
t1 = time.time()
print('Execution took {:.4f}'.format(t1 - t0))

'''
Raymond Hettinger
	Profi Tips

'''

import os
import threading

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# 1
for i in range(len(colors)):
	print(colors[i])
# 2
print(sorted(colors, key=len))
# 3
for i in range(len(colors) - 1, -1, -1):
	print(colors[i])
# 4
for color in reversed(colors):
	print(color)
# 5
for i in range(len(colors)):
	print(i, '-->', colors[i])
# 6
for i, color in enumerate(colors):
	print(i, '-->', colors[i])
# 7
n = min(len(names), len(colors))
for i in range(n):
	print(names[i], '-->', colors[i])
# 8
for name, color in zip(names, colors):
	print(name, '-->', color)
# 9
for color in sorted(colors, reverse=True):
	print(color)
# 10
print(sorted(colors, key=len))

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# 11
print(d)
for k in d:
	print(k)
# 12
# for k in d.keys():
#	if k.startswith('r'):
#		del d[k]
# 13
for k in d:
	print(k, '-->', d[k])
# 14
for k, v in d.items():
	print(k, '-->', v)

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# 15
d = dict(zip(names, colors))
print(d)

colors = ['red', 'green', 'blue', 'yellow', 'red', 'green', 'blue', 'red']
# 16 Counting in dictionaries
d = {}
for color in colors:
	if color not in d:
		d[color] = 0
	d[color] += 1
print(d)
# 17
d = {}
for color in colors:
	d[color] = d.get(color, 0) + 1

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa']

# 18
from collections import defaultdict

d = defaultdict(int)
for color in colors:
	d[color] += 1

# 19 Grouping in dictionaries
d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)
print(d)

# 20
d = {}
for name in names:
	key = len(name)
	d.setdefault(key, []).append(name)
print(d)

# 21
d = defaultdict(list)
for name in names:
	key = len(name)
	d[key].append(name)

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

# 22
while d:
	key, value = d.popitem()
	print(key, '-->', value)


# 22 Updating multiple state variables

def fibonacci(n):
	x, y = 0, 1
	for i in range(n):
		print(x)
		x, y = y, x + y


fibonacci(10)

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa']

# 23 Concatenating Strings
s = names[0]
for name in names:
	s += ', ' + name
print(s)

# 24
print(', '.join(names))

# Updating sequences

# 25
del names[0]
names.pop(0)
names.insert(0, 'mark')

# 26
from collections import deque

names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa'])

del names[0]
names.popleft()
names.appendleft('mark')

# Caching decorator
# usable for pure functions (function has same result with same arguments)

# 27
from functools import wraps


def cache(func):
	saved = {}

	@wraps(func)
	def newfunc(*args):
		if args in saved:
			return newfunc(*args)
		result = func(*args)
		saved[args] = result
		return result

	return newfunc


# How to use locks
# make a lock:
lock = threading.Lock

# old way to use a lock:
lock.acquire()
try:
	print('critical section')
finally:
	lock.release()

# new way:
with lock:
	print('critical section')

# Factor out temporary contexts

# old way:
try:
	os.remove('somefile.tmp')
except OSError:
	pass

# new way:
# with ignored(OSError):
# os.remove('somefile.tmp')

# ------------------------------------------------
'''
CONTEXT MANAGER

'''


def file_open(filename):
	f = open(filename, 'w')
	f.write('hello\n')  # Eception here, the file will never be closed!
	f.close()


def file_open_better(filename):
	with open(filename, 'w') as f:
		f.write('hello\n')


def try_finally(host, port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		s.connect((host, port))
		s.sendall(b'Hello')
	finally:
		s.close()


def try_finally_better(host, port):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((host, port))
		s.sendall(b'Hello')


'''
WALRUS OPERATOR :=

'''

print(x := 123)

print([y for x in range(10) if (y := x ** 2) % 2 == 0])

while (name := input('Enter your name: ')) != 'exit':
	print('Hello', name)

'''
ALTERNATIVE CONSTRUCTOR

'''

print(dict.fromkeys(['raymond', 'rachel', 'matthew']))

'''
Raymond Hettinger
	Summary: Toolset for New-Style Classes

1. Inherit from object() // old
2. Instance variables: 
	for information unique to an instance
3. Class variables: 
	for data shared among all instances
4. Regular methods: 
	need 
		'self' 
	to operate on instance data
5. Class methods: 
	implement alternative constructors. They need 
		'cls'
	so they can create subclass instances as well.
6. Static methods: 
	attach functions to classes. 
	They don't need 'self' or 'cls'.
	Static methods improve discoverability and require context to be specified.
7. A propoerty(): // old
    lets getter and setter methods invoked automatically by attribute access.
    This allows Python classes to freely expose their instance variables.
8. The __slots__ variable
	implements the Flyweight Design Pattern by suppressinginstance dictionaries
	
	
'''

'''
Raymond Hettinger
	The Art of Subclassing
	
	InstDict1   --->
	InstDict2   --->    SubClassDict   ---> ParClassDict
	InstDict3   --->
	
	A Subclass delegates work to another class
	A Subclass and its parents are just two different dictionaries that contain functions
	A Subclass points to its parent
	The pointer means: 'I delegate work to this class'

	Classes are dictionaries of functions
	Subclasses point to other dictionaries to reuse their code
	The Subclasses are in complete control of what happens
	
	LISKOV SUBSTTUTION PRINCIPLE:
	"If S is a subtype of T, then objects of type T 
	may be replaced with objects of type S" 
	
		-> POLYMORPHISM & SUBSTITUTABILITY

'''

'''
Raymond Hettinger
	super considered super
	
	Linearisation:
	
	MRO Method Resolution Order
	super in Python does not call parents, 
	but parents from the children
	super means "next in line", starting from youngest child
	
	!!!
	-> children get called before their parents
	-> parents get called in the order listed
	-> parents stay in order
	!!!
	-> multiple inheritance: use keyword arguments
		(you can not know who you are calling)
	
'''


class A:
	pass


class B(A):
	pass


class C(B):
	pass


class D(C, B):
	pass


help(D)

'''
Raymond Hettinger
	Namespaces
	
'''

d = dict()
d['raymond'] = 'red'
d['raymond']

x = 10
globals()['x']
print(x)

globals()['x'] = 11
print(x)

from types import SimpleNamespace

ns = SimpleNamespace(x=99, y=100)
print(ns)

print(ns.x)
print(ns.y)

#  dict()   globals()   SimpleNamespace
#  d['x']      x            ns.x

# emulate dictionaries

n = 8

# karr
karr = [[] for i in range(n)]
varr = [[] for i in range(n)]

print(n)
print(karr)
print(varr)

key, value = 'raymond', 'red'
i = hash(key) % n
print(i)

karr[i].append(key)
varr[i].append(value)

print(karr)
print(varr)

# [[], [], ['raymond'], [], [], [], [], []]
# [[], [], ['red'], [], [], [], [], []]
