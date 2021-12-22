# Chapter 2 - BUILT-IN FUNCTIONS


bin(3)
# '0b11'
bin(-10)
# '-0b1010'


format(14, '# b'), format(14, 'b')
# ('0b1110', '1110')
f'{14:# b}', f'{14:b}'
# ('0b1110', '1110')


bool(1 < 2)
# True
bool()
# False


bytearray(range(45, 124))
# bytearray(b'-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{')


chr(65)
# 'A'
chr(8364)
# '€'
for i in range(0, 2 ** 8):
	print(i, chr(i))


# delattr(object, name)
class foobar:
	def __init__(self, xvar):
		self.x = xvar


fb = foobar(7)
fb.x
# 7

delattr(fb, 'x')
fb.x
# AttributeError: 'foobar' object has no attribute 'x'


# Container 'dictionary'

d = dict(Anna=1, Berta=2, Regina=3)
d
# {'Anna': 1, 'Berta': 2, 'Regina': 3}


dir
# <built-in function dir>

dir()
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__main__', '__name__', '__package__', '__pyzo__', '__spec__']

dir(abs)
# ['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']


a = 13
b = 4

divmod(a, b)
# (3, 1)
(a // b, a % b)
# (3, 1)


# enumerate(iterable, start=0)

seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

list(enumerate(seasons, start=1))


# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

# equivalent:
def enumerateit(sequence, start=0):
	n = start
	for elem in sequence:
		yield n, elem
		n += 1


list(enumerateit(seasons))

# eval(source, globals=None, locals=None, /)
x = 1
eval('x+1')
# 2

eval('seasons')

# exec(source, globals=None, locals=None, /)
exec('x = 1 + 2')
x
# 3


# filter(function or None, iterable) --> filter object

# filter(seasons.index==1, seasons)


float('+1.23')
# 1.23
float('   -12345\n')
# -12345.0
float('1e-003')
# 0.001
float('+1E6')
# 1000000.0
float('-Infinity')
# --inf


# format(value[, format_spec ])

format(+1.23, '# >6.4')
# ' 1.23'


frozenset([1, 2, 3])


# frozenset({1, 2, 3})


class mat():
	
	def __init__(self, rows: int):
		self.rows = rows
		self.x = [[] for i in range(rows)]
	
	def __repr__(self):
		return "Basis Matrix Objekt"


myMat = mat(2)
getattr(myMat, 'rows')
# 2

repr(myMat)

globals()
# {'__name__': '__main__', '__doc__' ...'mat': <class '__main__.mat'>, 'myMat': <__main__.mat object at 0x7f6972128be0>}


hasattr(myMat, 'rows')
# True


hash(myMat)
# 8755678794343


help(myMat)

"""
Help on mat in module __main__ object:

class mat(builtins.object)
 |  mat(rows: int)
 |
 |  Methods defined here:
 |
 |  __init__(self, rows: int)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)

"""

hex(255)
# '0xff'
hex(-42)
# '-0x2a'
'%# x' % 255, '%x' % 255, '%X' % 255
# ('0xff', 'ff', 'FF')
format(255, '# x'), format(255, 'x'), format(255, 'X')
# ('0xff', 'ff', 'FF')
f'{255:# x}', f'{255:x}', f'{255:X}'
# ('0xff', 'ff', 'FF')

(13.).hex()
# '0x1.a000000000000p+3'


id(myMat)
# 140090860709488


s = input('--> ')
# --> Monty Python's Flying Circus
s
# 'Monty Python's Flying Circus'


x = '11'

int(x, base=10)


class mat2(mat):
	pass


myMat2 = mat2(22)
isinstance(myMat2, mat2)
# True
isinstance(myMat2, mat)
# True


issubclass(mat2, mat)
# True


# iter(object [, sentinel ])

list(range(5))
# [0, 1, 2, 3, 4]

iter(range(5))
# <range_iterator object at 0x7f6972130ae0>

iter([0, 1, 2, 3, 4])
# <list_iterator object at 0x7f6972130c40>

iter({0, 1, 2, 3, 4})
# <set_iterator object at 0x7f6971fd4e40>

it = iter((1, 2, 3, 4))
# <tuple_iterator object at 0x7f6972122580>

print(next(it))


# 1
# 2
# 3
# 4
# Traceback (most recent call last): File "<console>", line 1, in <module> StopIteration


# define iterable:

class PrintNumber:
	def __init__(self, max):
		self.max = max
	
	def __iter__(self):
		self.num = 0
		return self
	
	def __next__(self):
		if (self.num >= self.max):
			raise StopIteration
		self.num += 1
		return self.num


print_num = PrintNumber(3)

print_num_iter = iter(print_num)
print(next(print_num_iter))  # 1
print(next(print_num_iter))  # 2
print(next(print_num_iter))  # 3

#  raises StopIteration
print(next(print_num_iter))


class DoubleIt:
	
	def __init__(self):
		self.start = 1
	
	def __iter__(self):
		return self
	
	def __next__(self):
		self.start *= 2
		return self.start
	
	__call__ = __next__


my_iter = iter(DoubleIt(), 16)

for x in my_iter:
	print(x)

len('Hello')
# 5

len([0, 11, 222, 3333, 44444])
# 5


# class list([iterable ])

list(range(5))
# [0, 1, 2, 3, 4]


locals()
# {'__name__': '__main__', '__doc__' ...  'myMat2': <__main__.mat2 object at 0x7f6971fd2af0>}


# map(function, iterable, ...)
# Return an iterator that applies function to every item of iterable, yielding the results.

map(lambda x: x ** 2, range(5))
# <map object at 0x7f6972130b80>

list(map(lambda x: x ** 2, range(5)))
# [0, 1, 4, 9, 16]


# max(iterable, *[, key, default ])
# max(arg1, arg2, *args[, key ])

max({1, 2, 3, 4, 5})
# 5
max(6, 10)
6
max([1, 2, 3], [1, 2, 4])
# [1, 2, 4]


# class memoryview(object)


# min(iterable, *[, key, default ])
# min(arg1, arg2, *args[, key ])

min({1, 2, 3, 4, 5})
# 1
min(6, 10)
6
min([1, 2, 3], [1, 2, 4])
# [1, 2, 3]


# next(iterator[, default ])

next(map(lambda x: x ** 2, range(5)))
# 0


# class object


# oct(x)

oct(8)
# '0o10'
oct(-56)
# '-0o70'
'%# o' % 10, '%o' % 10
# ('0o12', '12')
format(10, '# o'), format(10, 'o')
# ('0o12', '12')
f'{10:# o}', f'{10:o}'
# ('0o12', '12')


# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)


# ord(c)

ord('a')
# 97
ord('€')
# 8364


# pow(base, exp[, mod ])
# computed more efficiently than pow(base, exp) % mod.

pow(38, -1, mod=97)
# 23
23 * 38 % 97 == 1


# True


# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)


# class property(fget=None, fset=None, fdel=None, doc=None)

# Return a property attribute.


class C:
	
	def __init__(self):
		self._x = None
	
	def getx(self):
		return self._x
	
	def setx(self, value):
		self._x = value
	
	def delx(self):
		del self._x
	
	x = property(getx, setx, delx, "I'm the 'x' property.")


c = C()
c.x = 10
c.x


class Parrot:
	
	def __init__(self):
		self._voltage = 100000
	
	@property
	def voltage(self):
		"""Get the current voltage."""
		return self._voltage


p = Parrot()
p.voltage  # NOT p.voltage()


class D:
	def __init__(self):
		self._x = None
	
	@property
	def x(self):
		"""I'm the 'x' property."""
		return self._x
	
	@x.setter
	def x(self, value):
		self._x = value
	
	@x.deleter
	def x(self):
		del self._x


d = D()
d.x = 10
d.x

# class range(start, stop[, step ])
# immutable sequence type

list(map(lambda x: print(x), range(3, 18, 3)))

# repr(object)

repr('String')
# "'String'"
repr(10)
# '10'
eval(repr(10))
# 10
repr(seasons)
# "['Spring', 'Summer', 'Fall', 'Winter']"

repr(mat)
# "<class '__main__.mat'>"
repr(myMat)
# 'Basis Matrix Objekt'


# reversed(seq)

list(reversed(range(10)))
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


# round(number[, ndigits ])

round(10.5755, 2)
10.58
round(-10.5755, 2)
-10.58

#  class set([iterable ])

set(range(10))
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

set(map(lambda x: x ** 2, range(10)))


# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}


# setattr(object, name, value)

class foobar:
	def __init__(self, xvar):
		self.x = xvar


fb = foobar(1)
fb.x
# 1

# delattr (fb, 'x')
# fb.x
# AttributeError: 'foobar' object has no attribute 'x'

setattr(fb, 'x', 4)
getattr(fb, 'x')
# 4

# may define a new attribute:
setattr(fb, 'y', 6)
getattr(fb, 'y')
# 6


# class slice(start, stop[, step ])

slice(1, 10, 2)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a[1:7:2]
# [2, 4, 6]


# sorted(iterable, *, key=None, reverse=False)

sorted(a[1:7:2], reverse=True)


# [6, 4, 2]


# @staticmethod
# A static method can be called either on the class (such as C.f()) or on an instance (such as C().f()).

class E:
	@staticmethod
	def f(*arg):
		pass


E.f()  # call on the class
E().f()  # call on the instance


class E:
	builtin_open = staticmethod(open)


# class str(object=b'', encoding='utf-8', errors='strict')


# sum(iterable, /, start=0)

sum(range(1, 101))

# super([type[, object-or-type ]])

E.__mro__
# (<class '__main__.E'>, <class 'object'>)

super(E)


# <super: <class 'E'>, NULL>

class C(E):
	
	def method(self, arg):
		super().method(arg)  # This does the same thing as: super(C, self).method(arg)


# class tuple([iterable ])
# immutable sequence type

t = (1, 2, 3)
t[0] = 7
# TypeError: 'tuple' object does not support item assignment


# class type(object)
# class type(name, bases, dict, **kwds)

type(10)
# <class 'int'>
type(E)
# <class 'type'>
E.__class__


# <class 'type'>


class X:
	a = 1


# this creates an identical type object:

X = type('X', (), dict(a=1))

# vars([object ])

vars(X)
# mappingproxy({'a': 1, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'X' objects>, '__weakref__': <attribute '__weakref__' of 'X' objects>, '__doc__': None})

X.__dict__
# mappingproxy({'a': 1, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'X' objects>, '__weakref__': <attribute '__weakref__' of 'X' objects>, '__doc__': None})


vars()  # == locals()
# {'__name__': '__main__', '__doc__': ' pyzokernel/start.py\n\nStarting script for


# zip(*iterables)

list(zip('ABCD', 'xy'))


# [('A', 'x'), ('B', 'y')]

def zipdef(*iterables):
	#  zip('ABCD', 'xy') --> Ax By
	sentinel = object()
	iterators = [iter(it) for it in iterables]
	while iterators:
		result = []
		for it in iterators:
			elem = next(it, sentinel)
			if elem is sentinel:
				return
			result.append(elem)
		yield tuple(result)


list(zipdef('ABCD', 'xy'))
# [('A', 'x'), ('B', 'y')]


x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)
# [(1, 4), (2, 5), (3, 6)]

#  Unzip a list with *Operator:
x2, y2 = zip(*zip(x, y))
x == list(x2) and y == list(y2)
x
# [1, 2, 3]
y
# [4, 5, 6]
# True


# __import__(name, globals=None, locals=None, fromlist=(), level=0)


#  CHAPTER 3 - BUILT-IN CONSTANTS


False
True
None
NotImplemented
Ellipsis
__debug__

quit
exit
copyright
credits
license

#  CHAPTER 4 - BUILT-IN TYPES


# 4.1 Truth Value Testing
"""
None, False
0, 0.0, 0j, Decimal(0), Fraction(0, 1)
'', (), [], {}, set(), range(0)
"""

# 4.2 Boolean Operations — and, or, not

# lower priority
x or y  # short-circuit operator
x and y  # short-circuit operator
not x  # not a == b <=> not (a == b)
# higher priority


# 4.3 Comparisons

"""
<
<=
>
>=
==
!=
is
is not

"""

# 4.4 Numeric Types — int, float, complex
import math

divmod(7, 2)[1]
# 1
math.floor(8.2)
# 8
math.ceil(-7.2)
# -7
(0b0010) << 2
# 8
~(0b0010)
# -3
int.bit_length(10)
# 4


# 4.5 Iterator Types

"""
iterator.__iter__()
iterator.__next__()
"""

# 4.6 Sequence Types — list, tuple, range
"""
x in s
x not in s
s + t
s * n or n * s
s[i]
s[i:j]
s[i:j:k]
len(s)
min(s)
max(s)
# s.index(x[, i[j]])
s.count(x)
"""

# Attention:
lists = [[]] * 3
lists
# [[], [], []]
lists[0].append(3)
lists
# [[3], [3], [3]]

lists = [[] for i in range(3)]
lists[0].append(3)
lists[1].append(5)
lists[2].append(7)
lists  # [[3], [5], [7]]
