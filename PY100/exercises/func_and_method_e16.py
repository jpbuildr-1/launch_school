def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

"""

parameters:
- left 			lines: 1, 2
- right 		lines: 1, 2
- prompt		lines: 4, 5

function names:
- multiply 		lines: 1, 9
- get_num		lines: 4, 7, 8
- float			lines: 5
- input			lines: 5
- print			lines: 10


"""