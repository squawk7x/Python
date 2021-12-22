import random


suits = ['\u2666', '\u2665', '\u2660', '\u2663']
ranks = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class bcolors:
	diamond = '\033[95m'  # MAGENTA
	heart = '\033[91m'  # RED
	spate = '\033[93m'  # YELLOW
	club = '\033[94m'  # CYAN
	RESET = '\033[0m'  # RESET COLOR

class Card:
	''' Represents a single playing card '''
	
	def __init__(self, suit, rank):
		if suit in suits and rank in ranks:
			self.suit = suit
			self.rank = rank
			self.value = self.set_value(self.rank)
	
	def __str__(self):
		
		if self.suit == '\u2666':
			card = f'{bcolors.diamond}{self.suit}{self.rank}{bcolors.RESET} '
		elif self.suit == '\u2665':
			card = f'{bcolors.heart}{self.suit}{self.rank}{bcolors.RESET} '
		elif self.suit == '\u2660':
			card = f'{bcolors.spate}{self.suit}{self.rank}{bcolors.RESET} '
		elif self.suit == '\u2663':
			card = f'{bcolors.club}{self.suit}{self.rank}{bcolors.RESET} '
		
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


# card = Card()

class Deck:
	''' Represents a card deck with a blind and a stack '''
	
	def __init__(self):
		self.blind = []
		self.stack = []
		
		for suit in suits:
			for rank in ranks:
				self.blind.append(Card(suit, rank))
	
		self.shuffle_blind()
	
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
		print(f'{str(self.stack[-1])}{(len(self.stack) - 1) * "#"}')
		'''
	
	def put_card_on_stack(self, card):
		self.stack.append(card)
	
	def get_top_card_from_stack(self):
		if self.stack:  # this 'if' statement could be omitted
			return self.stack[-1]


deck = Deck()


class Handdeck:
	''' Represents the players cards with "some" functionality '''
	
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
	
	def get_possible_cards(self):
		self.possible_cards = []
		for card in self.cards:
			if card.suit == deck.get_top_card_from_stack().suit or card.rank == deck.get_top_card_from_stack().rank or card.rank == 'J':
				self.possible_cards.append(card)
		return self.possible_cards


class Player:
	''' Represents a player with cards in hand '''
	
	def __init__(self, name=None):
		self.name = name
		self.hand = Handdeck()
		
		for _ in range(5):
			self.hand.cards.append(deck.blind.pop())
		
		''' open first card on stack '''
		if not deck.stack:
			deck.stack.append(self.hand.cards.pop())
		
		self.hand.possible_cards = self.hand.get_possible_cards()
	
	def show(self):
		self.show_hand()
		self.show_possible_cards()
	
	def show_hand(self):
		print(f'{self.name} holds ({len(self.hand.cards)}) card(s) with [{self.hand.count_points()} points]:')
		cards = ''
		for card in self.hand.cards:
			cards += str(card)
		print(cards)
	
	
	def show_possible_cards(self):
		print(f'{self.name} can play ({len(self.hand.get_possible_cards())}) card(s):')
		possible_cards = ''
		for possible_card in self.hand.possible_cards:
			possible_cards += str(possible_card)
		print(possible_cards)
		
		
		#print(f'{[str(card) for card in self.hand.get_possible_cards()]} --> '
		#      f'[{str(deck.get_top_card_from_stack())}]')
	
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


class Game:
	player_list = []
	number_of_players = 0
	
	def __init__(self):
		self.number_of_players = int(input(f"{bcolors.club}How many players?{bcolors.RESET}"))
		
		for player in range(self.number_of_players):
			self.player_list.append(Player(f'Player-{player}'))
	
	def watch_the_stack(self):
		card = deck.get_top_card_from_stack()
		if card.rank == '7':
			self.player.get_card_from_blind()
		if card.rank == '8':
			self.player.get_card_from_blind()
			self.player.get_card_from_blind()
		if card.rank == '6':
			pass
		if card.rank == 'A':
			
			
			pass
		if card.rank == 'J':
			pass
			
	def play(self):
		
		while True:
			key = input('(1..) player | a: toggle | s: put | x: draw | (q)uit')
		
			if key == 'q':
				break
			
			if key == '1':
				self.player = game.player_list[0]
				game.watch_the_stack()
			if key == '2':
				self.player = game.player_list[1]
				game.watch_the_stack()
			
			if key == 'a' or key == 'd':
				self.player.toggle_possible_cards()
			if key == 's':
				self.player.put_card_on_stack()
			if key == 'x':
				self.player.get_card_from_blind()
			if key == ' ':
				if self.player == game.player_list[0]:
					self.player = game.player_list[1]
				else:
					self.player = game.player_list[0]
			
			deck.show()
			self.player.show()


game = Game()
game.play()

