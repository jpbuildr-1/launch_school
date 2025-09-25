names = ['Chris', 'Max', 'Karis', 'Victor']
upper_names = []

# Uses While Loop
# index = 0

# while index < len(names):
# 	upper_name = names[index].upper()
# 	upper_names.append(upper_name)
# 	index += 1

# For loop example
# for name in names:
# 	upper_name = name.upper()
# 	upper_names.append(upper_name)

# print(upper_names) # ['CHRIS', 'MAX', 'KARIS', 'VICTOR']

# Exclude Max
for name in names:
	# Via conditional search for 'Max'
	# if name == 'Max':
	# 	continue

	# upper_name = name.upper()
	# upper_names.append(upper_name)

	# Via conditional search for not 'Max'
	if name != 'Max':
		upper_name = name.upper()
		upper_names.append(upper_name)

print(upper_names) # ['CHRIS', 'KARIS', 'VICTOR']