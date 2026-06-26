import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = choice

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _human_wins(self):
        human_choice = self._human.move
        computer_choice = self._computer.move

        return ((human_choice == "rock" and computer_choice == "scissors") or
                (human_choice == "paper" and computer_choice == "rock") or
                (human_choice == "scissors" and computer_choice == "paper"))

    def _computer_wins(self):
        human_choice = self._human.move
        computer_choice = self._computer.move

        return ((computer_choice == "paper" and human_choice == "rock" ) or
                (computer_choice == "scissors" and human_choice == "paper") or
                (computer_choice == "rock" and human_choice == "scissors"))

    def _display_winner(self):
        print(f"You chose: {self._human.move}")
        print(f"The computer chose: {self._computer.move}")

        if self._human_wins():
            print('You win!')
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print("It's a tie")

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _play_again(self):
        while True:
            answer = input("Play again? (Y / N) ")
        return answer.lower().startswith('y')

    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break

        self._display_goodbye_message()

RPSGame().play()