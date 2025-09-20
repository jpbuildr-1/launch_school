
print('abc-def'.isalpha()) 		# False, - is not a letter
print('abc_def'.isalpha()) 		# False, _ is not a letter
print('abc def'.isalpha()) 		# False, ' ' is not a letter
print('abc def'.isalpha() and
	  'abc def'.isspace()) 		# False, ' ' is not a letter
print('abc def'.isalpha() or
	  'abc def'.isspace()) 		# False, a is not a space
print('abcdef'.isalpha()) 		# True, all are letters
print('31415'.isdigit()) 		# True, all are numbers
print('-31415'.isdigit()) 		# False, - is not a number
print('31_415'.isdigit()) 		# False, _ is not a number
print('3.1415'.isdigit()) 		# False, . is not a number
print(''.isspace())				# False, an empty string sx'' is not a space

# What will the following code print?