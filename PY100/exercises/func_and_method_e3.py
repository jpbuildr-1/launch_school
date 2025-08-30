# Asks user for number.
def input_number(question):
	number = input(question)
	return number

# Multplies two numbers.
def multiply(number1, number2):
	return number1 * number2

# Shows multiplication equation between two numbers.
def show_equation():
	number1 = float(input_number("Enter the first number: "))
	number2 = float(input_number("Enter the second number: "))

	numbers_multiplied = multiply(number1, number2)	

	print(f'{number1} * {number2} = {numbers_multiplied}')

show_equation()

