<<<<<<< HEAD
from os import close
from platform import system
import random
from datetime import date
=======
from platform import system
import random
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
import keyboard
from pynput import mouse

suits = ['\u2666', '\u2665', '\u2660', '\u2663']
ranks = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suit_colors = ['\033[95m', '\033[91m', '\033[93m', '\033[94m']
reset_color = '\033[0m'


class Card:
	# Represents a single playing card
	
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
<<<<<<< HEAD
		if rank in {'10', 'Q', 'K'}:
			value = 10
		if rank == 'A':
			value = 15
		if rank == 'J':
			value = 20
=======
		if rank in {'10', 'Q', 'K'}: value = 10
		if rank == 'A': value = 15
		if rank == 'J': value = 20
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
		return value
	
	def get_value(self):
		return self.value


class Jsuit:
	# Represents the suit to choose for 'J'
	
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
	# array of suits for 'J'
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
		print(11 * " " + js)


jchoice = Jchoice()


class Deck:
	# Represents a card deck with a blind and a stack
	
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
	
	# deck methods
	
	def show(self):
		self.show_blind(open=False)
		self.show_cards_for_evaluation()
		self.show_bridge_monitor()
		self.show_stack()
	
	# blind methods
	
	def show_blind(self, open=True):
		blind = ''
		for card in self.blind:
			if open:
				blind += str(card)
			else:
				blind += '## '
		
		print(f'\n{20 * " "}Blind ({len(self.blind)}) card(s):')
		print(f'{20 * " "}{blind}\n')
	
	def shuffle_blind(self):
		random.shuffle(self.blind)
	
	def card_from_blind(self):
		if len(self.blind) == 0:
			self.blind = self.stack
			self.stack = []
			self.stack.append(self.blind.pop())
			# for c in range(len(self.stack) - 1):
			#	self.blind.append(self.stack.pop())
			random.shuffle(self.blind)
			self.shufflings += 1
		if self.blind:
			return self.blind.pop()
		else:
			print('not enough cards available')
	
	# stack methods
	
	def show_stack(self):
		stack = ''
		stack += f'{20 * " "}{jchoice.get_j()}{(self.stack[-1])}'
		for card in range(len(self.stack) - 1):
			stack += 'XX '
		print(f'{20 * " "}Stack ({len(self.stack)}) card(s):')
		print(f'{stack}\n')
	
	def put_card_on_stack(self, card):
		self.stack.append(card)
	
	def get_top_card_from_stack(self):
		if self.stack:
			return self.stack[-1]
	
	#  bridge monitor
	
	def update_bridge_monitor(self, card: Card):
		if card.rank != deck.bridge[0].rank:
			deck.bridge.clear()
		deck.bridge.append(card)
	
	def show_bridge_monitor(self):
		bridge = ''
		for card in self.bridge:
			bridge += str(card)
		print(f'Bridge monitor ({len(self.bridge)}) card(s):')
		print(f'{bridge}')
	
	def check_is_bridge(self):
<<<<<<< HEAD
		if len(deck.bridge) == 4:
=======
		if len(deck.bridge) >= 4:
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
			return True
		else:
			return False
	
	# evaluation monitor
	
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
<<<<<<< HEAD
	''' Represents the player's cards with some functionality '''
=======
	''' Represents the players cards with 'some' functionality '''
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
	
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
	score = 0
	
	def __init__(self, name=None):
		self.name = name
		self.hand = Handdeck()
	
	def __lt__(self, other):
		if self.score < other.score:
			return True
		else:
			return False
<<<<<<< HEAD
	
=======
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
	'''
	def __eq__(self, other):
		if self.score == other.score:
			return True
		else:
			return False
	'''
	
	def __gt__(self, other):
		if self.score > other.score:
			return True
		else:
			return False
	
	def draw_new_cards(self):
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
	
	def show_hand(self, open=True):
		cards = ''
		for card in self.hand.cards:
			if open:
				cards += str(card)
<<<<<<< HEAD
			else:
				cards += '## '
		print(
			f'{self.name} holds ({len(self.hand.cards)}) card(s) [{self.hand.count_points()} points]:')
=======
			else: 
				cards += '## '
		print(f'{self.name} holds ({len(self.hand.cards)}) card(s) [{self.hand.count_points()} points]:')
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
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
	
<<<<<<< HEAD
	def get_card_from_blind(self, cards=1):
		for card in range(cards):
			card = deck.card_from_blind()
			self.hand.cards.append(card)
			self.hand.cards_drawn.append(card)
=======
	def get_card_from_blind(self):
		card = deck.card_from_blind()
		self.hand.cards.append(card)
		self.hand.cards_drawn.append(card)
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
	
	def play_card(self):
		if self.hand.possible_cards:
			card = self.hand.possible_cards.pop()
			deck.update_bridge_monitor(card)
			self.hand.cards.remove(card)
			deck.put_card_on_stack(card)
			self.hand.cards_played.append(card)
			deck.append_card_for_evaluation(card)
			jchoice.clear_j()


class Bridge:
	'''
	Game of Bridge

	Rules Of The Game:
	------------------
	Bridge is played with 36 cards (4 suits and ranks from 6 to Ace) by 2-4 players.
	Each player starts with 5 cards from blind. First player puts a card onto the stack
	and can add more cards with same rank. The next player can play first card either
	same suit or same rank and can play more cards with same rank. First the cards on hand
	must be used and at least 1 card must be played or must be drawn from blind.
	No more than one card can be drawn from blind, except a '6' must be covered.

	Special Cards:
	--------------
	6   must be covered by same player, drawing cards until possible move
	7   next player gets 1 card from blind
	8   next player gets 2 cards for each '8' from blind and will be passed over
	J   can be played to any suit and player can choose which suit must follow
	A   next player will be passed over. With multiple 'A' the next players will be passed over

	Special Rule 'Bridge':
	----------------------
	If there are the same 4 cards in a row on the stack, the player of the 4th card can choose whether or not
	to finish the actual round.

	Counting:
	---------
	A round is over when one player has no more cards.
	The players note their points:

<<<<<<< HEAD
													 6   0
													 7   0
													 8   0
													 9   0
													10  10
													J   20  (-20)
													Q   10
													K   10
													A   15
=======
							 6   0
							 7   0
							 8   0
							 9   0
							10  10
							J   20  (-20)
							Q   10
							K   10
							A   15
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)

	The points of several rounds will be added.
	If the blind was empty and the stack was reshuffeled, the points of this round are doubled, tripled, ...
	If a player finishes a round with a 'J' his score will be reduced by 20 for each 'J' of this last move.
	If a player reaches exactly 125 points, his score is back on 0!
	The player with the highest score starts the next round.

	The game is over once a player reaches more than 125 points.
	'''
	
	player = None
	number_of_players = 0
	player_list = []
	number_of_rounds = 0
<<<<<<< HEAD
	number_of_games = 0
=======
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
	shuffler = None
	
	def __init__(self):
		
		while True:
			
			try:
				print("Enter number of players:")
				self.number_of_players = int(keyboard.read_hotkey(False))
			except ValueError:
				print('Valid number, please')
				continue
			if 1 <= self.number_of_players <= 6:
				break
			else:
				print('Please enter value between 1 and 6')
	
<<<<<<< HEAD
	# self.start_round()
=======
	#self.start_round()
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
	
	def start_round(self):
		
		deck.__init__()
		
		if self.player_list == []:
			self.number_of_rounds = 0
			for player in range(self.number_of_players):
				self.player_list.append(Player(f'Player-{player + 1}'))
		
		self.number_of_rounds += 1
		
		for player in self.player_list:
			player.draw_new_cards()
		
		self.set_shuffler()
		self.player = self.get_shuffler()
		self.player.put_initial_card()
	
	def set_shuffler(self):
		if self.shuffler == None:
			self.shuffler = self.player_list[0]
		else:
			self.shuffler = max(self.player_list)
<<<<<<< HEAD
	
	# self.shuffler = (sorted(self.player_list, key=lambda player: player.score)).pop()
=======
			#self.shuffler = (sorted(self.player_list, key=lambda player: player.score)).pop()
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
	
	def get_shuffler(self):
		return self.shuffler
	
	def activate_next_player(self):
		self.player.hand.cards_played = []  # this player preparation for next turn
		self.player.hand.cards_drawn = []  # this player preparation for next turn
		self.player_list.append(self.player_list.pop(0))
		self.player = self.player_list[0]  # next player activated
		self.evaluate()
	
	def evaluate(self):
<<<<<<< HEAD
		aces = 0
		eights = 0
=======
		leaps_for_ace = 0
		leaps_for_eight = 0
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
		
		for card in deck.evaluation:
			
			if card.rank == '7':
				self.player.get_card_from_blind()
				self.player.hand.cards_drawn.clear()
			if card.rank == '8':
<<<<<<< HEAD
				eights += 1
			if card.rank == 'A':
				aces += 1
		
		deck.evaluation.clear()
		
		if eights == 1 or (eights and self.number_of_players == 2):
			for eight in range(eights):
				self.player.get_card_from_blind(2)
			self.player.hand.cards_drawn.clear()
			self.activate_next_player()
		
		elif eights >= 2:
			print(f"\n{13 * ' '}? ? ? How to share the 8's ? ? ?\n")
			print(f'{13 * " "}| (n)ext player | (a)ll players |\n')
			key = keyboard.read_hotkey(False)
			if key == 'n':
				for eight in range(eights):
					self.player.get_card_from_blind(2)
				self.player.hand.cards_drawn.clear()
				self.activate_next_player()
			if key == 'a':
				leap = 1
				while leap <= eights:
					if leap != self.number_of_players:
						self.player.get_card_from_blind(2)
						self.player.hand.cards_drawn.clear()
					else:
						eights += 1
					leap += 1
					self.activate_next_player()
		
		'''
		#Player/A	1	2	3	4

			2		1	3	1	3
			3		1	2	4	2
			4		1	2	3	5
			5		1	2	3	4
			6		1	2	3	4
		'''
		if aces > self.number_of_players:
			aces -= 2
		if aces == self.number_of_players:
			aces += 1
		for ace in range(aces):
=======
				self.player.get_card_from_blind()
				self.player.get_card_from_blind()
				self.player.hand.cards_drawn.clear()
				leaps_for_eight = 1
			if card.rank == 'A':
				leaps_for_ace += 1
		
		deck.evaluation = []
		
		for _ in range(leaps_for_eight + leaps_for_ace):
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
			self.activate_next_player()
	
	def show_other_players(self, player: Player):
		for p in self.player_list:
			if p != player:
				p.show_hand(open=False)
<<<<<<< HEAD
	
	def finish_round(self):
		
=======

	def finish_round(self):

>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
		if deck.get_top_card_from_stack().rank == 'J':
			self.player.score -= 20 * len(deck.bridge) * deck.shufflings
		
		self.activate_next_player()  # evaluation of last round
		
		for player in self.player_list:
			player.score += player.hand.count_points() * deck.shufflings
			if player.score == 125:
				player.score = 0
			player.show_hand(open=True)
		
<<<<<<< HEAD
		list = sorted(self.player_list, key=lambda player: player.name)
		try:
			f = open(f'{date.today()}_scores.txt')
		except IOError:
			f = open(f'{date.today()}_scores.txt', 'a')
			f.write(f'\n\nGame - Round   ')
			for player in list:
				f.write(f'{player.name} ')
			f.write('\n')
		finally:
			f.close()
			with open(f'{date.today()}_scores.txt', 'a') as f:
				f.write(f'  {self.number_of_games:2d} -{self.number_of_rounds:2d}{7 * " "}')
				for player in list:
					f.write("  {:3d}    ".format(player.score))
				f.write('\n')
		
		self.show_scores()
		
=======
		self.show_scores()

>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
		self.set_shuffler()
		if self.shuffler.score <= 125:
			print(f'{self.shuffler.name} will start next round')
			self.start_round()
		else:
			print(f'\nThe Winner is ...\n')
<<<<<<< HEAD
			# winner = sorted(self.player_list, key=lambda player: player.score, reverse=True).pop()
			print(f'{18 * " "}{min(self.player_list).name}\n')
			print(f'{27 * " "}+ + + G A M E  O V E R + + + \n')
			print(f'{34 * " "}| (n)ew game |\n')
			keyboard.wait('n')
			self.number_of_games += 1
	
	def show_scores(self):
		try:
			with open(f'{date.today()}_scores.txt') as f:
				for line in f:
					print(line, end='')
				print('\n')
		except IOError:
			print('\n\nPlaying 1st round - No score list availabe yet')
		
		print(f"(r)eturn\n")
		keyboard.wait('r')
	
	def play(self):
		self.number_of_games += 1
		
		self.start_round()
		
		while True:
			print(f'\n{100 * "-"}')
=======
			#winner = sorted(self.player_list, key=lambda player: player.score, reverse=True).pop()
			print(f'{16*" "}{min(self.player_list).name}\n')
			print(f'{13*" "}G A M E  O V E R')
			print(f'{7*" "}| n: new game | q:uit game |')
			keyboard.wait('n')
		
	def show_scores(self):
		
		print(f'\n Scores (round {self.number_of_rounds})\n{19 * "-"}')
		for player in self.player_list:
			print(f' {player.name} -->  '"{:3d}".format(player.score))
		print(f"{19 * '-'}\n return with 'e'\n")
		
		keyboard.wait('e')
	
	def play(self):
		self.start_round()

		while True:
			print(f'\n{100*"-"}')
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
			self.show_other_players(self.player)
			deck.show()
			self.player.show()
			
			print(
				'\n| TAB: toggle | SHIFT: put | ALT: draw | SPACE: next Player | s: scores | n: new game | q:uit game |')
<<<<<<< HEAD
			
			key = keyboard.read_hotkey(False)
			
			'''
			def on_click(x, y, button, pressed):

				if button == mouse.Button.left:
					keyboard.send('shift')

				if button == mouse.Button.middle:
					keyboard.send('space')

				if button == mouse.Button.right:
					keyboard.send('alt')

			def on_scroll(x, y, dx, dy):
				keyboard.send('tab')

			with mouse.Listener(
					on_click=on_click,
					on_scroll=on_scroll) as listener:
					listener.start()
			'''
			if key == 'c':
				for suit in suits:
					self.player.hand.cards.clear()
=======

			key = keyboard.read_hotkey(False)
			
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
			if key == 'j':
				for suit in suits:
					self.player.hand.cards.append(Card(suit, 'J'))
			if key == '8':
				for suit in suits:
					self.player.hand.cards.append(Card(suit, '8'))
<<<<<<< HEAD
			if key == 'a':
				for suit in suits:
					self.player.hand.cards.append(Card(suit, 'A'))
=======
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
			elif key == 'q':
				break
			elif key == 'n':
				self.player_list = []
				self.start_round()
			elif key == 's':
				self.show_scores()
			elif key == 'tab':
				self.player.toggle_possible_cards()
			elif key == 'alt':
<<<<<<< HEAD
				
				'''
				pull card possible, (not '6' on stack) if:
				------------------------------------------
						card   possible  card
				played    card    drawn
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
=======

				'''
				pull card possible, (not '6' on stack) if:
				------------------------------------------
					card   possible  card
				played    card    drawn
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
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
				'''
				
				stack_card = deck.get_top_card_from_stack()
				
				if stack_card.rank == '6' and not self.player.hand.possible_cards:
					self.player.get_card_from_blind()
				
				elif not self.player.hand.cards_played and not self.player.hand.possible_cards and not self.player.hand.cards_drawn:
					self.player.get_card_from_blind()
				
				else:
					pass
			
			if key == 'shift':
				self.player.play_card()
				if not self.player.hand.cards:
					self.finish_round()
			
			if key == 'space':
				
				'''
				next player possible, (no 6 on stack) if:

<<<<<<< HEAD
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
=======
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
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
				'''
				
				next_player = False
				
				if deck.check_is_bridge():
<<<<<<< HEAD
					print(f'\n{17 * " "}* * * B R I D G E * * *\n')
=======
					print(f'\n{17*" "}* * * B R I D G E * * *\n')
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
					print(f'{24 * " "}| Y | N |\n')
					key = keyboard.read_hotkey(False)
					if key == 'n':
						pass
					if key == 'y':
						self.finish_round()
				
				if self.player.hand.cards_played:
					
					if deck.get_top_card_from_stack().rank == '6':
						next_player = False
					
					elif deck.get_top_card_from_stack().rank == 'J':
<<<<<<< HEAD
						
						print(f'\n{20 * " "}\u2191\u2191')
						jchoice.show_js()
						print(
							f'{5 * " "}| TAB: toggle color | SPACE: set color / next player |')
						
						while True:
							jkey = keyboard.read_hotkey(False)
							
=======

						print(f'\n{20 * " "}\u2191\u2191')
						jchoice.show_js()
						print(f'{5* " "}| TAB: toggle color | SPACE: set color / next player |')
						
						while True:
							jkey = keyboard.read_hotkey(False)

>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
							if jkey == 'tab':
								jchoice.toggle_js()
								deck.show()
								self.player.show()
								print(f'\n{20 * " "}\u2191\u2191')
								jchoice.show_js()
<<<<<<< HEAD
								print(
									f'{5 * " "}| TAB: toggle color | SPACE: set color / next player |')
							
=======
								print(f'{5* " "}| TAB: toggle color | SPACE: set color / next player |')
								
>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
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


<<<<<<< HEAD
if __name__ == "__main__":
	bridge = Bridge()
	bridge.play()
=======
bridge = Bridge()

bridge.play()

>>>>>>> adb6adc (20211231-09:07 Game of Bridge)
