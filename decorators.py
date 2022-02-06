from functools import wraps
import time


def timed(f):
	
	@wraps(f)
	def timed_f(*args, **kwargs):
		start = time.perf_counter()
		value = f(*args, **kwargs)
		elapsed = time.perf_counter() - start
		print(f'time consumed: {elapsed} second(s)')
		return value
	
	return timed_f


def cached(f):
	saved = {}
	
	@wraps(f)
	def cached_f(*args, **kwargs):
		if args in saved:
			return saved[args]
		result = f(*args, **kwargs)
		saved[args] = result
		return result
	
	return cached_f


def logged(f):
	
	@wraps(f)
	def logged_f(*args, **kwargs):
		value = f(*args, **kwargs)
		with open('logfile.txt', 'a+') as file:
			f_name = f.__name__
			print(f"{f_name} returned value {value}")
			file.write(f"{f_name} returned value {value}")
		return value
	
	return logged_f


if __name__ == '__main__':
	
	@timed
	def expensive_f(sec=0):
		print(f'Sleeping for {sec} second(s) ...')
		time.sleep(sec)
	
	expensive_f(1)
	
	@cached
	def fibonacci(n):
		if n == 1:
			return 1
		elif n == 2:
			return 1
		elif n > 2:
			return fibonacci(n - 2) + fibonacci(n - 1)
	
	
	# Try with and without decorator @cached
	for n in range(10):
		print(f'{n}: {fibonacci(n)}')
	
	
	@logged
	def add(x, y):
		return x + y
	
	
	print(add(10, 20))
