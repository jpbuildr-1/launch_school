# Uses list comprehension
squares = [ number * number for number in range(5)]

print(squares) # [0, 1, 4, 9, 16]

# Same as above using ordinary for loop
squares = []
for number in range(5):
	square = number * number
	squares.append(square)

print(squares) # [0, 1, 4, 9 , 16]

# Selection example
multiples_of_6 = [ number for number in range(20)
					if number % 6 == 0 ]
print(multiples_of_6) # [0, 6, 12, 18]

# Example combined selection and transformation:
even_squares = [ number * number 
				 for number in range(10)
				 if number % 2 == 0 ]
print(even_squares) # [0, 4, 16, 36, 64]

# Iterate through dictionary to create list of names in uppercase
cats_colors = {
	'Tess': 'brown',
	'Leo': 'orange',
	'Fluffy': 'gray',
	'Ben': 'black',
	'Kat': 'orange',
}

names = [ name.upper() for name in cats_colors ]
print(names)
# ['TESS', 'LEO', 'FLUFFY', 'BEN', 'KAT']

# Create list with only orange cats
cat_colors = {
	'Tess': 'brown',
	'Leo': 'orange',
	'Fluffy': 'gray',
	'Ben': 'black',
	'Kat': 'orange',
}

names = [ name.upper()
		  for name in cats_colors
		  if cats_colors[name] == 'orange' ]
print(names) # ['LEO', 'KAT']

# Add multiple criteria to update result with cat names starting with L
names = [ name.upper()
		  for name in cats_colors
		  if cats_colors[name] == 'orange'
		  if name[0] == 'L' ]
print(names) # ['LEO']
