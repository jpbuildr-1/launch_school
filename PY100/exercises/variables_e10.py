# Assume the obj already has the value of 42
# when the code below starts running. Which of
# the subsequent statements reassign the
# variable? Which statements mutate the value
# of the object that obj references? Which
# statements do neither? If necessary, you can
# read the documentations

obj = 42

obj = 'ABcd' 		# Reassignment 	-	'ABcd'
obj.upper() 		# Neither 		-  'ABcd'
obj = obj.lower()	# Reassignment	-	'abcd'
print(len(obj))		# Neither		-	'abcd'
obj = list(obj)		# Reassignment	-	['a', 'b', 'c', 'd']
obj.pop()			# Mutation		-	['a', 'b', 'c']
obj[2] = 'X'		# Mutation		-	['a', 'b', 'X']
obj.sort()			# Mutation		-	['X', 'a', 'b']
set(obj)			# Neither		-	['X', 'a', 'b']
obj = tuple(obj)	# Reassignment	-	('X', 'a', 'b')

print(obj)
print(type(obj))