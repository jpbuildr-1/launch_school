# looping over a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
	print(key)

print()
# looping over a dictionary's values
for value in my_dict.values():
	print(value)

print()
# looping over a dictionary's key/value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}
for item in my_dict.items():
	print(item)

print()
# looping over dictionary's key/value pairs (pythonic way)
my_dict = {'a': 1, 'b': 2, 'c': 3}
for (key, value) in my_dict.items():
	print(f'{key} = {value}')

print()
# looping over dictionary's key/value pairs (more pythonic way)
my_dict = {'a': 1, 'b': 2, 'c': 3}
for key, value in my_dict.items():
	print(f'{key} = {value}')