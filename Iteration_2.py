'''
ITERABLES

Sequences = Iterable + Ordered
lists, tuples, strings, bytes

'''


# --------------------------------------------------------

for letter in 'Socratia':
	print (letter)


for byte in b'Binary':
	print(byte)
	
'''
for digit in 1001:
	print(digit)
	# TypeError: 'int' object is not iterable
'''

for digit in [eval(_) for _ in str(1001)]:
	print(digit)
	
'''
collections.abc

abstract base classes

'''

# --------------------------------------------------------

users = ('Tim', 'Mike', 'Alexa')

looper = users.__iter__()  # looper = iter(users)
type(looper)  #  tuple_iterator

looper.__next__()  # next(looper)
looper.__next__()
looper.__next__()
looper.__next__()  # StopIteration

	
# --------------------------------------------------------

users = ['Tim', 'Mike', 'Alexa']

for user in users:
	print(user)

it = iter(users)
while True:
	try:
		user = next(it)
		print(user)
	except StopIteration:
		break

# --------------------------------------------------------

class Portfolio:
	def __init__(self):
		self.holdings = {}  # key = ticker, value = number of shares
		
	def buy(self, ticker, shares):
		self.holdings[ticker] = self.holdings.get(ticker, 0) + shares
	
	def sell(self, ticker, shares):
		self.holdings[ticker] = self.holdings.get(ticker, 0) - shares
		
	def __iter__(self):
		return iter(self.holdings.items())
	
	
p = Portfolio()
p.buy('Alpha', 15)
p.buy('Beta', 23)
p.buy('Gamma', 9)
p.buy('Gamma', 20)

for (ticker, shares) in p:
	print(ticker, shares)

# --------------------------------------------------------

import itertools

ranks = list(range(6, 11)) + ['J', 'Q', 'K', 'A']
ranks = [str(rank) for rank in ranks]

suits = ['Diamonds', 'Hearts', 'Spaders', 'Clubs']
deck = [card for card in itertools.product(suits, ranks)]

for (index, card) in enumerate(deck):
	print(1 + index, card)

hands = [hand for hand in itertools.combinations(deck, 5)]
print (f'The number of 5-card Bridge hands is {len(hands)}.')

# --------------------------------------------------------
