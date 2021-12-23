import random

suits = ['\u2666', '\u2665', '\u2660', '\u2663']
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit_color = ['\033[95m', '\033[91m', '\033[93m', '\033[94m']
reset_color = '\033[0m'


class Card:
	''' Represents a single playing card '''
	
	def __init__(self, suit, rank):
		if suit in suits and rank in ranks:
			self.suit = suit
			self.rank = rank
			self.value = self.set_value(self.rank)
	
	def __str__(self):
		
		if self.suit == '\u2666':
			card = f'{suit_color[0]}{self.suit}{self.rank}{reset_color} '
		elif self.suit == '\u2665':
			card = f'{suit_color[1]}{self.suit}{self.rank}{reset_color} '
		elif self.suit == '\u2660':
			card = f'{suit_color[2]}{self.suit}{self.rank}{reset_color} '
		elif self.suit == '\u2663':
			card = f'{suit_color[3]}{self.suit}{self.rank}{reset_color} '
		
		return card
	
	def __eq__(self, other):
		if self.suit == other.suit and self.rank == other.rank:
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


class Deck:
	''' Represents a card deck with a blind and a stack '''
	
	def __init__(self):
		self.blind = []
		self.stack = []
		
		for suit in suits:
			for rank in ranks:
				self.blind.append(Card(suit, rank))
	
	# self.shuffle_blind()
	
	''' deck methods '''
	
	def show(self):
		self.show_blind()
		self.show_stack()
	
	''' blind methods '''
	
	def show_blind(self):
		blind = ''
		print(f'Blind ({len(self.blind)}) card(s):')
		
		for card in self.blind:
			blind += str(card)
		print(blind)
		
		'''
		print(len(self.blind) * '# ')
		'''
	
	def shuffle_blind(self):
		random.shuffle(self.blind)
	
	def draw_card_from_blind(self):
		if not self.blind:
			self.blind = self.stack
			self.stack = []
			self.stack.append(self.blind.pop())
		# random.shuffle(self.blind)
		if self.blind:  # this 'if' statement could be omitted
			return self.blind.pop()  # there was more than 1 card on stack
	
	''' stack methods '''
	
	def show_stack(self):
		
		print(f'Stack ({len(self.stack)}) card(s):')
		stack = ''
		for card in self.stack:
			stack += str(card)
		print(stack)
		
		'''
		print(f'{str(self.stack[-1])}{(len(self.stack) - 1) * '#'}')
		'''
	
	def put_card_on_stack(self, card):
		self.stack.append(card)
	
	def get_top_card_from_stack(self):
		if self.stack:  # this 'if' statement could be omitted
			return self.stack[-1]


deck = Deck()


class Handdeck:
	''' Represents the players cards with 'some' functionality '''
	
	def __init__(self):
		self.cards = []
		self.possible_cards = []
	
	def __len__(self):
		return len(self.cards)
	
	def count_points(self):
		points = 0
		for card in self.cards:
			points += card.value
		return points
	
	def remove_card_from_cards(self, c: Card):
		if self.cards:
			for card in self.cards:
				if card.suit == c.suit and card.rank == c.rank:
					self.cards.remove(card)
	
	def remove_card_from_possible_cards(self, c: Card):
		if self.possible_cards:
			for card in self.possible_cards:
				if card.suit == c.suit and card.rank == c.rank:
					self.possible_cards.remove(card)
	
	def get_possible_cards(self, cards_played=False):
		self.possible_cards = []
		for card in self.cards:
			if deck.get_top_card_from_stack():  # cards on deck not empty
				if not cards_played:
					if card.suit == deck.get_top_card_from_stack().suit or card.rank == deck.get_top_card_from_stack().rank or card.rank == 'J':
						self.possible_cards.append(card)
				else:
					if card.rank == deck.get_top_card_from_stack().rank or card.rank == 'J':
						self.possible_cards.append(card)
		
		return self.possible_cards


class Player:
	''' Represents a player with cards in hand '''
	name = None
	hand = None
	cards_played = []
	
	def __init__(self, name=None):
		self.name = name
		self.hand = Handdeck()
		
		for _ in range(5):
			self.hand.cards.append(deck.blind.pop())
		
		''' open first card on stack '''
		if not deck.stack:
			deck.stack.append(self.hand.cards.pop())
			self.cards_played.append(deck.get_top_card_from_stack())
	
	def show(self):
		self.show_hand()
		self.show_possible_cards()
	
	def show_hand(self):
		cards = ''
		for card in self.hand.cards:
			cards += str(card)
		print(f'{self.name} holds ({len(self.hand.cards)}) card(s) with [{self.hand.count_points()} points]:')
		print(cards)
	
	def show_possible_cards(self):
		cards = ''
		self.hand.possible_cards = self.hand.get_possible_cards(self.cards_played)
		for card in self.hand.possible_cards:
			cards += str(card)
		print(f'{self.name} can play ({len(self.hand.possible_cards)}) card(s):')
		print(cards)
	
	def toggle_possible_cards(self):
		if self.hand.possible_cards:
			card = self.hand.possible_cards.pop()
			self.hand.cards.remove(card)
			self.hand.cards.insert(0, card)
			self.hand.possible_cards.insert(0, card)
	
	def get_card_from_blind(self):
		self.hand.cards.append(deck.draw_card_from_blind())
		self.hand.get_possible_cards()
	
	def put_card_on_stack(self):
		if self.hand.possible_cards:
			card = self.hand.possible_cards.pop()
			self.hand.cards.remove(card)
			deck.put_card_on_stack(card)
			self.cards_played.append(card)
			self.turn_completed = bool(self.cards_played)


class Game:
	player = None
	number_of_players = 0
	player_list = []
	cards_for_evaluation = []
	
	def __init__(self):
		# self.number_of_players = 2
		self.number_of_players = int(input(f'How many players?'))
		
		for player in range(self.number_of_players):
			self.player_list.append(Player(f'Player-{player + 1}'))
		
		self.player = self.player_list[0]
		self.turn_completed = (deck.get_top_card_from_stack().rank != '6')
	
	def activate_next_player(self):
		self.cards_for_evaluation = self.player.cards_played
		self.player.cards_played = []  # preparation for next turn
		self.player_list.append(self.player_list.pop(0))  # get actual player to the end of playerlist
		self.player = self.player_list[0]  # next player now on position 0
	
	def evaluate(self):
		leaps = 0
		
		for card in self.cards_for_evaluation:
			
			if card.rank == '6':
				pass
			if card.rank == '7':
				self.player.get_card_from_blind()
			if card.rank == '8':
				self.player.get_card_from_blind()
				self.player.get_card_from_blind()
				leaps += 1
			if card.rank == 'A':
				leaps += 1
			if card.rank == 'J':
				pass
		
		for _ in range(leaps):
			self.activate_next_player()
		
		self.cards_for_evaluation.remove(card)
		
		return leaps
	
	def play(self):
		
		deck.show()
		self.player.show()
		
		while True:
			
			key = input('a: toggle | s: put | x: draw | (q)uit')
			
			if key == 'q':
				break
			if key == 'a' or key == 'd':
				self.player.toggle_possible_cards()
			if key == 's':
				self.player.put_card_on_stack()
			if key == 'x':
				self.player.get_card_from_blind()
			
			if key == ' ':
				if self.player.cards_played and (deck.get_top_card_from_stack().rank != '6'):
					self.activate_next_player()
					self.evaluate()
			
			deck.show()
			self.player.show()


game = Game()
game.play()
