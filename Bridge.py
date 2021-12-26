'''
TODO:
blind refill
bridge
round -125

'''

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
		self.evaluation = []
		self.shufflings = 1
		
		for suit in suits:
			for rank in ranks:
				self.blind.append(Card(suit, rank))
		
		self.shuffle_blind()
	
	''' deck methods '''
	
	def show(self):
		self.show_blind()
		self.show_cards_for_evaluation()
		self.show_bridge_monitor()
		self.show_stack()
	
	''' blind methods '''
	
	def show_blind(self):
		blind = ''
		for card in self.blind:
			 blind += str(card)
			#blind += '## '
		blind += '\n'
		print(f'{20 * " "}Blind ({len(self.blind)}) card(s):')
		print(f'{20 * " "}{blind}')
		
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
		'''
		stack = ''
		for card in self.stack:
			stack += str(card)
		print(f'Stack ({len(self.stack)}) card(s):')
		print(f'{stack}{jchoice.get_j()}')
		'''
		stack = ''
		stack += f'{20 * " "}{jchoice.get_j()}{(self.stack[-1])}'
		for card in range(len(self.stack) - 1):
			stack += 'XX '
		print(f'{20 * " "}Stack ({len(self.stack)}) card(s):')
		print(stack)
	
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
	
	def append_card_for_evaluation(self, card: Card):
		if card.rank in {'7', '8', 'A'}:
			self.evaluation.append(card)
	
	def remove_card_from_evaluation(self, card):
		self.evaluation.remove(card)
	
	def show_cards_for_evaluation(self):
		evaluation = ''
		for card in self.evaluation:
			evaluation += str(card)
		print(f'Cards for evaluation ({len(self.evaluation)}) card(s):')
		print(f'{evaluation}')


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
			self.hand.cards.append(deck.blind.pop())
	
	def put_initial_card(self):
		if not deck.stack:
			card = self.hand.cards.pop()
			deck.put_card_on_stack(card)
			self.hand.cards_played.append(card)
			deck.append_card_for_evaluation(card)
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
	
	def play_card(self):
		if self.hand.possible_cards:
			card = self.hand.possible_cards.pop()
			self.hand.cards.remove(card)
			deck.put_card_on_stack(card)
			self.hand.cards_played.append(card)
			deck.append_card_for_evaluation(card)
			jchoice.clear_j()
			deck.check_is_bridge(card)


class Bridge:
	'''
	
	Rules Of The Game
	--------------
	Bridge is played with 36 cards (4 suits and ranks from 6 to Ace) by 2-4 players.
	Each player starts with 5 cards from blind. First player puts a card onto the stack
	and can add more cards with same rank. The next player can play first card either
	same suit or same rank and can play more cards with same rank. First the cards on hand
	must be used and at least 1 card must be played or must be drawn from blind.
	No more than one card can be drawn from blind, except a '6' must be covered.
	
	Special Cards:
	--------------
	6   must be covered by same player
	7   next player gets 1 card from blind
	8   next player gets 2 cards from blind and will be passed over
	J   can be played to any suit and player can choose what suit must follow
	Ace next player will be passed over. With multiple aces the next players will be passed over
	
	Special Rule 'Bridge':
	----------------------
	If there are the same 4 cards in a row on the stack, the player of the 4th card can choose wether or not
	to finish tha actual round.
	
	Counting:
	---------
	A round is over when one player has no more cards.
	The players note their points:
						
							 6   0
							 7   0
							 8   0
							 9   0
							10  10
							J   20
							Q   10
							K   10
							A   15

	The points for several rounds will be added.
	If the blind was empty and reshuffeled, the points of this round are doubled.
	If a player finishes a round with a 'J' his score will be reduced by 20 for each 'J' of this last move.
	If a player reaches exactly 125 points, his score is back on 0!
	
	The game is over when one player has more than 125 points.
	
	'''
	
	player = None
	number_of_players = 3
	player_list = []
	scores = {}
	
	def __init__(self):
		
		while True:
			
			try:
				print("Enter number of players:")
				self.number_of_players = int(keyboard.read_hotkey(False))
				self.number_of_players = 3
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
		self.player.hand.cards_played = []  # this player preparation for next turn
		self.player.hand.cards_drawn = []  # this player preparation for next turn
		self.player_list.append(self.player_list.pop(0))
		self.player = self.player_list[0]  # next player activated
		self.evaluate()
	
	def evaluate(self):
		leaps_for_ace = 0
		leaps_for_eight = 0
		
		for card in deck.evaluation:
			
			if card.rank == '7':
				self.player.get_card_from_blind()
			if card.rank == '8':
				self.player.get_card_from_blind()
				self.player.get_card_from_blind()
				leaps_for_eight = 1
			if card.rank == 'A':
				leaps_for_ace += 1
				
		deck.evaluation = []
		
		for _ in range(leaps_for_eight + leaps_for_ace):
			self.activate_next_player()
	
	def show_other_players(self, player: Player):
		other_players = ''
		for p in self.player_list:
			if p != player:
				other_players += f'\n{38 * " "}| {p.name} holds ({len(p.hand)}) card(s)'
				p.show_hand()
				
		other_players += '\n'
		print(other_players)
	
	def show_scores(self, round_count = False, bridge=False):
		if bridge:
			self.activate_next_player()
		
		if round_count:
			print(f'\nScores this round:\n{18*"-"}')
			for player in self.scores.keys():
				self.scores[player] += player.hand.count_points() * deck.shufflings
				if self.scores[player] == 125:
					self.scores[player] = 0
				print(player.name, " --> ", self.scores[player])
			print(f'{18* "-"}')
			
		else:
			print(f'\nLast Scores:\n{18*"-"}')
			for player in self.scores.keys():
				print(player.name, " --> ", self.scores[player])
			print(f'{18*"-"}')
		
	def play(self):
		self.new_round(shuffler=0)
		self.show_other_players(self.player)
		deck.show()
		self.player.show()
		
		
		while True:  # self.player.hand.cards:
			
			print('TAB: toggle | CAPS: put | SHIFT: draw | SPACE: next Player | o: scores | r: new round | (q)uit game')
			
			key = keyboard.read_hotkey(False)
			
			if key == '8':
				for suit in suits:
					self.player.hand.cards.append(Card(suit, '8'))
			if key == 'q':
				break
			if key == 'r':
				deck.bridge = []
				self.new_round(shuffler=1)
			if key == 'o':
				self.show_scores()
			if key == 'tab':
				self.player.toggle_possible_cards()
			if key == 'caps lock':
				self.player.play_card()
			
			if key == 'shift':
				
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
			
			if key == 'space':
				
				'''
				next player possible, (no 6 on stack) if:
				
				 card   possible  card    next
				played    card    drawn   player
					1       1       1       Y
					1       1       0       Y
					1       0       1       Y
					1       0       0       Y
					0       1       1       N
					0       1       0       N
					0       0       1       Y
					0       0       0       N
				'''
				
				next_player = False
				
				if self.player.hand.cards_played:
					
					if deck.get_top_card_from_stack().rank == '6':
						next_player = False
					
					elif deck.get_top_card_from_stack().rank == 'J':
						
						while True:
							print('===========')
							jchoice.show_js()
							print('TAB: toggle color | SPACE: set color / next player')
							jkey = keyboard.read_hotkey(False)
							
							if jkey == 'tab':
								jchoice.toggle_js()
								deck.show()
								self.player.show()
							
							if jkey == 'space':
								jchoice.set_j()
								break
						
						next_player = True
					
					else:
						next_player = True
				
				if not self.player.hand.cards_played:
					
					if self.player.hand.possible_cards:
						next_player = False
					
					if not self.player.hand.possible_cards and self.player.hand.cards_drawn:
						next_player = True
					
					if not self.player.hand.possible_cards and not self.player.hand.cards_drawn:
						next_player = False
				
				if next_player:
					self.activate_next_player()
			
			self.show_other_players(self.player)
			deck.show()
			self.player.show()
		
		
		self.activate_next_player()  # last round will be counted
		self.show_scores(round_count=True)
		self.new_round()
		print('GAME OVER')


bridge = Bridge()
bridge.play()
