'''
RANDOM WALK & MONTE CARLO METHOD


'''

import random


def random_walk(n):
	'''Returns coordinates after 'n' block random walk'''
	
	x, y = 0, 0
	
	for _ in range(n):
		step = random.choice(['N', 'S', 'E', 'W'])
		
		if step == 'N':
			y = y + 1
		elif step == 'S':
			y = y - 1
		elif step == 'E':
			x = x + 1
		else:
			x = x - 1
	
	return (x, y)

for _ in range(25):
	walk = random_walk(10)
	distance = abs(walk[0]) + abs(walk[1])
	print(walk, 'Distance from home = ', distance)


def random_distance(n):
	'''Returns (random) distance after 'n' block random walk
	(short version)'''
	
	x, y = 0, 0
	for i in range(n):
		(dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
		x += dx
		y += dy
	return abs(x) + abs(y)


number_of_walks = 25
walk_length = 10

for _ in range(number_of_walks):
	print(f'After {walk_length} blocks walk distance from home is {random_distance(walk_length)}')

Random_Walk_Monte_Carlo.py
'''
MONTE CARLO SIMULATION

'''

'''
What is the longest random walk you can take so that
on average
you will end up 4 blocks or fewer from home?

'''

number_of_walks = 1000
max_dist = 4

for walk_length in range(1, 50):
	no_transport = 0
	for _ in range(number_of_walks):
		if random_distance(walk_length) <= max_dist:
			no_transport +=1
	no_transport_percentage = no_transport/number_of_walks
	print(f'After {walk_length} blocks probability of no transport is {100*no_transport_percentage}')
	
