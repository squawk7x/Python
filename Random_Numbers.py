import random


'''
uniform distributions

'''
for _ in range(10):
	print(random.random())


def my_random(lowest=0, highest=1):
	return random.random() * (highest - lowest) + lowest


for _ in range(10):
	print(my_random(3, 7))
	
# uniform function:

for _ in range(10):
	print(random.uniform(3,7))

'''
more distributions

'''

for _ in range(10):
	print(random.normalvariate(0, 1))


'''
discrete distributions

'''

for _ in range(10):
	print(random.randint(1,6))

choices = ['rock', 'paper', 'scissors']
for _ in range(10):
	print(random.choice(choices))

