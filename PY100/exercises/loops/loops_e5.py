my_list = [
	[1, 3, 6, 11],
	[4, 2, 4],
	[9, 17, 16, 0],
]

# Print even numbers within the nested lists
for nested in my_list:
	for number in nested:
		# Even numbers are divisible by 2
		if number % 2 == 0:
			print(number)