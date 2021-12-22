def is_prime_v1(n):
	''' Returns True if 'n' is a prime number'''
	if n == 1:
		return False  # 1 is not a prime, it is a "unit"
	
	for d in range(2, n):
		if n % d == 0:
			return False
	
	return True


'''

   36:
   
 2 x 18
 3 x 12
 4 x  9      dividing line
 6 x  6   <----------------
 9 x  4       duplicates
12 x  3
18 x  2
36 x  1

'''

import math


def is_prime_v2(n):
	''' Returns True if 'n' is a prime number'''
	if n == 1:
		return False  # 1 is not a prime, it is a "unit"
	if n == 2:
		return True
	
	for d in range(3, int(math.sqrt(n)) + 1, 2):
		if n % d == 0:
			return False
	
	return True


# ================ TEST FUNKTION =====================

import time

t0 = time.time()

for n in range(1, 10001, 2):
	print(n, is_prime_v2(n))

t1 = time.time()

print(f'time required {t1 - t0}')
