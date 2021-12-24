import random

suits = ['\u2666', '\u2665', '\u2660', '\u2663']
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit_colors = ['\033[95m', '\033[91m', '\033[93m', '\033[94m']
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
			card = f'{suit_colors[0]}{self.suit}{self.rank}{reset_color} '
		elif self.suit == '\u2665':
			card = f'{suit_colors[1]}{self.suit}{self.rank}{reset_color} '
		elif self.suit == '\u2660':
			card = f'{suit_colors[2]}{self.suit}{self.rank}{reset_color} '
		elif self.suit == '\u2663':
			card = f'{suit_colors[3]}{self.suit}{self.rank}{reset_color} '
		
		return card
	
	def __eq__(self, other):
		if self.suit == other.suit and self.rank == other.rank:
			return True
		else:
			return False
	
	def get_suit(self):
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


class Jsuit:
	
	def __init__(self, suit, color):
		self.suit = suit
		self.color = color
	
	def __str__(self):
		
		sign = f'{self.color}{2 * self.suit}{reset_color} '
		
		return sign
	
	def __eq__(self, other):
		if self.suit == other.suit:
			return True
		else:
			return False
	
	def get_suit(self):
		return self.suit


class Jchoice:
	js = []
	j = None
	
	def __init__(self):
		self.js = [Jsuit('\u2666', '\033[95m'), Jsuit('\u2665', '\033[91m'), Jsuit('\u2660', '\033[93m'),
		           Jsuit('\u2663', '\033[94m')]
	
	def toggle_js(self):
		self.js.insert(0, self.js.pop())
	
	def set_j(self):
		self.j = self.js[-1]
	
	def clear_j(self):
		self.j = None
	
	def get_j(self):
		if self.j:
			return self.j
		else:
			return ''
	
	def get_j_suit(self):
		if self.j:
			return self.j.suit
	
	def show_js(self):
		js = ''
		for j in self.js:
			js += str(j)
		print(js)


jchoice = Jchoice()


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
		if self.blind:
			return self.blind.pop()
	
	''' stack methods '''
	
	def show_stack(self):
		
		print(f'Stack ({len(self.stack)}) card(s):')
		stack = ''
		for card in self.stack:
			stack += str(card)
		print(f'{stack}{jchoice.get_j()}')
	
	def put_card_on_stack(self, card):
		self.stack.append(card)
		
		if card.rank == 'J':
			pass
	
	def get_top_card_from_stack(self):
		if self.stack:
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
	
	def get_possible_cards(self, yet_set: bool):
		
		self.possible_cards = []
		stack_card = deck.get_top_card_from_stack()
		
		if not yet_set:
			if stack_card.rank == 'J':
				for card in self.cards:
					if card.suit == jchoice.get_j_suit() or card.rank == 'J':
						self.possible_cards.append(card)
			
			else:
				for card in self.cards:
					if card.rank == stack_card.rank or card.suit == stack_card.suit or card.rank == 'J':
						self.possible_cards.append(card)
		
		if yet_set:
			if stack_card.rank == '6':
				for card in self.cards:
					if card.rank == stack_card.rank or card.suit == stack_card.suit or card.rank == 'J':
						self.possible_cards.append(card)
			
			else:
				for card in self.cards:
					if card.rank == stack_card.rank:
						self.possible_cards.append(card)
		
		return self.possible_cards


class Player:
	''' Represents a player with cards in hand '''
	name = None
	hand = None
	cards_drawn = []
	cards_played = []
	
	def __init__(self, name=None):
		self.name = name
		self.hand = Handdeck()
		
		for _ in range(5):
			card = deck.blind.pop()
			self.hand.cards.append(card)
			self.cards_drawn.append(card)
			
		
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
		self.hand.possible_cards = self.hand.get_possible_cards(bool(self.cards_played))
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
		if deck.blind and not self.cards_played and not self.cards_drawn\
				and not self.hand.get_possible_cards(self.cards_played):
			card = deck.draw_card_from_blind()
			self.hand.cards.append(card)
			self.cards_drawn.append(card)
			self.hand.get_possible_cards(bool(self.cards_played))
	
	def put_card_on_stack(self):
		if self.hand.possible_cards:
			card = self.hand.possible_cards.pop()
			self.hand.cards.remove(card)
			deck.put_card_on_stack(card)
			self.cards_played.append(card)
			self.hand.possible_cards = self.hand.get_possible_cards(bool(self.cards_played))
			jchoice.clear_j()


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
	
	# self.turn_completed = (deck.get_top_card_from_stack().rank != '6')
	
	def activate_next_player(self):
		self.cards_for_evaluation = self.player.cards_played
		self.player.cards_played = []  # preparation for next turn
		self.player_list.append(self.player_list.pop(0))  # get actual player to the end of playerlist
		self.player = self.player_list[0]  # next player now on position 0
		self.player.cards_drawn = []
	
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
			
			self.cards_for_evaluation.remove(card)
		
		for _ in range(leaps):
			self.activate_next_player()

		
		return None
	
	def play(self):
		
		deck.show()
		self.player.show()
		
		while True:
			
			key = input('a: toggle | s: put | x: draw | space: next Player | (q)uit game')
			
			if key == 'q':
				break
			if key == 'a' or key == 'd':
				self.player.toggle_possible_cards()
			if key == 's':
				self.player.put_card_on_stack()
			if key == 'x':
				self.player.get_card_from_blind()
			
			if key == ' ':
				
				if self.player.cards_played and (deck.get_top_card_from_stack().rank == 'J'):
					
					jchoice.show_js()
					
					while True:
						key = input('a: toggle color | space: set color')
						
						if key == 'a' or key == ' ':
							jchoice.toggle_js()
							jchoice.show_js()
						if key == ' ':
							jchoice.set_j()
							break
					
					self.activate_next_player()
					self.evaluate()
					
					
				
				
				elif self.player.cards_played and (deck.get_top_card_from_stack().rank != '6'):
					self.activate_next_player()
					self.evaluate()
			
			deck.show()
			self.player.show()


game = Game()
game.play()
