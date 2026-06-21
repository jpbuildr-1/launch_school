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

class PokerHand:
    def __init__(self, deck):
        self.poker_hand = [deck.draw() for _ in range(5)]

    def print(self):
        for card in self.poker_hand:
            print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"

    def _is_royal_flush(self):
        royal_cards = [10, 'Jack', 'Queen', 'King', 'Ace']
        if not self._is_flush():
            return False
        for card in self.poker_hand:
            if card.rank not in royal_cards:
                return False
        return True

    def _is_straight_flush(self):
        if not self._is_flush():
            return False
        if not self._is_straight():
            return False
        return True

    def _is_four_of_a_kind(self):
        return 4 in self.rank_count().values()

    def _is_full_house(self):
        return 3 in self.rank_count().values() and 2 in self.rank_count().values()

    def _is_flush(self):
        suits = [card.suit for card in self.poker_hand]
        same_suit = suits[0]
        for suit in suits:
            if suit != same_suit:
                return False
        return True

    def _is_straight(self):
        cards = self.sorted_by_rank_value()
        for idx in range(len(cards) - 1):
            if cards[idx] + 1 != cards[idx + 1]:
                return False
        return True

    def _is_three_of_a_kind(self):
        return 3 in self.rank_count().values()

    def _is_two_pair(self):
        return sum(1 for count in self.rank_count().values()
                      if count == 2) == 2

    def _is_pair(self):
        return 2 in self.rank_count().values()

    def sorted_by_rank_value(self):
        return sorted([card.rank_value for card in self.poker_hand])

    def rank_count(self):
        count = {}
        for card in self.poker_hand:
            rank = card.rank
            if rank not in count:
                count[rank] = 1
            else:
                count[rank] += 1
        return count

hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self.cards = cards

# # All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")