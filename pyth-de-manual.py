import math

print(u"Gr\u00fcezi Welt")

"""
and
as
assert
break
class
continue
def
del
elif
else
except
False
finally
for
from
global
if
import
in
is
lambda
None
nonlocal
not
or
pass
raise
return
True
try
while
with
yield
"""

choice = 'Mortadella'
print({'Gelbwurst': 1.25,
       'Mortadella': 1.99,
       'Leberwurst': 0.99,
       'Speck': 1.10}[choice])  # 1,99

options = {'Gelbwurst': 1.25,
           'Mortadella': 1.99,
           'Leberwurst': 0.99,
           'Speck': 1.10}
choice = 'Mozarella'
print(options.get(choice, 'Schlechte Auswahl')) # Schlechte Auswahl

if choice in options:
	print(options['choice'])
else:
	print('Schlechte Auswahl')

# 3 Verzweigungen und Schleifen

s0 = 'Habe nun, ach! Philosophie, Juristerei und Medizin'
s1 = ''
i = 0
while i < len(s0):
	s1 += s0[i]  # i-tes Zeichen von s0
	if s0[i] == '!': break
	i += 1
print(s1)

# Collatz Vermutung
def testgerade(n):
	if n % 2 == 0:
		return True
def collatz(n):
	u = 0
	while n > 2:
		print(n)
		while testgerade(n):
			n = n / 2
			u += 1
			print(n)
		n = (3 * n + 1) / 2
		u += 1
	return u
print("Anzahl der Schleifen: {}".format(collatz(871)))

i = 1
while i <= 5:
	print(i)
	i += 1
	if i == 4: break
else:
	print("Fertig!")

i = 1
while i <= 5:
	print(i)
	i += 1
	if i == 4: break
print("Fertig!")

# 4 Strukturierte Daten

t = ('a', 'b', 'c', 'd', 'e')

t[1: 10: 2]  # ('b', 'd')
t[-1: -4: -1]  # ('e', 'd', 'c')

'c' in t  # True
t.count('c')
t.index('b', 0, 1)  # ValueError: tuple.index(x): x not in tuple

t2 = t + t
t2.count('b')  # 2
t2.index('b')  # 1
t2.index('b', 2)  # 6

l = [1, 2, 3, 4, 5]
list(t)  # ['a', 'b', 'c', 'd', 'e']
list('Hund')  # ['H', 'u', 'n', 'd']

l[1] = 7  # [1, 7, 3, 4, 5]
l[1:1] = 2,  # [1, 2, 7, 3, 4, 5]
l[l.__len__(): l.__len__()] = 6,
l.insert(l.__len__(), 7)
l[1:4:2] = 'X', 'X'  # [1, 'X', 7, 'X', 4, 5, 6, 7]

ll = [0, [1, 2]]
ll[1][0]
ll[1][0] = 3
l[l.__len__(): l.__len__()] = 7,

l1 = [1, 2, 3]
l2 = l1  # Referenz wird übergeben!
l2[1] = 4
l1  # [1, 4, 3]

l2 = l1[:]  # shallow copy
l2[1] = 2  # [1, 2, 3]
l1  # [1, 4, 3]

l1 = [1, [2, 3], 4]
l2 = l1[:]  # shallow copy
l1[0] = 0
l1  # [0, [2, 3], 4]
l2  # [1, [2, 3], 4]

l1 = [1, [2, 3], 4]
l2 = l1[:]  # shallow copy
l2[1][0] = 5  # Aber:
l1  # [1, [5, 3], 4]
l2  # [1, [5, 3], 4]

from copy import deepcopy

l1 = [1, [2, 3], 4]
l2 = deepcopy(l1)
l2[1][0] = 5
l1  # [1, [2, 3], 4]
l2  # [1, [5, 3], 4]

liste = [[]] * 4  # nur Referenzen erstellt!
liste  # [[], [], [], []]
liste[0].append('bla')  # [['bla'], ['bla'], ['bla'], ['bla']]

liste = [[] for i in range(4)]
liste  # [[], [], [], []]
liste[0].append('bla')  # [['bla'], [], [], []]

liste = [1, 2, 3]
liste.insert(0, 'a')  # ['a', 1, 2, 3]
liste[0:0] = 'b'  # ['a', 1, 2, 3]
liste  # ['b', 'a', 1, 2, 3]

liste = [1, 2, 3]
liste.reverse()  # [3, 2, 1]

liste = [1, 2, 3]
list(reversed(liste))
liste  # [1, 2, 3]

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del (liste[0::2])  # [2, 4, 6, 8, 10]

s = 'Donaudampfschifffahrtsgesellschaft'
s[5:16]  # 'dampfschiff'
s[::2]  # 'Dnuapshffhtgslshf'
min(s), max(s)  # ('D', 'u')
s.index('f')  # 9

for essen in ('Bratwurst', 'Spinat', 'Kartoffelbrei'):
	if essen == 'Spinat':
		print("Iiih, {} ist eklig!".format(essen))
		break
	print("Mmmh, {}!".format(essen))
else:
	print("Alles lecker!")

zip("abc", (1, 2, 3))  # object at 0x7f86dd5241c8>
list(zip("abc", (1, 2, 3)))  # [('a', 1), ('b', 2), ('c', 3)]

r = range(1, 10)
r[2]  # 3
r[3:5]  # range(4, 6)
r[2::3]  # range(3, 10, 3)
range(0, 3, 2) == range(0, 4, 2)  # True
r.start, r.stop, r.step  # (1, 10, 1)

s = "Donaudampfschifffahrtsgesellschaft"
vokale = "aeiou"
vvk = 0

for i in range(len(s) - 1):
	if s[i] in vokale and s[i + 1] not in vokale:
		vvk += 1
print("{} Vokale standen vor einem Konsonant".format(vvk))

# List Comprehension

[2 * i for i in range(10)]  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print("\n".join(["Gib mir ein {}!".format(c) for c in "HALLO"]))
[i + j for i in ('a', 'b', 'c') for j in ('1', '2', '3')]
[i for i in range(10) if i % 2 == 0]
[i for i in range(0, 21) if i % 3]

for j in range(1, 11):
	print(["{:3}".format(i * j) for i in range(1, 11)])

v1 = list(range(11))
v2 = list(range(11))
print(v1)
print(v2)
print([v1[i] + v2[i] for i in range(len(min(v1, v2)))])

# 5 Funktionen

def hallo():  # glorifizierte Zuweisung mit Referenz
	print("Hallo Welt!")  # auf Funktions-Objekt

x = 1
def func(value):  # x in Namensraum von func
	x = value + 1
	print("x in func:", x)
	return x

func(x)
print("x in main:", x)

def f(liste):  # aber hier:
	liste[1] += 1  # Referenz auf eine Liste

l0 = [1, 2, 3]
f(l0)
l0  # [1, 3, 3]

l0 = [1, 2, 3]
f(l0[:])  # Kopie wird übergeben
l0  # [1, 2, 3]

def g(liste):
	liste = ['a', 'b']  # neue Referenz auf andere Liste
	print(liste)  # außerhalb nicht mehr gültig
l1 = [1, 2, 3]
g(l1)
l1  # [1, 2, 3]

def fakul(n):
	if n == 1: return 1
	return n * fakul(n - 1)  # Rekursion
fakul(10)

def f(a, b, c):
	print("a = {} b = {} c = {}".format(a, b, c))

f(1, 2, 3)
f(1, c=3, b=2)

# Ackermann Funktion
def ack(n=0, m=0):
	if n == 0:
		return m + 1
	elif m == 0:
		return ack(n - 1, 1)
	else:
		return ack(n - 1, ack(n, m - 1))

def f(*args):
	print("args = {}".format(args))
f('a', 3, 'x', 55, 17)

def g(a, b, *args):
	print("a = {} b={} args = {}".format(a, b, args))
g(1, 2, 3, 4)

def ueb(*args):
	return sum(args) / len(args)
ueb(1, 2, 3)

x = 33
def f():
	x = 44  # nonlocal (aus Sicht von g)
	def g():  # Zugriff auf x möglich!
		print(x)
	g()
f()
x

def f():
	def g():  # lokale Funktion
		print("Hallo aus g")
	return g  # Referenz von g nach außen übergeben
func = f()
func()  # Referenz auf lokale Funktion g bleibt erhalten

# Fabrikfunktion
def x_mal(k):
	def aktion(n):
		return k * n
	return aktion
doppelt = x_mal(2)
doppelt(3)
dreifach = x_mal(3)
dreifach(11)

# LEGB Regel (local, enclosed, global, built-in)

x_global: int = 7
def myfunc():
	def local_func():
		return x_global
	return local_func()
myfunc()

x, y = 1, 2
def f():
	global x
	x, y = 5, 6
f()
x, y

def f():
	x, y = 1, 2
	def g():
		y = 3
		def h():
			nonlocal x, y
			x, y = 4, 5
		h()
		print("y =", y)
	g()
	print("x =", x, "y =", y)
f()


# Fabrikfunktion
def makeUnderLine(pattern):
	def underline(s):
		print(s)
		ul = ""
		for i in s:
			ul += pattern
		print(ul)
	return underline
dash = makeUnderLine('~')
dash("Huhu")

# 6.1 Dictionaries

d = {}  # leere Dictionary, NICHT leeres set (s.u.)

d = {'A': 1, 'B': 2, 'C': 3}  # Schlüssel muß hashable sein
dict((('bla', 'blubb'), ('bli', 'fasel')))  # {'bla': 'blubb', 'bli': 'fasel'}

d['A']  # 1
d['D']  # KeyError: 'D'
d.get('D')
d.items()
d.keys()
d.values()
rev = dict(zip(d.values(), d.keys()))  # {'A': 1, 'B': 2, 'C': 3}

d = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie'}
while len(d) > 0:
	print("{} = {}".format(*d.popitem()))
d = {'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie'}
d1 = {'B': 'Beta', 'K': 'Kappa', 'T': 'Tau'}
d.update(d1)

# -----------------------------------------------------
import sys

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
code = 'FLIEGENPILZ'

decode = {}
buchstabe = ord('A')

for c in code + alphabet:
	if c not in decode:
		decode[c] = chr(buchstabe)
		buchstabe += 1

encode = dict([(v, k) for k, v in decode.items()])

cipher = ''
for c in " ".join(sys.argv[1:]).upper():
	cipher += encode.get(c, ' ')
print(cipher)

# -----------------------------------------------------

# 6.2 Funktionsaufrufe mit beliebigen benannten Parametern

"""
----------------------------------------------------------
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
----------------------------------------------------------
"""

args = (1, 2)
print(args)  # (1, 2)
print(*args)  # 1 2

kwargs = {'a': 1, 'b': 2}
print(kwargs)
print(*kwargs)
print(str(**kwargs))

def f(**kwargs):
	for k in kwargs:
		print("{} => {}".format(k, kwargs[k]))

f()
f(a=1, b=2)
f(1, b=2)

def g(a, b=0, *args, **kwargs):
	print("a = {}".format(a))
	print("b = {}".format(b))
	print("Weitere unbenannte Parameter:")
	for p in args:
		print(p)
	print("Weitere benannte Parameter:")
	for p in kwargs:
		print("{} = {}".format(p, kwargs[p]))

g(789, c="blubb", d="bla")
g(123, 456, 789, 999, c="blubb", d="bla")
g(123, c="bli", b=456, d="bla")

def f(a=0, b=0):
	print("a={} b={}".format(a, b))

k = {'a': 123, 'b': 456}
f(**k)
f(**{'b': 789})

def g(**kwargs):
	c = kwargs.pop('c', None)
	if c is not None:
		kwargs['a'] = c + 2
	f(**kwargs)
g(b=123, c=987)

# 6.3 Dictionary Comprehensions

{c: c * (ord(c) - 64) for c in 'ABCDE'}
{k: 0 for k in "abcdefg"}

f = {'a': 12, 'b': 5, 'e': 15, 'A': 3, 'C': 2, 'E': 10}
f0 = {c.upper(): f.get(c.upper(), 0) + f.get(c.lower(), 0) for c in f}
f0

s = "DONAUDAMPFSCHIFFFAHRTSGESELLSCHAFT"
{c: s.count(c) for c in s if c in "AEIOU"}

# 6.4 Mengen
# set       mutable
# frozenset immutable, hashable

f = frozenset(('Alpha', 'Bravo', 'Charlie', 'Bravo'))
f.union(('Delta'))
f

s = ()  # leeres set, mit {} -> leeres Dictionary
s

s = {'Alpha', 'Bravo', 'Charlie', 'Bravo'}
s = set(('Alpha', 'Bravo', 'Charlie', 'Bravo'))
s  # {'Alpha', 'Bravo', 'Charlie'}
s.isdisjoint({'Bravo', 'Hotel', 'Tango'})
s.isdisjoint(['Delta', 'Echo'])

s = set("ABC")
s.issubset("ABCDE")
s.issubset("DEF")
s.issuperset("AB")

s0 = set("ABC")
s1 = set("BC")
s2 = set("ABCDE")
s1 <= s0
s0 >= s2

s0 = set("ABC")
s1 = set("CDE")
s2 = set("BCFG")
s0.intersection(s2)
s0.intersection(s1, s2)
s0 & s2
s0 & s1 & s2

s0.union(s1)
s0.union(s1, s2)
s0 | s1

s2.difference("AB")
s2.difference(s0, s1)
s2 - set("AB")

s1.symmetric_difference(s2)
s1 ^ s2

t = frozenset('abc') | set('bcd')
type(t)
t

s = set("AB")
s.add("C")
s.remove("B")
s.remove("Z")  # KeyError
s.discard("C")
s.discard("Z")  # kein KeyError
s.pop()  # Remove and return an arbitrary set element
s.clear()

s = set("AB")
s.update("BC")
s
s = set("AB")
s |= set("BC")
s


# 7.1 Klassen, Attribute und Methoden'

class Animal:
	species = "Tier"
	name = "Unbekanntes Tier"
	
	def define(self, species, name):    # das Objekt wird als Parameter self übergeben.
		self.species = species
		self.name = name
	
	def describe(self):
		print("{} ist ein {}".format(self.name, self.species))
	
	def getSpecies(self):
		return self.species

lassie = Animal()
lassie.define("Hund", "Lassie")
lassie.describe()

flipper = Animal()
flipper.define("Delfin", "Flipper")
flipper.describe()

maja = Animal()
maja.define("Biene", "Maja")
maja.describe()
maja.getSpecies()

class C0:
	__slots__ = ('a',)
obj = C0()
obj.a = 1
obj.a
obj.b = 2 # 'C0' object has no attribute 'b'


class Animal2:
	all_animals = {}
	
	def define(self, species, name):
		self.species = species
		self.name = name
		self.all_animals[self.name] = self
	
	def describe(self):
		print("{} ist ein {}".format(self.name, self.species))
	
	def getSpecies(self):
		return self.species
	
	@staticmethod
	def enumerate():
		for name, animal in Animal2.all_animals.items(): # unpacking dictionary
			animal.describe()
	
	@classmethod
	def enumerate(cls):
		for name, animal in cls.all_animals.items():
			animal.describe()


lassie = Animal2()
lassie.define("Hund", "Lassie")

flipper = Animal2()
flipper.define("Delfin", "Flipper")

maja = Animal2()
maja.define("Biene", "Maja")

Animal2.enumerate()


# 7.2. Konstruktoren und Destruktoren

class Animal3:
	species = "Tier"
	name = "Unbekanntes Tier"
	
	def __init__(self, name=None, species=None):
		if name: self.name = name
		if species: self.species = species
	
	def __init__(self, name=None, aclass=None, species=None):
		if name: self.name = name
		if species: self.species = species
		if aclass: self.aclass = aclass
		if aclass == 'Insekt':
			self.legs, self.wings = 6, 2
		elif aclass == 'Vogel':
			self.legs, self.wings = 2, 2
		elif aclass == 'Säugetier':
			self.legs, self.wings = 4, 0
	
	def describe(self):
		print("{} ist ein {}".format(self.name, self.species))
	
	def __del__(self):
		print('Destructor called, {} deleted.'.format(self.name))

lassie = Animal3('Lassie', 'Säugetier', 'Hund')
lassie.describe()
lassie.legs


class DeleteLogger:
	def __del__(self):
		print("Objekt {} wird gelöscht!".format(id(self)))
obj1 = DeleteLogger()
obj2 = obj1
del obj1
del obj2


# 7.3 Vererbung

class Animal4:
	
	def __init__(self, name=None, species=None):
		if name: self.name = name
		if species: self.species = species
	
	def describe(self):
		print("{} ist ein {}".format(self.name, self.species))
	
	def __del__(self):
		print('Destructor called, {} deleted.'.format(self.name))


class Bird(Animal4):
	legs = 2
	wings = 2
	
	def __init__(self, name=None, species=None):
		super(Bird, self).__init__(name, species)
	
	def fly(self):
		print("{} fliegt!".format(self.name))
	
	def sing(self):
		print("{} singt!".format(self.name))


tweety = Bird(name="Tweety", species="Kanarienvogel")
tweety.legs, tweety.wings
# (2, 2)
tweety.fly()
# Tweety fliegt!
tweety.sing()
# Tweety singt!

class A:
	def x(self):
		print("Methode x!")

class B:
	def y(self):
		print("Methode y!")

class C(A, B):
	pass

c = C()
c.y()

#-----------------------------------------------------------
import math

class shape:
	color = "black"
	def __init__(self, color = "white"):
		self.color = color

class circle(shape):
	radius = 0
	def __init__(self, radius):
		self.radius = radius
	def area(self):
		return math.pi * self.radius**2
	def circumference(self):
			return 2 * math.pi * self.radius
	
class rectangle(shape):
	length = 0
	width = 0
	def __init__(self, length, width):
		self.length = length
		self.width = width
	def area(self):
		return self.length * self.width
	def circumference(self):
		return 2 * (self.length + self.width)
	
class square(rectangle):
	def __init__(self, length):
		self.length, self.width = length, length
		self.color = "red"
	
c = circle(1)
c.color
c.area()
c.circumference()

r = rectangle(2,7)
r.color
r.area()
r.circumference()

s = square(3)
s.color
s.area()
s.circumference()

#-----------------------------------------------------------

# 7.4 Operatoren überladen

class Vector:
	def __init__(self, x, y):
		self.x, self.y = x, y
	
	def add(self, v):
		return Vector(self.x + v.x, self.y + v.y)
	
	def __repr__(self):
		return "Vector({}, {})".format(self.x, self.y)
	
	def __str__(self):
		return "({}/{})".format(self.x, self.y)
	
	def __add__(self, other):
		if isinstance(other, Vector):
			return Vector(self.x + other.x, self.y + other.y)
		
		elif isinstance(other, int) or isinstance(other, float):
			return Vector(self.x + other, self.y + other)
		
		return NotImplemented
	
	def __radd__(self, other):
		if isinstance(other, Vector):
			return Vector(self.x + other.x, self.y + other.y)
		
		elif isinstance(other, int) or isinstance(other, float):
			return Vector(self.x + other, self.y + other)
		
		return NotImplemented
	
	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self

u = Vector(1, 2)
v = Vector(-1, 0)
t = u.add(v)
t.x, t.y
t
u += Vector(2, 3)
u


# 7.5 »Duck Typing«

# sequence protocol: __len__ + __getitem__

class PowersOfTwo:
	
	def __init__(self, n):
		self.n = n
	
	def __len__(self):
		return self.n
	
	def __getitem__(self, index):
		if isinstance(index, int):
			if 0 <= index < self.n: return 2 ** index
			raise IndexError
		elif isinstance(index, slice):
			start, stop, step = index.indices(self.n)
			return [2 ** i for i in range(start, stop, step)]
		raise TypeError


p2 = PowersOfTwo(10)
len(p2)

p2[6]
p2[3:6]


class Fibonacci:
	
	def __init__(self, n):
		self.n = n
	
	def __len__(self):
		return self.n
	
	def fib(self, zahl):
		a, b = 0, 1
		z = 0
		while z < zahl:
			a, b = b, a + b
			z += 1
		return a
	
	def __getitem__(self, item):
		if isinstance(item, int):
			if 0 <= item <= self.n:
				return self.fib(item)
			raise IndexError
		elif isinstance(item, slice):
			start, stop, step = item.indices(self.n)
			return [self.fib(i) for i in range(start, stop, step)]
		raise TypeError


f = Fibonacci(10)

len(f)
f[2]
f[0:10:1]
