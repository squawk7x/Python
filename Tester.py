import os
import threading

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

#1
for i in range(len(colors)):
	print(colors[i])
#2
print(sorted(colors, key=len))
#3
for i in range(len(colors) - 1, -1, -1):
	print(colors[i])
#4
for color in reversed(colors):
	print(color)
#5
for i in range(len(colors)):
	print(i, '-->', colors[i])
#6
for i, color in enumerate(colors):
	print(i, '-->', colors[i])
#7
n = min(len(names), len(colors))
for i in range(n):
	print(names[i], '-->', colors[i])
#8
for name, color in zip(names, colors):
	print(name, '-->', color)
#9
for color in sorted(colors, reverse=True):
	print(color)
#10
print(sorted(colors, key=len))

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

#11
print(d)
for k in d:
	print(k)
#12
#for k in d.keys():
#	if k.startswith('r'):
#		del d[k]
#13
for k in d:
	print(k, '-->', d[k])
#14
for k, v in d.items():
	print(k, '-->', v)

names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

#15
d = dict(zip(names, colors))
print(d)

colors = ['red', 'green', 'blue', 'yellow', 'red', 'green', 'blue', 'red']
#16 Counting in dictionaries
d = {}
for color in colors:
	if color not in d:
		d[color] = 0
	d[color] += 1
print(d)
#17
d = {}
for color in colors:
	d[color] = d.get(color, 0) + 1

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa']

#18
from collections import defaultdict

d = defaultdict(int)
for color in colors:
	d[color] += 1

#19 Grouping in dictionaries
d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)
print(d)

#20
d = {}
for name in names:
	key = len(name)
	d.setdefault(key, []).append(name)
print(d)

#21
d = defaultdict(list)
for name in names:
	key = len(name)
	d[key].append(name)

d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

#22
while d:
	key, value = d.popitem()
	print(key, '-->', value)


#22 Updating multiple state variables

def fibonacci(n):
	x, y = 0, 1
	for i in range(n):
		print(x)
		x, y = y, x + y


fibonacci(10)

names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa']

#23 Concatenating Strings
s = names[0]
for name in names:
	s += ', ' + name
print(s)

#24
print(', '.join(names))

#Updating sequencies

#25
del names[0]
names.pop(0)
names.insert(0, 'mark')

#26
from collections import deque

names = deque(['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa'])

del names[0]
names.popleft()
names.appendleft('mark')

#Caching decorator
#usable for pure functions (function has same result with same arguments)

#27
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


#How to use locks
#make a lock:
lock = threading.Lock

#old way to use a lock:
lock.acquire()
try:
	print('critical section')
finally:
	lock.release()

#new way:
with lock:
	print('critical section')

#Factor out temporary contexts

#old way:
try:
	os.remove('somefile.tmp')
except OSError:
	pass

#new way:
# with ignored(OSError):
	#os.remove('somefile.tmp')
