def factorial_while_loop(number):
	result = 1
	current_integer = number

	while current_integer > 1:
		result *= current_integer
		current_integer -= 1
	
	return result

def factorial_for_loop(num):
	result = 1

	for number in range(1, num + 1):
		result *= num
	
	return result

factorial_for_loop(1)