'''
52 card deck
Deck shuffle at initializaiton
draw method that deals one card
    if no more then generate a new set of 52 shuffled cards
'''
import random

class Card:
    RANK_VALUES = {
        2: 2, 
        3: 3, 
        4: 4, 
        5: 5, 
        6: 6, 
        7: 7, 
        8: 8, 
        9: 9, 
        10: 10, 
        'Jack': 11,
        'Queen': 12,
        'King': 13,
        'Ace': 14,
        }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank_value < other.rank_value

    def __eq__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    @property
    def rank_value(self):
        return self.RANK_VALUES[self.rank]

class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):
        self.create_deck()

    def draw(self):
        if self.cards:
            return self.cards.pop()
        self.create_deck()
        return self.cards.pop()

    def create_deck(self):
        self.cards = [Card(rank, suit) for suit in self.SUITS
                                       for rank in self.RANKS]
        random.shuffle(self.cards)
        return self.cards

deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).