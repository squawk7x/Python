import unittest
from math import pi


def circle_area(r):
	if type(r)not in [int, float]:
		raise TypeError('The must be a non-negative real number')
	if r < 0:
		raise ValueError('The radius cannot be negative')
	return pi * (r ** 2)


class Tips_Test(unittest.TestCase):  # create Subclass of TestCase class
	
	def setUp(self):
		print(('SETUP Called...'))
		self.a = 10
	
	def tearDown(self):
		self.a = 0
		print('TEARDOWN Called...')
	
	def test_func(self):  # naming convention test_* or *_test
		print('TEST-1 Called...')
		
		# Arrange
		a = 10
		
		# Act
		result = circle_area(self.a)
		
		# Assert
		self.assertAlmostEqual(result, pi * 100)
	
	def test_values(self):
		print('TEST-2 Called...')
		
		# Arrange
		a = 10
		
		# Act
		result = circle_area(self.a)
		
		# Assert
		self.assertRaises(ValueError, circle_area, -2)
		
	def test_types(self):
		self.assertRaises(TypeError, circle_area, 3+5j)
		self.assertRaises(TypeError, circle_area, True)
		self.assertRaises(TypeError, circle_area, 'string')

if __name__ == '__main__':
	unittest.main()

'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK


'''
