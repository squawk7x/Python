import random
import keyboard



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
		
		sign = f'{self.color}{self.suit}{self.suit}{reset_color} '
		
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
		self.bridge = []
		self.shufflings = 1
		
		for suit in suits:
			for rank in ranks:
				self.blind.append(Card(suit, rank))
	
		self.shuffle_blind()
	
	''' deck methods '''
	
	def show(self):
		self.show_blind()
		self.show_bridge_monitor()
		self.show_stack()
	
	''' blind methods '''
	
	def show_blind(self):
		blind = ''
		for card in self.blind:
			blind += str(card)
		print(f'Blind ({len(self.blind)}) card(s):')
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
			self.shufflings += 1
		random.shuffle(self.blind)
		if self.blind:
			return self.blind.pop()
	
	''' stack methods '''
	
	def show_stack(self):
		stack = ''
		for card in self.stack:
			stack += str(card)
		print(f'Stack ({len(self.stack)}) card(s):')
		print(f'{stack}{jchoice.get_j()}')
	
	def put_card_on_stack(self, card):
		self.stack.append(card)
	
	def get_top_card_from_stack(self):
		if self.stack:
			return self.stack[-1]

	''' bridge monitor '''
	
	def check_is_bridge(self, card: Card):
		
		if card.rank != deck.bridge[0].rank:
			deck.bridge.clear()
		deck.bridge.append(card)
		if len(deck.bridge) == 4:
			return True
		else:
			return False
		
	def show_bridge_monitor(self):
		bridge = ''
		for card in self.bridge:
			bridge += str(card)
		print(f'Bridge monitor ({len(self.bridge)}) card(s):')
		print(f'{bridge}')
		
deck = Deck()


class Handdeck:
	''' Represents the players cards with 'some' functionality '''
	
	def __init__(self):
		self.cards = []
		self.cards_drawn = []
		self.cards_played = []
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
		stack_card = deck.get_top_card_from_stack()
		
		'''
		1st move:
		---------
		suit    rank    J
		
		stack_card = '6'
		suit    rank    J
		
		stack_card = 'J'
		suit            J
		
		2nd move:
		---------
				rank
		
		stack_card = '6'
		suit    rank    J
		
		stack_card 'J':
		suit            J
		
		'''
		
		if not self.cards_played:
			
			if stack_card.rank == 'J':
				for card in self.cards:
					if card.suit == jchoice.get_j_suit() or card.rank == 'J':
						self.possible_cards.append(card)
			
			else:
				for card in self.cards:
					if card.rank == stack_card.rank or card.suit == stack_card.suit or card.rank == 'J':
						self.possible_cards.append(card)
		
		if self.cards_played:
			if stack_card.rank == '6':
				for card in self.cards:
					if card.rank == stack_card.rank or card.suit == stack_card.suit or card.rank == 'J':
						self.possible_cards.append(card)
				
			elif stack_card.rank == 'J':
				for card in self.cards:
					if card.suit == jchoice.get_j_suit() or card.rank == 'J':
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
	
	def __init__(self, name=None):
		self.name = name
		self.hand = Handdeck()
		
		''' draw the initial 5 cards'''
		self.draw_5_cards()
	
		''' open first card on stack Player 0'''
		self.put_initial_card()
	
	def draw_5_cards(self):
		self.hand.cards = []
		self.hand.cards_played = []
		self.hand.cards_drawn = []
		
		for _ in range(5):
			card = deck.blind.pop()
			self.hand.cards.append(card)
			
	def put_initial_card(self):
		if not deck.stack:
			card = self.hand.cards.pop()
			deck.put_card_on_stack(card)
			self.hand.cards_played.append(card)
			deck.bridge.append(card)
			
	def show(self):
		self.show_possible_cards()
		self.show_hand()
	
	def show_hand(self):
		cards = ''
		for card in self.hand.cards:
			cards += str(card)
		print(f'{self.name} holds ({len(self.hand.cards)}) card(s) [{self.hand.count_points()} points]:')
		print(cards)
	
	def show_possible_cards(self):
		cards = ''
		self.hand.possible_cards = self.hand.get_possible_cards()
		for card in self.hand.possible_cards:
			cards += str(card)
		print(f'{self.name} has played ({len(self.hand.cards_played)}) / drawn ({len(self.hand.cards_drawn)}) card(s)'
		      f' and can play ({len(self.hand.possible_cards)}) card(s):')
		print(cards)
	
	def toggle_possible_cards(self):
		if self.hand.possible_cards:
			card = self.hand.possible_cards.pop()
			self.hand.cards.remove(card)
			self.hand.cards.insert(0, card)
			self.hand.possible_cards.insert(0, card)
	
	def get_card_from_blind(self):
		if deck.blind:
			card = deck.draw_card_from_blind()
			self.hand.cards.append(card)
			self.hand.cards_drawn.append(card)
	
	def put_card_on_stack(self):
		if self.hand.possible_cards:
			card = self.hand.possible_cards.pop()
			self.hand.cards.remove(card)
			deck.put_card_on_stack(card)
			self.hand.cards_played.append(card)
			deck.check_is_bridge(card)
			jchoice.clear_j()


class Game:
	player = None
	number_of_players = 3
	player_list = []
	cards_for_evaluation = []
	scores = {}
	
	def __init__(self):
		
		while True:
			
			try:
				print("Enter number of players:")
				self.number_of_players = int(keyboard.read_key())
			except ValueError:
				print('Valid number, please')
				continue
			if 1 <= self.number_of_players <= 4:
				break
			else:
				print('Please enter value between 1 and 4')
		
		
		self.new_round()
		
	def new_round(self, shuffler=0):
		
		global deck
		
		deck = Deck()
		deck.shuffle_blind()
		
		if not self.player_list or len(self.player_list) != self.number_of_players:
			for player in range(self.number_of_players):
				self.player_list.append(Player(f'Player-{player + 1}'))
		
		if not self.scores:
			for player in self.player_list:
				self.scores[player] = 0
				
		for player in self.player_list:
			player.draw_5_cards()
		
		self.player = self.player_list[shuffler]
		self.player.put_initial_card()

	
	def activate_next_player(self):
		self.cards_for_evaluation = self.player.hand.cards_played
		self.player.hand.cards_played = []  # preparation for next turn
		self.player_list.append(self.player_list.pop(0))  # get actual player to the end of playerlist
		self.player = self.player_list[0]  # next player now on position 0
		self.player.hand.cards_drawn = []
	
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
	
		
	def show_scores(self, bridge=False):
		if bridge:
			self.activate_next_player()
			self.evaluate()
		
		if not self.player.hand.cards:
			print(f'The winner of this round is {self.player.name}')
			print('')
			
		for player in self.scores.keys():
			self.scores[player] += player.hand.count_points()  # * deck.shufflings
			if self.scores[player] == 125:
				self.scores[player] = 0
			print(player.name, " --> ", self.scores[player])
		looser = sorted(self.scores.items(), key=lambda kv: (kv[1], kv[0])).pop()
		print(f'The new shuffler for next round is {looser[0].name}')
	
	def play(self):
		self.new_round(shuffler=0)
		deck.show()
		self.player.show()
		
		while self.player.hand.cards:
			
			print('a: toggle | s: put | x: draw | space: next Player | o: scores | r: new round | (q)uit game')
			
			if keyboard.read_key() == '8':
				for suit in suits:
					self.player.hand.cards.append(Card(suit, '8'))
			if keyboard.read_key() == 'q':
				break
			if keyboard.read_key() == 'r':
				deck.bridge = []
				self.new_round(shuffler=1)
			if keyboard.read_key() == 'o':
				self.show_scores()
			if keyboard.read_key() == 'a':
				self.player.toggle_possible_cards()
			if keyboard.read_key() == 's':
				self.player.put_card_on_stack()
		
			if keyboard.read_key() == 'x':
				
				'''
				pull card possible, (not '6' on stack) if:
				------------------------------------------
				
				 card   possible  card
				played    cards   drawn
					1       1       1       N
					1       1       0       N
					1       0       1       N
					1       0       0       N
					0       1       1       N
					0       1       0       N
					0       0       1       N
					0       0       0       Y
					
				'6' on stack:
				-------------
							1               Y
				
				'''
				
				stack_card = deck.get_top_card_from_stack()
				
				if stack_card.rank == '6' and not self.player.hand.possible_cards:
					self.player.get_card_from_blind()
				
				elif not self.player.hand.cards_played and not self.player.hand.possible_cards and not self.player.hand.cards_drawn:
					self.player.get_card_from_blind()
					
				else:
					pass
				
			if keyboard.read_key() == 'space':
				
				'''
				next player possible, (no 6 on stack) if:
				
				 card   possible  card    next
				played    cards   drawn   player
					1       1       1       Y
					1       1       0       Y
					1       0       1       Y
					1       0       0       Y
					0       1       1       N
					0       1       0       N
					0       0       1       Y
					0       0       0       N
				'''
				
				if self.player.hand.cards_played:
					
					if deck.get_top_card_from_stack().rank == '6':
						pass
					
					elif deck.get_top_card_from_stack().rank == 'J':
						jchoice.show_js()
						while True:
							print('a: toggle color | space: set color')
							if keyboard.read_key() == 'a':
								jchoice.toggle_js()
								jchoice.show_js()
							if keyboard.read_key() == 's':
								jchoice.set_j()
								break
						self.activate_next_player()
						self.evaluate()
				
					else:
						self.activate_next_player()
						self.evaluate()
				
				if not self.player.hand.cards_played:
					
					if self.player.hand.possible_cards:
						pass
					
					elif not self.player.hand.possible_cards and self.player.hand.cards_drawn:
						self.activate_next_player()
						self.evaluate()
					
					elif not self.player.hand.possible_cards and not self.player.hand.cards_drawn:
						pass
			
			deck.show()
			self.player.show()
		
		self.show_scores()


game = Game()
game.play()
