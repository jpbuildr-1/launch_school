import os
import random
import pdb

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WINS_NEEDED = 2
WINNING_LINES = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
MOVES_FIRST = 'computer'

def prompt(message):
    print(f"==> {message}")

def display_board(board, score):
    os.system('clear')
    if someone_won(board):
        prompt(f"{detect_winner(board)} won!")
    elif board_full(board):
        prompt("It's a tie!")
    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")
    prompt(f'Match Score: Human {score['human_match']} Comp {score['comp_match']}')
    prompt(f'Game Score: Human {score['human_score']} Comp {score['comp_score']}')
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def empty_squares(board):
    return [key for key, value in board.items() if value == INITIAL_MARKER]

def player_chooses_square(board):
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices, ', ', 'and')}):")
        square = input().strip()
        if square in valid_choices:
            break

        prompt("Sorry, that's not a valid choice.")
    board[int(square)] = HUMAN_MARKER

def join_or(valid_choices, delimiter=', ', last_word='or'):
    match len(valid_choices):
        case 0:
            return ''
        case 1:
            return valid_choices[0]
        case 2:
            return f'{valid_choices[0]} {last_word} {valid_choices[1]}'
    leading = delimiter.join(str(item) for item in valid_choices[0:-1])
    return f'{leading}{delimiter}{last_word} {valid_choices[-1]}'

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    return None

def someone_won(board):
    return bool(detect_winner(board))    

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    square = computer_plays_offense(board) or computer_plays_defense(board) or (5 if board[5] == ' ' else None) or random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

def computer_plays_offense(board):
    square = None
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        immediate_opp = (board[sq1] == COMPUTER_MARKER and board[sq2] == COMPUTER_MARKER and board[sq3] == INITIAL_MARKER) or (board[sq1] == COMPUTER_MARKER and board[sq2] == INITIAL_MARKER and board[sq3] == COMPUTER_MARKER) or (board[sq1] == INITIAL_MARKER and board[sq2] == COMPUTER_MARKER and board[sq3] == COMPUTER_MARKER)
        if immediate_opp:
            if board[sq1] == INITIAL_MARKER:
                square = sq1
                break
            elif board[sq2] == INITIAL_MARKER:
                square = sq2
                break
            elif board[sq3] == INITIAL_MARKER:
                square = sq3
                break
    return square

def computer_plays_defense(board):
    square = None
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        immediate_threat = (board[sq1] == HUMAN_MARKER and board[sq2] == HUMAN_MARKER and board[sq3] == INITIAL_MARKER) or (board[sq1] == HUMAN_MARKER and board[sq2] == INITIAL_MARKER and board[sq3] == HUMAN_MARKER) or (board[sq1] == INITIAL_MARKER and board[sq2] == HUMAN_MARKER and board[sq3] == HUMAN_MARKER)
        if immediate_threat:
            if board[sq1] == INITIAL_MARKER:
                square = sq1
                break
            elif board[sq2] == INITIAL_MARKER:
                square = sq2
                break
            elif board[sq3] == INITIAL_MARKER:
                square = sq3
                break
    return square

def initialize_score():
    return {'human_score': 0, 'human_match': 0, 'comp_score': 0, 'comp_match': 0}

def keep_score(board, score):
    if detect_winner(board) == 'Player':
        score['human_score'] += 1
    if detect_winner(board) == 'Computer':
        score['comp_score'] += 1
    if score['human_score'] == WINS_NEEDED:
        score['human_match'] += 1
        score['human_score'] = 0
    if score['comp_score'] == WINS_NEEDED:
        score['comp_match'] += 1
        score['comp_score'] = 0

def play_again():
    prompt("Play again? (y or n)")
    answer = input().lower()
    while answer.lower() != 'y' and answer.lower() != 'n':
        prompt("Please enter a valid input.")
        prompt("Play again? (y or n)")
        answer = input().lower()
    return answer

def play_tic_tac_toe():
    if MOVES_FIRST == 'choose':
        prompt('Choose who goes first (player, computer)')
        first = input().lower()
    else:
        first = MOVES_FIRST
    score = initialize_score()
    while True:
        board = initialize_board()

        while True:
            display_board(board, score)
            if first == 'player':
                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break
                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break
            elif first == 'computer':
                computer_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break
                display_board(board, score)
                player_chooses_square(board)
                if someone_won(board) or board_full(board):
                    break

        if someone_won(board):
            keep_score(board, score)
        display_board(board, score)

        match_over = score['human_match'] == WINS_NEEDED or score['comp_match'] == WINS_NEEDED
        if match_over:
            winner = "Player" if score['human_match'] == WINS_NEEDED else "Computer"
            prompt(f'The {winner} won the match!')
            score = initialize_score()
        if play_again() != 'y':
            break
        if match_over:
            score = initialize_score()
    prompt('Thanks for playing Tic Tac Toe!')

# Call the main game function
play_tic_tac_toe()