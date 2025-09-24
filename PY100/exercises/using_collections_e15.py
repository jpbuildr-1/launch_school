# Without running the following code, what values will be
# printed by line 10?

pets = {
	'Cat': 'Meow',
	'Dog': 'Bark',
	'Bird': 'Tweet',
}

keys = pets.keys() 			# dict_keys(['Cat', 'Dog', 'Bird'])
del pets['Dog']				# dict_keys(['Cat', 'Bird'])
pets['Snake'] = 'Sssss'		# dict_keys(['Cat', 'Bird', 'Snake'])
print(keys)					# dict_keys(['Cat', 'Bird', 'Snake'])