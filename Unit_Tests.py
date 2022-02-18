import unittest
from math import pi


def circle_area(r):
	if type(r)not in [int, float]:
		raise TypeError('The must be a non-negative real number')
	if r < 0:
		raise ValueError('The radius cannot be negative')
	return pi * (r ** 2)


class TestCircleArea(unittest.TestCase):  # create Subclass of TestCase class
	
	def setUp(self):
		print(('SETUP Called...'))
		self.a = 10
	
	def tearDown(self):
		self.a = 0
		print('TEARDOWN Called...')

	def test_area(self):
		# Test areas when radius >= 0

		print('test_area called...')
		self.assertAlmostEqual(circle_area(1), pi)
		self.assertAlmostEqual(circle_area(0), 0)
		self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

	def test_func(self):  # naming convention test_* or *_test
		print('test_func called...')
		
		# Arrange
		a = 10
		
		# Act
		result = circle_area(a)
		
		# Assert
		self.assertAlmostEqual(result, pi * 100)
	
	def test_values(self):
		# Make sure value errors are raised when necessary

		print('test_values called...')
		
		# Arrange
		a = -2
		
		# Act
		# result = circle_area(a)
		
		# Assert
		self.assertRaises(ValueError, circle_area, a)
		
	def test_types(self):
		# Make sure type errors are raised when input is not real number

		print('test_types called...')
		self.assertRaises(TypeError, circle_area, 3+5j)
		self.assertRaises(TypeError, circle_area, True)
		self.assertRaises(TypeError, circle_area, 'string')

if __name__ == '__main__':
	unittest.main()

# python3.10 -m unittest Unit_Tests.py

'''
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK


'''
