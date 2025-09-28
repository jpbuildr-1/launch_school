squares = { f'{number}-squared': number * number
			for number in range(1, 6) }
print(squares)

# Set comprehension example
squares = { number * number for number in range(1,6) }
print(squares) # {1, 4, 9, 16, 25}