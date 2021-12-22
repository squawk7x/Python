'''
LOGGING

 0 - NOTSET
10 - DEBUG
20 - INFO
30 - WARNING
40 - ERROR
50 - CRITICAL


'''

import logging

dir(logging)

'''
CONSTANTS
Classes
methods

'''

import logging
import math

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename="./Loggingtest.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
# default level 30 - WARNING
# default filemode = 'a' (append)

logger = logging.getLogger()


def quadratic_formula(a, b, c):
	"""Return the solutions to the quadratic equation ax^2 + bx +c = 0"""
	
	logger.info('# quadratic_formula({0}, {1}, {2})'.format(a, b, c))
	
	# Compute the discrminat
	logger.debug("# Compute the discriminent")
	disc = b ** 2 - 4 * a * c
	
	# Compute the two roots
	root1 = (-b + math.sqrt(disc)) / (2 * a)
	root2 = (-b - math.sqrt(disc)) / (2 * a)
	
	# Return the roots
	logger.debug('# Return the roots')
	
	return (root1, root2)


roots = quadratic_formula(1, 0, -4)
print(roots)
roots = quadratic_formula(1, 0, 1)
print(roots)

logger.debug('Debug message...')
logger.info('Info message...')
logger.warning('Warning message...')
logger.error('Error message...')
logger.critical('Critical message...')
