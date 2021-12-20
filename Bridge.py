import random

suits = ['\u2666', '\u2665', '\u2660', '\u2663']
ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card:
	''' Represents a single playing card '''
	
	def __init__(self, suit, rank):
		if suit in suits and rank in ranks:
			self.suit = suit
			self.rank = rank
			self.value = self.set_value(self.rank)
	
	def __str__(self):
		return '{} {}'.format(self.suit, self.rank)
	
	def __eq__(self, other):
		if self.rank == other.rank or self.suit == other.suit or self.rank == 'J':
			return True
		else:
			return False
	
	def get_suite(self):
		return self.suit
	
	def get_rank(self):
		return self.rank
	
	def set_value(self, rank):
		value = 0
		if rank in {'10', 'Q', 'K'}: value = 10
		if rank == 'A': value = 15
		if rank == 'J': value = 20
		return value
	
	def get_value(self):
		return self.value


# card = Card()


class Deck:
	''' Represents a full card deck
	with a closed drawpile and an open stack '''
	
	def __init__(self):
		self.drawpile = []
		self.stack = []
		
		for suit in suits:
			for rank in ranks:
				self.drawpile.append(Card(suit, rank))
		
		#self.shuffle_drawpile()
	
	''' drawpile methods '''
	def shuffle_drawpile(self):
		random.shuffle(self.drawpile)
	
	def show_drawpile(self):
		print([str(card) for card in self.drawpile])
	
	def draw_card(self):
		if len(self.drawpile) == 0:
			self.drawpile = self.stack
			self.stack = []
		# random.shuffle(self.drawpile)
		return self.drawpile.pop()
	
	''' stack methods '''
	def put_card(self, card):
		self.stack.append(card)
	
	def show_stack(self):
		print([str(card) for card in self.stack])
		
	def get_stackcard(self):
		return self.stack[-1]
	

deck = Deck()
deck.show_drawpile()
deck.show_stack()



class Player:
	''' Represents a player with cards in hand '''
	
	def __init__(self, name=None):
		self.hand = []
		self.possible = []
		self.name = name
		
		for _ in range(5):
			self.get_card()
		
		''' Eröffnungskarte '''
		if deck.stack == []:
			deck.stack.append(self.hand.pop())
	
	def show_hand(self):
		print([str(card) for card in self.hand])
	
	def show_possible(self):
		print([str(card) for card in self.possible])
	
	def get_card(self):
		self.hand.append(deck.draw_card())

	def calculate_possible_cards(self):
		for card in self.hand:
			if card.__eq__(deck.get_stackcard()):
				self.possible.append(card)
		return self.possible

	def play(self):
		self.calculate_possible_cards()
		while self.possible:

			deck.put_card(self.possible.pop())
			self.hand.remove()
			self.calculate_possible_cards()


p1 = Player('Computer')
p2 = Player('Player 2')

print('Drawpile:', len(deck.drawpile))
deck.show_drawpile()
print('Stack: ', len(deck.stack))
deck.show_stack()

print(p1.name, ':', p1.show_hand())
print(p2.name, ':', p2.show_hand())

print('Drawpile:', len(deck.drawpile))
deck.show_drawpile()
print('Stack: ', len(deck.stack))
deck.show_stack()

'''


while True:
	print('Stack: ', len(deck.stack))
	deck.show_stack()
	
	print('Possible Cards Player 1: ')
	print(p1.show_hand())
	print(p1.show_possible())
	p1.play()
	
	print('Stack: ', len(deck.stack))
	deck.show_stack()

'''

