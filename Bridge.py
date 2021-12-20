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
	with a closed deck and an open stack '''
	
	def __init__(self):
		self.blind = []
		self.stack = []
		
		for suit in suits:
			for rank in ranks:
				self.blind.append(Card(suit, rank))
		
		#self.shuffle_blind()
	
	''' deck methods '''
	def shuffle_blind(self):
		random.shuffle(self.blind)
	
	def show_blind(self):
		print([str(card) for card in self.blind])
	
	def draw_blind(self):
		if len(self.blind) == 0:
			self.blind = self.stack
			self.stack = []
		random.shuffle(self.blind)
		return self.blind.pop()
	
	''' stack methods '''
	def put_stack(self, card):
		self.stack.append(card)
	
	def show_stack(self):
		print([str(card) for card in self.stack])
		
	def what_is_stack(self):
		return self.stack[-1]
	

deck = Deck()
deck.show_blind()
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
	
	def show_possible_cards(self):
		self.calculate_possible_cards()
		print([str(card) for card in self.possible])
	
	def get_card(self):
		self.hand.append(deck.draw_blind())

	def calculate_possible_cards(self):
		for card in self.hand:
			if card.__eq__(deck.what_is_stack()):
				self.possible.append(card)
		return self.possible

	def play(self):
		self.calculate_possible_cards()
		while self.possible:
			card =self.possible.pop()
			deck.put_stack(card)
			self.hand.remove(card)
			self.calculate_possible_cards()


p1 = Player('Computer')
p2 = Player('Player 2')

print('Deck:', len(deck.blind))
deck.show_blind()
print('Stack: ', len(deck.stack))
deck.show_stack()

print(p1.name, ':')
p1.show_hand()
print(p1.name, 'Options:')
p1.show_possible_cards()

print(p2.name, ':')
p2.show_hand()
print(p2.name, 'Options:')
p2.show_possible_cards()


print('Deck:', len(deck.blind))
deck.show_blind()
print('Stack: ', len(deck.stack))
deck.show_stack()


while True:
	print('Stack: ', len(deck.stack))
	deck.show_stack()
	
	print('Possible Cards Player 1: ')
	p1.show_hand()
	p1.show_possible_cards()
	p1.play()
	
	print('Stack: ', len(deck.stack))
	deck.show_stack()


