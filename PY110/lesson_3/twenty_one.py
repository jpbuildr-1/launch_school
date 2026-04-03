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
        - Randomly deal one card to dealer from the available deck, for each card dealt add card value to the dealer value and set the bool in the deck to True
        - End dealer turn when total is greater than or equal to 17
6. If dealer busts, player wins.
    - If the dealer card value is greater than 21 then bust and game ends.
7. Compare cards and declare winner.
    - Player wins if card value is greater than the dealer's card value
    - Dealer wins if card value is greater than player's card value
    - Game is tied if card values are equal
'''
import random
import os

def prompt(phrase):
    print(f'===> {phrase}')

def initialize_deck():
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    card = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'jack': 10, 'queen': 10, 'king': 10, 'ace': [1, 11]}
    return {f"{name} of {suit}": [card[name], name, suit, False] for suit in suits
                      for name in card}

def cards_available(deck):
    return [card for card in deck
                 if deck[card][3] == False]

def deal_hand(deck):
    hand = deal_card(deck) + deal_card(deck)
    return hand

def deal_card(deck):
    card = random.choice(cards_available(deck))
    deck[card][3] = True
    return [card]

def ace_check(deck, hand):
    ['ace of spades', 'ace of clubs', 'ace of hearts', 'ace of diamonds']


def display_board(deck, dealer_hand, player_hand):
    os.system('clear')
    prompt(f"Dealer has: {deck[dealer_hand[0]][1]} and unknown card")
    prompt(f"You have: {' and '.join([deck[card][1] for card in player_hand])}")
    prompt(total_hand(deck, player_hand))


def total_hand(deck, hand):
    total = 0
    ace_count = 0
    for card in hand:
        if deck[card][1] == 'ace':
            ace_count += 1
        else:
            total += deck[card][0]
    if ace_count == 1:
        if total + 11 > 21:
            total = total + 1
        else:
            total = total + 11
    elif ace_count == 2:
        if total + 11 > 21:
            total = total + 1 + 1
        else:
            total = total + 11 + 1
    return total

def twenty_one():
    deck = initialize_deck()
    dealer_hand = deal_hand(deck)
    player_hand = deal_hand(deck)

    display_board(deck, dealer_hand, player_hand)

    prompt("Would you want to hit or stay?")
    hit_or_stay = input()

    while total_hand(deck, player_hand) < 21 and hit_or_stay == 'hit':
        player_hand += deal_card(deck)
        display_board(deck, dealer_hand, player_hand)
        if total_hand(deck, player_hand) > 21:
            prompt('Bust, dealer wins.')
            break
        prompt("Would you want to hit or stay?")
        hit_or_stay = input()
    while total_hand(deck, dealer_hand) < 18:
        dealer_hand += deal_card(deck)
        if total_hand(deck, dealer_hand) > 21:
            prompt('Dealer busts, player wins.')
            break
    display_board(deck, dealer_hand, player_hand)
    


twenty_one()