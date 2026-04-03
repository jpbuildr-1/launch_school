'''
1. Initialize the 3x3 board
    - init an empty board with 9 squares
2. Player goes first and places 'X'
    - Player chooses an empty square on the board
    - The square chosen will have a 'X'
3. Computer goes second and places 'O'
    - Computer chooses an empty square on the board
    - The square chosen will have an 'O'
4. Repeat 2 and 3 until 3 in a row ('X' or 'O') or full board
    - End the game when one of the following is met:
        - One of the rows contain all 'X' or 'O'
        - One of the columns contain all 'X' or 'O'
        - One of the diagonals contain all 'X' or 'O'
        - There are no more empty spaces on the board
5. Then game ends, ask play again?
    - Show winner, whoever got 3 in a row
    - Ask player if they want to play again?
'''
import random
import os
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

def prompt(phrase):
    print(f"===> {phrase}")

def initialize_board(board):
    os.system('clear')
    print()
    print(f'     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print(f'     |     |     ')
    print(f'-----|-----|-----')
    print(f'     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print(f'     |     |     ')
    print(f'-----|-----|-----')
    print(f'     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print(f'     |     |     ')
    print()

def empty_square(board):
    return [str(square) for square in board if board[square] == ' ']

def display_board(board):
    os.system('clear')
    if someone_won(board, HUMAN_MARKER):
        prompt('Player won!')
    elif someone_won(board, COMPUTER_MARKER):
        prompt('Computer won!')
    elif full_board(board):
        prompt("It's a tie!")
    print()
    print(f'     |     |     ')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
    print(f'     |     |     ')
    print(f'-----|-----|-----')
    print(f'     |     |     ')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
    print(f'     |     |     ')
    print(f'-----|-----|-----')
    print(f'     |     |     ')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
    print(f'     |     |     ')
    print()

def player_move(board):
    prompt(f"Choose a square: {','.join(empty_square(board))}")
    move = int(input())
    while board[move] != ' ':
        prompt(f"Please choose a different square: {','.join(empty_square(board))}")
        move = int(input())
    board[move] = HUMAN_MARKER

def computer_move(board):
    move = int(random.choice(empty_square(board)))
    board[move] = COMPUTER_MARKER

def someone_won(board, mark):
    if rows_match(board, mark) or columns_match(board, mark) or diagonals_match(board, mark):
        return True
    return False


def rows_match(board, mark):
    if (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark):
        return True

def columns_match(board, mark):
    if (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark):
        return True

def diagonals_match(board, mark):
     if (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark):
        return True   

def full_board(board):
    if all([board[square].strip() for square in board]):
        return True
    return False

def tic_taco():
    board = {square: ' ' for square in range(1, 10)}
    initialize_board(board)
    while True:
        player_move(board)
        if someone_won(board, HUMAN_MARKER) or full_board(board):
            display_board(board)
            break
        computer_move(board)
        if someone_won(board, COMPUTER_MARKER) or full_board(board):
            display_board(board)
            break
        display_board(board)
tic_taco()