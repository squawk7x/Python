# Fibonacci numbers module


def fib(n):
	'''writes Fibonacci series up to n'''
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()


def fib2(n):
	'''returns Fibonacci series up to n'''
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result


def fib3(n):
	'''returns n-th value of fibonacci serie'''
	a, b = 0, 1
	for _ in range(2, n + 2):
		a, b = b, a + b
	return b


def fibonacci(n):
	"""returns n-th value of fibonacci serie
	Recursion: fibonacci (n) is slowing down with greater n"""
	if n == 1:
		return 0
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n - 1) + fibonacci(n - 2)


'''
MEMOIZATION

'''

fibonacci_cache = {1: 1, 2: 2}


def fibonacci2(n):
	"""returns n-th value of fibonacci serie
	cached Recursion fibonacci (n)"""
	
	# If n cached, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		value = fibonacci2(n - 1) + fibonacci2(n - 2)
	
	# Cache the value
	fibonacci_cache[n] = value
	# return value
	return value


'''
FUNCTOOLS

LRU - LEAST RECENTLY USED
'''

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci3(n):
	"""returns n-th value of fibonacci serie
	LRU-cached Recursion fibonacci (n)"""
	
	# Check that the input is a positive integer
	if type(n) != int:
		raise TypeError('n must be a positive integer')
	if n < 1:
		raise ValueError('n must be a positive integer')
	
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		value = fibonacci2(n - 1) + fibonacci2(n - 2)
	
	# Cache the value
	fibonacci_cache[n] = value
	# return value
	return value


n = 50
print(f'fibonacci3({n}): {fibonacci3(n)}')

for n in range(1, 10):
	print(fibonacci3(n + 1) / fibonacci3(n))

# append this to make the module usable as a script:
'''
if __name__ == "__main__":
	import sys
	
	fib(int(sys.argv[1]))
'''
