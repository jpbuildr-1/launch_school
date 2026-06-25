import random

class Player:
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self, player_type):
        self._player_type = player_type.lower()
        self.move = None

    def _is_human(self):
        return self._player_type == 'human'

    def choose(self):
        if self._is_human():
            message = f'Choose {" ".join(Player.CHOICES[:2])} or {Player.CHOICES[2]}: '

            while True:
                choice = input(message).lower()
                if choice in Player.CHOICES:
                    break
                
                print(f"{choice} IS AN INVALID RESPONSE")
            
            self.move = choice
            Move(self.move)
        else:
            self.move = random.choice(Player.CHOICES)

class Move:
    def __init__(self, choice):
        # This seems like we need something to keep track of the choice
        # a move object can be "paper", "rock" or "scissors"
        self.choice = choice


class Rule:
    def __init__(self):
        # not sure what the "state" of a rule object should be
        pass

    # not sure where "compare" goes yet
    def compare(self, move1, move2):
        pass

class RPSGame:
    def __init__(self):
        self._human = Player('human')
        self._computer = Player('computer')
    
    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_winner(self):
        print(f"You chose: {self._human.move}")
        print(f"The computer chose: {self._computer.move}")

        human_choice = self._human.move
        computer_choice = self._computer.move

        if ((human_choice == "rock" and computer_choice == "scissors") or
           (human_choice == "paper" and computer_choice == "rock") or
           (human_choice == "scissors" and computer_choice == "paper")):
            print('You win!')
        elif ((human_choice == "rock" and computer_choice == "paper") or
             (human_choice == "paper" and computer_choice == "scissors") or
             (human_choice == "scissors" and computer_choice == "rock")):
            print('Computer wins!')
        elif human_choice == computer_choice:
            print("It's a tie")

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _play_again(self):
        while True:
            answer = input("Play again? (Y / N) ")
            if answer.lower().startswith('y') or answer.lower().startswith('n'):
                break
            print(f"{answer} is not a valid response. Choose Y or N.")
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