# Without running the following code, determine what each
# print statement should print.

cats = ('Cocoa', 'Cheddar', 'Pudding', 'Butterscotch')

print('Butterscotch' in cats) 	# True
print('Butter' in cats) 		# False, 'Butter' is not in cats and must match list element exactly
print('Butter' in cats[3])		# True, 'Butter' is in 'Butterscotch'
print('cheddar' in cats)		# False, cheddar != Cheddar