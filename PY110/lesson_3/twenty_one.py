'''
1. Initialize deck
    - 52-card deck as a dictionary where key is name of card and 
      value is a nested list where the number value of card is the 1st element
      and a boolean flag used to check if the card has been deal as the 2nd element
      - suits = spades, clubs, hearts, diamonds
      - names = ace, two, three, four, five, six, seven, eight, nine, ten, jack, queen, king
2. Deal cards to player and dealer
    - Initialize the player_hand to an empty dictionary
    - Initialize the dealer_hand to an empty dictionary
    - Randomly deal two cards to player from the available deck, for each card dealt add card name and value to player_hand and set the bool flag in the deck to True
        - If the card is an Ace then the value is 11
    - Randomly deal two cards to dealer from the available deck, for each card dealt add card name and value to dealer_hand and set the bool flag in the deck to True
        - If the card is an Ace then the value is 11
3. Player turn: hit or stay
    - repeat until bust or stay
        - Randomly deal one card to player from the available deck, for each card dealt add card name and value to player_hand and set the bool flag in the deck to True
            - If the card is an Ace and player_hand contains an Ace
                - Check if player_hand's total value + Ace in hand with a value of 11 + Ace with value of 1 is less than 21 
                    - Then Ace value is 1
                - Check if player_hand's total value + Ace in hand with value of 1 + Ace with a value of 1 is less than 21 
                    - Update Ace in hand value to 1
                    - Ace value is 1
            - If the card is an Ace and player_hand does not contain an Ace
                - If player_hand total value is less than 21 then Ace value is 11 otherwise Ace value is 1
        - End player turn when player decides to stay
4. If player busts, dealer wins.
    - If the player card value is greater than 21 then bust and game ends.
5. Dealer turn: hit or stay
    - repeat until total >= 17
        - Randomly deal one card to player from the available deck, for each card dealt add card value to the player value and set the bool in the deck to True
        - End dealer turn when total is greater than or equal to 17
6. If dealer busts, player wins.
    - If the dealer card value is greater than 21 then bust and game ends.
7. Compare cards and declare winner.
    - Player wins if card value is greater than the dealer's card value
    - Dealer wins if card value is greater than player's card value
    - Game is tied if card values are equal
'''

def initialize_deck():
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    card = {'ace': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'jack': 10, 'queen': 10, 'king': 10}
    return {f"{name} of {suit}": [card[name], False] for suit in suits
                      for name in card}
def twenty_one():
    deck = initialize_deck()

twenty_one()