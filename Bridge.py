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
	
	def show(self):
		self.show_blind()
		self.show_stack()
	
	# self.shuffle_blind()
	
	''' deck methods '''
	
	def shuffle_blind(self):
		random.shuffle(self.blind)
	
	def show_blind(self):
		print(f'Blind ({len(self.blind)}) card(s):')
		print([str(card) for card in self.blind])
	
	def draw_card_from_blind(self):
		if not self.blind:
			self.blind = self.stack
			self.stack = []
			self.stack.append(self.blind.pop())
		# random.shuffle(self.blind)
		if self.blind:
			return self.blind.pop()  # there was more than 1 card on stack
	
	''' stack methods '''
	
	def put_card_on_stack(self, card):
		self.stack.append(card)
	
	def show_stack(self):
		print(f'Stack ({len(self.stack)}) card(s):')
		print([str(card) for card in self.stack])
	
	def get_top_card_from_stack(self):
		return self.stack[-1]


deck = Deck()


class Handdeck:
	''' Represents the players cards with "some" functionality '''
	
	def __init__(self):
		self.cards = []
	
	def count_points(self):
		points = 0
		for card in self.cards:
			points += card.value
		return points
	
	def get_possible_cards(self):
		self.possible_cards = []
		for card in self.cards:
			if card.__eq__(deck.get_top_card_from_stack()):
				self.possible_cards.append(card)
		return self.possible_cards


class Player:
	''' Represents a player with cards in hand '''
	
	def __init__(self, name=None):
		self.name = name
		self.hand = Handdeck()
		
		for _ in range(5):
			self.get_card_from_blind()
		
		''' open first card on stack '''
		if not deck.stack:
			deck.stack.append(self.hand.cards.pop())
	
	def show(self):
		self.show_hand()
		self.show_possible_cards()
	
	def get_card_from_blind(self):
		self.hand.cards.append(deck.draw_card_from_blind())
	
	''' TODO '''
	
	def put_card_on_stack(self):
		if self.hand.possible_cards:
			deck.put_card_on_stack(self.hand.possible_cards.pop())
			self.hand.cards.remove(deck.get_top_card_from_stack())
	
	def show_hand(self):
		print(f'{self.name} holds ({len(self.hand.cards)}) card(s):')
		print([str(card) for card in self.hand.cards])
		print(f'handdeck values {self.hand.count_points()} points')
	
	def show_possible_cards(self):
		print(f'{self.name} can play ({len(self.hand.get_possible_cards())}) card(s):')
		print(f'{[str(card) for card in self.hand.get_possible_cards()]} --> '
		      f'[{str(deck.get_top_card_from_stack())}]')
	
	def toggle_possible_cards(self):
		# self.hand.possible_cards = self.hand.get_possible_cards()
		if self.hand.possible_cards:
			self.hand.possible_cards.insert(0, self.hand.possible_cards.pop())
		print([str(card) for card in self.hand.cards])
		print([str(card) for card in self.hand.possible_cards])
		


deck.show()
p1 = Player('Player 1')
deck.show()
p1.show()

while True:
	key = input('s -> card to Stack | b -> card from Blind: | (q)uit')
	if key == 's':
		p1.put_card_on_stack()
		deck.show()
		p1.show()
	elif key == 't':
		p1.toggle_possible_cards()
		deck.show()
		p1.show()
	
	elif key == 'q':
		
		break
	else:
		p1.get_card_from_blind()
		deck.show()
		p1.show()
