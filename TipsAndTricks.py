'''
Strings

'''

name = 'Python'
print(f'Hello {name} {[1, 2, 3]}')

'''
Unpacking

'''

dic = {'a': 1, 'b': 2}
x, y = dic
print(x, y)
x, y = dic.values()
print(x, y)
x, y = dic.items()
print(x, y)

'''
Multiple Assignment / Values Swap

'''
x, y = 1, 2

# swaping values
x, y = y, x

'''
Comprehensions

'''
x = [[0 for _ in range(5)] for _ in range(5)]
print(x)
# _ (underscore is used as variable, which is not used later

sentence = 'Count how often appear my chars'
x = {char: sentence.count(char) for char in set(sentence)}
print(x)

'''
Inline / Ternary Condition

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
Sort by key

'''

lst = [[1,2], [3,4], [4,2],[-1,3],[4,5],[2,3]]
lst.sort() # by first element, no Python function for 2nd element -> lamda
print(lst)
lst.sort(key=lambda x:x[1])
print(lst)

def sort_func(x):
	return x[0] + x[1]

lst.sort(key=sort_func)
print(lst)

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
with open('text.txt', 'r') as f:
	file_contents = f.read()

'''
Indexes

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
Unpacking Values

'''
a, b = (1, 2)
print(a)
# print(b)
a, _ = (1, 2)
print(a)
a, b, c = (1, 2)  # Error
a, b, c = (1, 2, 3, 4, 5)  # Error
a, b, *_ = (1, 2, 3, 4, 5)
print(a)
print(b)
# print(c)
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
print(c)
print(d)

'''
Assigning Attributes

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
Argument Evaluation

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
LEGB - Local, Enclosing, Global, Built-in
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

# ------------------------------------------------

print("this module's name: {}".format(__name__))


def main():
	print('main()')


if __name__ == '__main__':
	main()

# ------------------------------------------------

try:
	f = open('testfile.txt')
	if f.name == 'currupt_file.txt':
		raise Exception
except FileNotFoundError as e:
	print(e)
except Exception as e:
	print(e)
else:
	print(f.read())
	f.close()
finally:
	print("Executing finally...")

# ------------------------------------------------
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

# ------------------------------------------------
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

HTTP METHODS:
GET
PUT
(POST is not)
DELETE

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
GENERATOR

'''


def fib(num):
	a, b = 0, 1
	for i in range(1, num + 1):
		yield '{}: {}'.format(i, a)
		a, b = b, a + b


for item in fib(10):
	print(item)
