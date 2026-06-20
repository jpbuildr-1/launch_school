'''
Update the class to rank the list of cards
input: list of Card objects
output: Card object
for rank the names are singular
rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
state: rank of the card, suit of the card
behavior: 
str
less than
greater than
equality
List changes using state to determine the lowest and highest value
Iterate through list to determine the lowest and highest values

Algo
CREATE AN OBJECT WITH INSTANCE VARIABLES RANK AND SUIT
DEFINE DUNDER METHODS STR, GT, LT, EQ
    str returns the object as a string value "rank of suit"
    lt compare self rank with other rank
    gt compare self rank with other rank
    eq compare self rank with other rank and self suit with other suit
    rank_value property to calculate the integer value of rank
'''

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

cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
print(str(min(cards)) == "2 of Hearts")            # True
print(str(max(cards)) == "Ace of Clubs")           # True     

cards = [Card(5, 'Hearts')]
print(min(cards) == Card(5, 'Hearts'))             # True
print(max(cards) == Card(5, 'Hearts'))             # True
print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

cards = [Card(4, 'Hearts'),
         Card(4, 'Diamonds'),
         Card(10, 'Clubs')]
print(min(cards).rank == 4)                        # True
print(max(cards) == Card(10, 'Clubs'))             # True
print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

cards = [Card(7, 'Diamonds'),
         Card('Jack', 'Diamonds'),
         Card('Jack', 'Spades')]
print(min(cards) == Card(7, 'Diamonds'))           # True
print(max(cards).rank == 'Jack')                   # True
print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

cards = [Card(8, 'Diamonds'),
         Card(8, 'Clubs'),
         Card(8, 'Spades')]
print(min(cards).rank == 8)                        # True
print(max(cards).rank == 8)                        # True