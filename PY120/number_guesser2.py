'''
Create a GuessingGame class for number between 1 - 100
7 guesses per game
Show remaining guesses
Output 'Enter a number between 1 and 100': user inputs a number
Check guess to see that it is valid then Output 'Enter a number between 1 and 100': user inputs a number doesn't count as guess
Output if guess is too low (<) or too high (>) or the number (==)

Output "You won!"

CREATE A PLAY METHOD
SHOW REMAINING GUESSES
OUTPUT PHRASE AND HAVE USER INPUT
SAY IF GUESS IS <, >, OR ==
SAY IF THERE ARE NO MORE GUESSES

GuessingGame
    initialize number of low, high, call reset instance method

    play method
        call reset method
        while number_of_guesses is greater than 0 and win_condition is false
            remaining_phrase
            set guess to user_input
            check_guess
        met_condition

    remaining_phrase
        if number_of_guesses is greater than 1
            return "You have number_of_guesses guesses remaining"
        return "You have number_of_guesses guesses remaining"

    user_input
        set guess to the input of "Enter a number between low and high: "
        while guess is not valid
            set guess to the input of "Invalid Guess. Enter a number between low and high: "
        return guess

    is_valid
        return if guess is between low and high

    check_guess
        subtract one from guess_remaining
        if guess is equal to random_number set win_condition to true and return "That's the number!"
        if guess is less than random_number return "Your guess is too low."
        if guess is greater than random_number return "Your guess is too high."

    met_condition
        if win_condition is true return "You won!" otherwise return "You have no more guesses. You lost!"

    reset
        set number_of_guesses, guess, random_number, win_condition
'''
import random
import math

class GuessingGame:

    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.reset()

    def play(self):
        self.reset()
        while self.number_of_guesses > 0 and not self.win_condition:
            print(self.remaining_phrase())
            self.user_input()
            print(self.check_guess())
            print()
        print(self.met_condition())
        print()

    def remaining_phrase(self):
        if self.number_of_guesses > 1:
            return f"You have {self.number_of_guesses} guesses remaining."
        return f"You have {self.number_of_guesses} guess remaining."

    def user_input(self):
        self.guess = input(f"Enter a number between {self.low} and {self.high}: ")
        while not self.is_valid():
            self.guess = input(f"Invalid guess. Enter a number between {self.low} and {self.high}: ")

    def is_valid(self):
        if self.guess.isdigit():
            self.guess = int(self.guess)
            return self.low <= self.guess <= self.high
        return False

    def check_guess(self):
        self.number_of_guesses -= 1
        if self.guess == self.random_number:
            self.win_condition = True
            return "That's the number!"
        elif self.guess < self.random_number:
            return 'Your guess is too low.'
        else:
            return 'Your guess is too high.'

    def met_condition(self):
        return "You won!" if self.win_condition else "You have no more guesses. You lost!"

    def reset(self):
        self.number_of_guesses = int(math.log2(self.high - self.low + 1)) + 1
        self.guess = None
        self.random_number = random.randrange(self.low, self.high + 1)
        self.win_condition = False

game = GuessingGame(1, 10)
game.play()
game.play()