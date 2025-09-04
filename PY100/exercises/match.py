value = 5

match value:
	case 1 | 2 | 3 | 4:
		print('value is < 5')
	case 5 | 6:
		print('value is 5 or 6')
	case _: # default case
		print('value is not 1, 2, 3, 4, 5, or 6')
# value is 5 or 6

value = 6

if value == 1 or value == 2 or value == 3 or value == 4:
	print('value is < 5')
elif value == 5 or value == 6:
	print('value is 5 or 6')
else:
	print('value is not 1, 2, 3, 4, 5, or 6')
# value is 5 or 6