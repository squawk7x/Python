# ------------------------------------------------
'''
THREADS
useful for I/O bound tasks (vs CPU bound tasks -> multiprocessing
manual way

'''

import time

start = time.perf_counter()


def do_something():
	print('Sleeping 1 second...')
	time.sleep(1)
	print('Done sleeping')


do_something()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# ------------------------------------------------

import time, threading

start = time.perf_counter()


def do_something():
	print('Sleeping 1 second...')
	time.sleep(1)
	print('Done sleeping')


t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)

t1.start()
t2.start()
t1.join()
t2.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# ------------------------------------------------

import time, threading

start = time.perf_counter()


def do_something():
	print('Sleeping 1 second...')
	time.sleep(1)
	print('Done sleeping')


threads = []

for _ in range(10):
	t = threading.Thread(target=do_something)
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# ------------------------------------------------

import time, threading

start = time.perf_counter()


def do_something(seconds):
	print(f'Sleeping {seconds} second...')
	time.sleep(seconds)
	print('Done sleeping')


threads = []

for _ in range(10):
	t = threading.Thread(target=do_something, args=[1.5])
	t.start()
	threads.append(t)

for thread in threads:
	thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# ------------------------------------------------

'''
THREADS
Thread pool executor

'''

import time, concurrent.futures

start = time.perf_counter()


def do_something(seconds):
	print(f'Sleeping {seconds} second...')
	time.sleep(seconds)
	return f'Done sleeping in {seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
	# results = [executor.submit(do_something, 1) for _ in range(10)]
	
	# using a list
	secs = [5, 4, 3, 2, 1]
	results = [executor.submit(do_something, sec) for sec in secs]
	
	for f in concurrent.futures.as_completed(results):
		print(f.result())

# f1 = executor.submit(do_something, 1)
# f2 = executor.submit(do_something, 1)
# print (f1.result())
# print (f2.result())


finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# ------------------------------------------------


import time, concurrent.futures

start = time.perf_counter()


def do_something(seconds):
	print(f'Sleeping {seconds} second...')
	time.sleep(seconds)
	return f'Done sleeping in {seconds}'


with concurrent.futures.ThreadPoolExecutor() as executor:
	# results = [executor.submit(do_something, 1) for _ in range(10)]
	
	secs = [5, 4, 3, 2, 1]
	
	results = executor.map(do_something, secs)
	for result in results:
		print(result)
	# order returned as they started



finish = time.perf_counter()

print(f'Finished in {round(finish - start, 2)} second(s)')

# ------------------------------------------------