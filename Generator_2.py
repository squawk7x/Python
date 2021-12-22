'''
GENERATORS

yield -> generator function

'''


def f():
	return 1
	return 2
	return 3


print(f())  # 1


def g():
	yield 1
	yield 2
	yield 3


print(g())  # <generator object g at 0x7f0ce1e616d0>

for x in g():
	print(x)

# ---------------------------------------------------------------

import string


def letters():
	for c in string.ascii_lowercase:
		yield c


for letter in letters():
	print(letter)

# ---------------------------------------------------------------

import itertools
def prime_numbers():
	'''yields prime numbers'''
	
	# Handle the first prime
	yield 2
	prime_cache = [2]
	
	# Loop over positive, odd integers
	for n in itertools.count(3, 2):
		is_prime = True
		
		# Check if any prime number divides n
		for p in prime_cache:
			if n % 5 == 0 or n % p == 0:
				is_prime = False
				break
				
		# Is it a prime?
	
		if is_prime:
			prime_cache.append(n)
			yield n
			
for p in prime_numbers():
	print(p)
	if p > 100:
		break

# ---------------------------------------------------------------

'''
GENERATOR EXPRESSIONS

List Comprehension: [ expression ]
Generator Expressions: ( expression )

'''

import itertools

squares = (x**2 for x in itertools.count(1))

for x in squares:
	print(x)
	
	if x > 500:
		squares.close()
		
'''
A "Tuple Comprehension" does NOT return a tuple, but a GENERATOR

'''

import itertools

squares = (x**2 for x in itertools.count(1))

print(type(squares))  # <class 'generator'>

'''
What is the "cost" of this generator?

'''

import itertools
import sys

squares = (x**2 for x in itertools.count(1))

print(sys.getsizeof(squares))  # 112 Bytes

'''A List comprehension would cost an infinite number of Bytes'''
