my_list = [
	[1, 3, 6, 11],
	[4, 2, 4],
	[9, 17, 16, 0],
]

outer_index = 0

while outer_index < len(my_list):
	nested_list = my_list[outer_index]
	nested_index = 0

	while nested_index < len(nested_list):
		if nested_list[nested_index] % 2 == 0:
			print(nested_list[nested_index])
		
		nested_index += 1
	
	outer_index += 1