
def multiply(number1, number2):
	return number1 * number2
	
def get_number(prompt):
	return float(input(prompt))
	
def display_calculation():
	number1 = get_number('Enter the first number: ')
	number2 = get_number('Enter the second number: ')

	print(f'{number1} * {number2} = {multiply(number1, number2)}')

display_calculation()
