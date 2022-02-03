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
	def cached_f(*args):
		if args in saved:
			return cached_f(*args)
		result = f(*args)
		saved[args] = result
		return result
	
	return cached_f



if __name__ == '__main__':
	
	@timed
	def expensive_f(sec=0):
		print(f'Sleeping for {sec} second(s) ...')
		time.sleep(sec)
	# expensive_f = timed(expensive_f)
	
	expensive_f(1)
