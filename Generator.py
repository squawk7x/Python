"""

The ``yield`` expression is used when defining a generator function or an asynchronous generator function and thus can only be used in the body of a function definition. Using a yield expression in a function’s body causes that function to be a generator, and using it in an ``async def`` function’s body causes that coroutine function to be an asynchronous generator.

"""


# A simple generator function

def my_gen():
	n = 1
	print('This is printed first')
	# Generator function contains yield statements
	yield n
	
	n += 1
	print('This is printed second')
	yield n
	
	n += 1
	print('This is printed at last')
	yield n


a = my_gen()

# <generator object my_gen at 0x7fc07c1585f0>
next(a)
# This is printed first
# 1
a.__next__()
# This is printed second
# 2
next(a)
# This is printed at last
# 3
a.__next__()
# Traceback (most recent call last): File "<console>", line 1, in <module> StopIteration

a = my_gen()
# Using for loop
for item in my_gen():
	print(item)

a = my_gen()
# Using for loop
for item in a:
	print(item)


# This is printed first
# 1
# This is printed second
# 2
# This is printed at last
# 3


def rev_str(my_str):
	length = len(my_str)
	for i in range(length - 1, -1, -1):
		yield my_str[i]


# For loop to reverse the string
for char in rev_str("hello"):
	print(char)

# Initialize the list

my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x ** 2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator = (x ** 2 for x in my_list)

print(list_)
# [1, 9, 36, 100]
print(generator)
# <generator object <genexpr> at 0x7fc07c1585f0>


# Initialize the list

my_list = [1, 3, 6, 10]

a = (x ** 2 for x in my_list)

print(next(a))
print(next(a))
print(next(a))
print(next(a))
next(a)

# 1
# 9
# 36
# 100
# Traceback (most recent call last):File "/home/andreas/Generator.py", line 100, in <module>next(a) StopIteration


# Generator expressions can be used as function
# arguments. When used in such a way, the round
# parentheses can be dropped.

sum(x ** 2 for x in my_list)
# 146

max(x ** 2 for x in my_list)


# 100

# mit iterator class:

class PowTwo:
	def __init__(self, max=0):
		self.n = 0
		self.max = max
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.n > self.max:
			raise StopIteration
		
		result = 2 ** self.n
		self.n += 1
		return result


it = PowTwo(11)
next(it)


# mit generator function:

def PowTwoGen(max=0):
	n = 0
	while n < max:
		yield 2 ** n
		n += 1


gen = PowTwoGen(11)
next(gen)


# Represent Infinite Stream by Lazyness

def all_even():
	n = 0
	while True:
		yield n
		n += 2


ae = all_even()
next(ae)


# Pipelining Generators

def fibonacci_numbers(nums):
	x, y = 0, 1
	for _ in range(nums):
		x, y = y, x + y
		yield x


def square(nums):
	for num in nums:
		yield num ** 2


print(sum(square(fibonacci_numbers(10))))
