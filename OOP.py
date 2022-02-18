class Employee:
	attr = 'class attribute'
	num_of_emps = 0

	def __init__(self, first, last):
		self.first = first
		self.last = last
		Employee.num_of_emps += 1  # not: self.num_of employees -> will stay class variable

	@classmethod
	def change_attr(cls, attribute):
		cls.attr = attribute

	# alternative constructor
	@classmethod
	def from_string(cls, emp_by_string):
		first, last = emp_by_string.split('-')
		return cls(first, last)

	@staticmethod
	def is_work_day(day):  # no self no cls
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

	@property
	def email(self):
		return "{}.{}@email.com".format(self.first, self.last)

	@property
	def fullname(self):
		return "{} {}".format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		self.first = None
		self.last = None
		print("deleted")


class Developer(Employee):
	attr = 'Developer class attribute'

	def __init__(self, first, last, prog_lang):
		super().__init__(first, last)
		self.prog_lang = prog_lang


print('Employee.num_of_emps: ', Employee.num_of_emps)
emp_1 = Employee('Jim', 'Smith')
emp_2 = Employee('Test', 'User')
print('Employee.num_of_emps: ', Employee.num_of_emps)

'''

class variable <-> instance variable

'''

print(Employee.attr)
print("namespace class: ", Employee.__dict__)
print(emp_1.attr)
print("namespace instance: ", emp_1.__dict__)
print(emp_2.attr)
print("namespace instance: ", emp_2.__dict__)

emp_1.attr = "instance attr"  # instance will create own attribute (self. ...)

print(Employee.attr)
print(emp_1.attr)
print(emp_2.attr)

print("namespace class: ", Employee.__dict__)
print("namespace instance: ", emp_1.__dict__)
print("namespace instance: ", emp_2.__dict__)

'''

regular method - class method - static method

'''

Employee.change_attr('new class attribute')
print(Employee.attr)
print(emp_1.attr)
print(emp_2.attr)

emp_1.change_attr('attribute changed by emp_1')
print(Employee.attr)
print(emp_1.attr)
print(emp_2.attr)

'''

class method as alternate constructor

'''

emp_3_by_str = 'John-Doe'
emp_3 = Employee.from_string(emp_3_by_str)

print(emp_1.first)
print(emp_2.first)
print(emp_3.first)

'''
static method

'''

import datetime

my_date = datetime.date(2021, 12, 14)
print(my_date, 'is workday:', Employee.is_work_day(my_date))

'''
Inheritance - Subclasses

'''

print(help(Developer))
dev_1 = Developer('Pro', 'Grammar', 'Python')
print(isinstance(dev_1, Employee))
print(issubclass(Developer, Employee))

'''

@property
def func(self)
	...
	
method 'func' can be used like an attribute

Setter & Getter

'''

# without @property:
# print(emp_1.first, emp_1.last, emp_1.email())

# with @property:
print(emp_1.first, emp_1.last, emp_1.email)
print(emp_1.fullname)

emp_1.fullname = 'Corey Schafer'  # method used like attribute
print(emp_1.first, emp_1.last, emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.first, emp_1.last, emp_1.email)
print(emp_1.fullname)

'''
Raymond Hettinger

	Summary: Toolset for New-Style Classes

1. Inherit from object() // old
2. Instance variables: 
	for information unique to an instance
3. Class variables: 
	for data shared among all instances
4. Regular methods: 
	need 
		'self' 
	to operate on instance data
5. Class methods: 
	implement alternative constructors. They need 
		'cls'
	so they can create subclass instances as well.
6. Static methods: 
	attach functions to classes. 
	They don't need 'self' or 'cls'.
	Static methods improve discoverability and require context to be specified.
7. A propoerty(): // old
    lets getter and setter methods invoked automatically by attribute access.
    This allows Python classes to freely expose their instance variables.
8. The __slots__ variable
	implements the Flyweight Design Pattern by suppressing instance dictionaries.
	Shrinks down the size of instancies.


'''


class A:
	class_a_var = 0

	# __slots__ =

	def __init__(self):
		self.instance_a_var = 'instance a variable'
		self.property_a_var = 'property a variable'
		# 2 possibilities to access class_var:
		A.class_a_var = 1  # not added to a.__dict__

	# self.class_var = 2  # added to a.__dict__

	def regular_a_method(self):
		print('regular a method')

	@property
	def property_a_method(self):  # defined as method, access like attribute
		return self.property_a_var

	@property_a_method.setter
	def property_a_method(self, var):
		self.property_a_var = var

	@property_a_method.deleter
	def property_a_method(self):
		self.property_a_var = None

	@classmethod
	def set_class_a_var(cls, var):
		cls.class_a_var = var

	@staticmethod
	def static_a_method():
		print('static a method')


print(A.__dict__, '\n')
a = A()
print(a.__dict__, '\n')

a.regular_a_method()

print(a.property_a_method)  # access like a variable
a.property_a_method = 'new property a variable'  # setting like a variable
print(a.property_a_method)

del a.property_a_method
print(a.property_a_method)

A.set_class_a_var('new class a variable')
print(A.class_a_var)

A.static_a_method()

'''
Raymond Hettinger

	The Art of Subclassing

	InstDict1   --->
	InstDict2   --->    SubClassDict   ---> ParClassDict
	InstDict3   --->

	A Subclass delegates work to another class
	A Subclass and its parents are just two different dictionaries that contain functions
	A Subclass points to its parent
	The pointer means: 'I delegate work to this class'

	Classes are dictionaries of functions
	Subclasses point to other dictionaries to reuse their code
	The Subclasses are in complete control of what happens

	LISKOV SUBSTTUTION PRINCIPLE:
	"If S is a subtype of T, 
	then objects of type T may be replaced with objects of type S" 

		-> POLYMORPHISM & SUBSTITUTABILITY

'''


class B(A):
	class_b_var = 100

	def __init__(self, var):
		super().__init__()
		self.instance_b_var = var

	pass


# print(help(B))

b = B(200)

print(isinstance(b, A))
print(issubclass(B, A))

'''
Raymond Hettinger

	super considered super

	Linearisation:

	MRO Method Resolution Order
	super in Python does not call parents, 
	but parents from the children
	super means "next in line", starting from youngest child

	!!!
	-> children get called before their parents
	-> parents get called in the order listed
	-> parents stay in order
	!!!
	-> multiple inheritance: use keyword arguments
		(you can not know who you are calling)

'''


class DoughFactory:

	def get_dough(self):
		return 'insecticide treated wheat dough'


class Pizza(DoughFactory):

	def order_pizza(self, *toppings):
		print('Getting dough')
		dough = super().get_dough()
		print('Making pie with %s' % dough)
		for topping in toppings:
			print('Adding %s' % topping)


class OrganicDoughFactory(DoughFactory):

	def get_dough(self):
		return 'pure untreated wheat dough'


class OrganicPizza(Pizza, OrganicDoughFactory):
	pass


if __name__ == '__main__':
	Pizza().order_pizza('Pepperoni', 'Pepper')
	print(help(Pizza))

	OrganicPizza().order_pizza('Sausage', 'Mushroom')
	print(help(OrganicPizza))


# --------------------------------------------------------------

class Robot:
	""" Sophisticated class that moves a real robot """

	# Don't wear down real robots by running tests!

	def fetch(self, tool):
		print('Physical Movement! Fetching')

	def move_forward(self, tool):
		print('Physical Movement! Moving forward')

	def move_backward(self, tool):
		print('Physical Movement! Moving backward')

	def replace(self, tool):
		print('Physical Movement! Replacing')


class CleaningRobot(Robot):  # CleaningRobot 'is a' Robot, not 'has a' Robot

	def clean(self, tool, times=10):
		super().fetch(tool)
		for i in range(times):
			super().move_forward(tool)
			super().move_backward(tool)
		super().replace(tool)


# if __name__ == '__main__':
# 	t = CleaningRobot()
# 	t.clean('broom')


class MockBot(Robot):
	""" Simulate a real robot by merely recording tasks """

	def __init__(self):
		self.tasks = []

	def fetch(self, tool):
		self.tasks.append('fetching %s' % tool)

	def move_forward(self, tool):
		self.tasks.append('forward %s' % tool)

	def move_backward(self, tool):
		self.tasks.append('backward %s' % tool)

	def replace(self, tool):
		self.tasks.append('replacing %s' % tool)


class MockedCleaningRobot(CleaningRobot, MockBot):
	""" Injects a mock bot into the robot dependency """


# it checks Mockbot *before* Robot is checked


import unittest


class TestCleaningRobot(unittest.TestCase):

	def test_clean(self):
		t = MockedCleaningRobot()
		t.clean('mop')
		expected = (['fetching mop'] +
					['forward mop', 'backward mop'] * 10 +
					['replacing mop'])

		self.assertEqual(t.tasks, expected)


if __name__ == '__main__':
	unittest.main()
