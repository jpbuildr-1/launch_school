my_set = {
	'Fluffy',
	'Butterscotch',
	'Pudding',
	'Cheddar',
	'Cocoa',
}

my_dict = { item: len(item) for item in my_set if len(item) % 2 != 0 }
print(my_dict)