import random

suits = ['\u2666', '\u2665', '\u2660', '\u2663']
ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card:
	''' Represents a single playing card '''
	
	def __init__(self, suit, rank):
		if suit in suits and rank in ranks:
			self.suit = suit
			self.rank = rank
			self.value = self.setcardvalue(self.rank)
	
	def __str__(self):
		return '{}{} {}'.format(self.suit, self.rank, self.value)
	
	def __eq__(self, other):  # can be
		if self.rank == other.rank or self.suit == other.suit or self.rank == 'J':
			return True
		else:
			return False
	
	def setcardvalue(self, rank):
		value = 0
		if rank in {'10', 'Q', 'K'}: value = 10
		if rank == 'A': value = 15
		if rank == 'J': value = 20
		return value
	
	def getvalue(self):
		return self.value


class Deck:
	''' Represents a full card deck
	with an closed drawpile and an open stack '''
	
	def __init__(self):
		self.drawpile = []
		self.stack = []
		
		for suit in suits:
			for rank in ranks:
				self.drawpile.append((suit, rank))
		
		self.shuffle_drawpile()
		
	
	def shuffle_drawpile(self):
		random.shuffle(self.drawpile)
	
	def show_drawpile(self):
		print(self.drawpile)
	
	def show_stack(self):
		print(self.stack)
	
	def draw_card(self):
		if len(self.drawpile) == 0:
			self.drawpile = self.stack
			self.stack = []
		# random.shuffle(self.drawpile)
		return self.drawpile.pop()
	
	def play_card(self, suit, rank):
		self.stack.append((suit, rank))


deck = Deck()


class Player:
	''' Represents a player with cards in hand '''
	
	def __init__(self, name):
		self.hand = []
		self.possible = []
		for _ in range(5):
			self.get_card()
		if name == 'Player 1':
			deck.play_card(self.hand[4][0], self.hand[4][1])  # Eröffnungskarte
			self.hand.pop(4)
	
	def get_card(self):
		self.hand.append(deck.draw_card())
		
	def possible_cards(self):
		for card in self.hand:
			if card[0] == deck.stack[-1][0] or card[1] == deck.stack[-1][1] or card[1] == 'J':
				self.possible.append(card)
		return self.possible
		
	def put_card(self):
		pass


print('Drawpile:')
deck.show_drawpile()
print('Stack: ')
deck.show_stack()

p1 = Player('Player 1')
p1.put_card()
print('Player 1: ', p1.hand)
p2 = Player('Player 2')
print('Player 2: ', p2.hand)

print('Drawpile:')
deck.show_drawpile()
print('Stack: ')
deck.show_stack()

print('Possible Cards Player 1: ')
print(p1.possible_cards())

