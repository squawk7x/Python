import random

suits = ['\u2666', '\u2665', '\u2660', '\u2663']
ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]

class Card:
	''' Represents a single playing card '''
	
	def __init__(self, suit, rank):
		if suit in suits and rank in ranks:
			self.suit = suit
			self.rank = rank
			self.value = self.setvalue(self.rank)
	
	def __str__(self):
		return '{} {}'.format(self.suit, self.rank, self.value)
	
	def __eq__(self, other):
		if self.rank == other.rank or self.suit == other.suit or self.rank == 'J':
			return True
		else:
			return False
		
	def getsuite(self):
		return self.suit
		
	def getrank(self):
		return self.rank
	
	def setvalue(self, rank):
		value = 0
		if rank in {'10', 'Q', 'K'}: value = 10
		if rank == 'A': value = 15
		if rank == 'J': value = 20
		return value
	
	def getvalue(self):
		return self.value

#card = Card()



class Deck:
	''' Represents a full card deck
	with a closed drawpile and an open stack '''
	
	def __init__(self):
		self.drawpile = []
		self.stack = []
		
		for suit in suits:
			for rank in ranks:
				self.drawpile.append(Card(suit, rank))
		
		self.shuffle_drawpile()
		
	
	def shuffle_drawpile(self):
		random.shuffle(self.drawpile)
	
	def show_drawpile(self):
		cards = [str(card) for card in self.drawpile]
		print(cards)
	
	def show_stack(self):
		cards = [str(card) for card in self.stack]
		print(cards)
	
	def draw_card(self):
		if len(self.drawpile) == 0:
			self.drawpile = self.stack
			self.stack = []
		# random.shuffle(self.drawpile)
		return self.drawpile.pop()
	
	def put_card(self, card):
		self.stack.append(card)


deck = Deck()


class Player:
	''' Represents a player with cards in hand '''
	
	def __init__(self, name):
		self.hand = []
		self.possible = []
		self.name = name
		
		for _ in range(5):
			self.get_card()
			
		''' Eröffnungskarte '''
		if self.name == 'Player 1':
			deck.put_card(self.hand.pop())
			
	def show_hand(self):
		cards = [str(card) for card in self.hand]
		print(cards)
		
	def show_possible(self):
		cards = [str(card) for card in self.possible]
		print(cards)
	
	def get_card(self):
		self.hand.append(deck.draw_card())
		
	def possible_cards(self):
		for card in self.hand:
			if card.__eq__(deck.stack[-1]):
				self.possible.append(card)
		return self.possible
		
	def play_card(self):
		pass


print('Drawpile:', len(deck.drawpile))
deck.show_drawpile()
print('Stack: ', len(deck.stack))
deck.show_stack()

p1 = Player('Player 1')
print('Player 1: ', p1.show_hand())
p2 = Player('Player 2')
print('Player 2: ', p2.show_hand())

print('Drawpile:', len(deck.drawpile))
deck.show_drawpile()
print('Stack: ', len(deck.stack))
deck.show_stack()

print('Possible Cards Player 1: ')
p1.possible_cards()
print(p1.show_possible())

