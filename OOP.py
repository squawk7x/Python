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
dev_1 = Developer('Pro', 'Grammer', 'Python')
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
