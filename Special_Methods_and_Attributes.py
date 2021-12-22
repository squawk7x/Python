class Snowflake:
	pass


flake = Snowflake()

print(dir(flake))  # some - but not all - of methods and attributes


# -----------------------------------------------------------------

class Martian:
	pass


m1 = Martian()
m1.first_name = 'Owen'
m1.last_name = 'Phelps'

print(m1.__dict__)


# -----------------------------------------------------------------


class Martian:
	'''Someone who lives on Mars'''
	
	def __init__(self, fn, ln):
		self.first_name = fn
		self.last_name = ln


print(Martian.__doc__)

m2 = Martian('Rob', 'Schenk')
print(m2.__dict__)

m2.arrival_date = '2037-12-15'
print(m2.__dict__)


# -----------------------------------------------------------------

class Martian:
	'''Someone who lives on Mars'''
	
	def __init__(self, fn, ln):
		self.first_name = fn
		self.last_name = ln
	
	def __setattr__(self, name, value):
		print(f'>>> You set {name} = {value}')
		self.__dict__[name] = [value]
# because original __setattr__ is overridden


m3 = Martian('Klaus', 'Iserlohn')
print(m3.__dict__)


# -----------------------------------------------------------------

class Martian:
	'''Someone who lives on Mars'''
	
	def __init__(self, fn, ln):
		self.first_name = fn
		self.last_name = ln
	
	def __setattr__(self, name, value):
		print(f'>>> You set {name} = {value}')
		self.__dict__[name] = value
	
	# because original __setattr__ is overridden
	
	def __getattr__(self, name):
		print(f">>> Get the '{name}' attribute")
		if name == 'full_name':
			return f'{self.first_name} {self.last_name}'
		else:
			raise AttributeError(f"No attribute found '{name}'")


m4 = Martian('Pierre', 'Aberg')
print(f"First name = {m4.first_name}")  # calling __getattribute__
print(f"Last name = {m4.last_name}")  # calling __getattribute__
print(m4.full_name)  # calling __getattr__
# __getattr__ is called only once with full_name

'''
>>> You set first_name = Pierre
>>> You set last_name = Aberg
First name = Pierre
Last name = Aberg
>>> Get the 'full_name' attribute
Pierre Aberg
'''
# print((m4.martian_name))

print(m4.__dict__)  # full_name is not stored in internal dictionary


# -----------------------------------------------------------------

class Martian:
	'''Someone who lives on Mars'''
	
	def __init__(self, fn, ln):
		self.first_name = fn
		self.last_name = ln
	
	def __setattr__(self, name, value):
		self.__dict__[name] = value


m5 = Martian('Prayash', 'Mohapatra')
print(m5)  # <__main__.Martian object at 0x7f344423ad30>
print(m5.__str__())  # <__main__.Martian object at 0x7f344423ad30>
print(id(m5))  # 139862458215728
0x7f344423ad30  # 139862458215728


# -----------------------------------------------------------------

class Martian:
	'''Someone who lives on Mars'''
	
	def __init__(self, fn, ln):
		self.first_name = fn
		self.last_name = ln
	
	def __setattr__(self, name, value):
		self.__dict__[name] = value
	
	def __str__(self):
		return f'{self.first_name} {self.last_name}'
	
m6 = Martian('Rod', 'Morlay')
print(m6)

# -----------------------------------------------------------------

'''
COMPARE


'''

class Martian:
	'''Someone who lives on Mars'''
	
	def __init__(self, fn, ln):
		self.first_name = fn
		self.last_name = ln
	
	def __setattr__(self, name, value):
		self.__dict__[name] = value
	
	def __str__(self):
		return f'{self.first_name} {self.last_name}'
	
	def __lt__(self, other):
		print(f'Comparing {self} and {other}')
		if self.last_name != other.last_name:
			return (self.last_name < other.last_name)
		else:
			return (self.first_name < other.first_name)
		
m7 = Martian('Cyrille', 'Collin')
m8 = Martian('Andy', 'Talor')

m7 < m8

