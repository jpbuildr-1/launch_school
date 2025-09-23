# Without running the following code, determine what each line should print.

print('johnson' in 'Joe Johnson') 		# False because the check is case sensitive
print('sen' not in 'Joe Johnson') 		# True 'sen' is not in 'Joe Johnson'
print('Joe J' in 'Joe Johnson') 		# True 'Joe J' is in 'Joe Johnson'
print(5 in range(5))					# False the range is from 0 - 4
print(5 in range(6))					# True the range is from 0 - 5
print(5 not in range(5, 10))			# False the range is from 5 - 9
print(0 in range(10, 0, -1))			# False range is from 10 - 1
print(4 in {6, 5, 4, 3, 2, 1})			# True
print({1, 2, 3} in {1, 2, 3})			# False
print({3, 2} in {1, frozenset({2, 3})})	# False 