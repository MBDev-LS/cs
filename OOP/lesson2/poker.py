import random


class Card():

	RANKNAME = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

	def __init__(self, suit: str, rank: int) -> None:
		self._suit = suit
		self._rank = rank
	
	def get_suit(self):
		return self._suit

	def get_rank(self):
		return self._rank
	
	def __str__(self) -> str:
		return Card.RANKNAME[self._rank] + self._suit[0]


class Deck():
	def __init__(self) -> None:
		self.cards = []

		for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
			for num_rank in range(1, 14):
				self.cards.append(Card(suit, num_rank))
	
	def shuffle(self) -> None:
		random.shuffle(self.cards)

	def take_card(self) -> Card:
		return self.cards.pop()

	def __str__(self) -> str:
		return f'<Deck: {", ".join([str(card) for card in self.cards])}>'

class Player():
	def __init__(self, name, startingBalance) -> None:
		self.name = name
		self.cards = []
		self.balance = startingBalance
		self.bet = 0

	def set_name(self, name) -> None:
		name = name
	
	def get_name(self) -> str:
		self.name
	
	def get_cards(self) -> list:
		return self.cards

	def play_turn(self, currentBet) -> str:
		pass
	
	def __str__(self) -> str:
		return f'<Player: {self.name}, {", ".join([str(card) for card in self.cards])}>'

class Table():
	def __init__(self, startingBalance, *args) -> None:
		self.deck = Deck()
		self.players = []
		self.totalBet = 0
		self.table_cards = []

		

		for name in args:
			if isinstance(name, str):
				self.players.append(Player(name, startingBalance))

		self.big_blind = 10
		self.small_blind = 5

		self.bet = self.small_blind
	
	def take_bet(self, player, amount):
		if player not in self.players:
			raise '[ERROR] Attempted to place bet for player not in game.'
		elif player.balance < amount:
			print(f'{player.name} attempted to bet more than their balance of {player.balance}.')
		
		player.balance -= amount 
		player.bet += amount
		self.totalBet += amount

		print(f'[BET] {player.name} bet {amount}, leaving them with a balance of {player.balance} and a total bet of {player.bet}')

	
	def pre_flop(self):
		self.deck.shuffle()
		for i, player in enumerate(self.players):
			player.cards.extend([self.deck.take_card(), self.deck.take_card()])
			print(f'[CARD TRACKING] {player.name} has the cards: {", ".join([str(card) for card in player.cards])}')
			if i == 0:
				print(f'[BLINDS] {player.name} is the big blind.')
				self.take_bet(player, self.big_blind)
			elif i == 1:
				print(f'[BLINDS] {player.name} is the small blind.')
				self.take_bet(player, self.small_blind)

	def flop(self):
		for i in range(3):
			self.table_cards = self.deck.cards.pop()
	
	def __str__(self) -> str:
		return f'<Table: (table cards: {self.table_cards}) (deck: {self.deck}) (players: {", ".join([str(player) for player in self.players])})>'

table = Table(100, 'Jeff', 'Dave', 'Sally', 'Matt')
table.pre_flop()
table.flop()
print(table)
