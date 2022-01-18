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
    def __init__(self, name) -> None:
        self.name = name
        self.cards = []

    def set_name(self, name) -> None:
        name = name
    
    def get_name(self) -> str:
        self.name
    
    def get_cards(self) -> list:
        return self.cards
    
    def __str__(self) -> str:
        return f'<Player: {self.name}, {", ".join([str(card) for card in self.cards])}'

class Table():
    def __init__(self, *args) -> None:
        self.deck = Deck()
        self.players = []
        for name in args:
            if isinstance(name, str):
                self.players.append(Player(name))
    
    def begin_game(self):
        self.deck.shuffle()
        for player in self.players:
            player.cards.extend([self.deck.take_card(), self.deck.take_card()])

    def __str__(self) -> str:
        return f'<Table: (deck: {self.deck}) (players: {", ".join([str(player) for player in self.players])})>'

table = Table('deck', 'Jeff', 'Dave', 'Sally', 'Matt')
table.begin_game()
print(table)
