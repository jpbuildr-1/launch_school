"""
Performs calculation on two numbers given by user
"""

def prompt(message):
    """Displays message to user"""
    print(f'==> {message}')

def invalid_number(number_str):
    """Checks user input for integer"""
    try:
        int(number_str)
    except ValueError:
        return True
    return False

prompt('Welcome to Calculator!')

prompt("Whats the first number?")
number1 = input()

while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

print('What operation would you like to perform?\n'
	  '1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

match operation:
    case '1':    # '1' represents addition
        output = int(number1) + int(number2)
    case '2':    # '2' represents subtraction
        output = int(number1) - int(number2)
    case '3':    # '3' represents multiplication
        output = int(number1) * int(number2)
    case '4':    # '4' represents division
        output = int(number1) / int(number2)

prompt(f'The result is: {output}')
