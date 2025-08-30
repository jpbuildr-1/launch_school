foo = 'bar' 	# Initializing a global variable foo to a string 'bar'. The variable can be referenced in other functions.

# Defining a function that creates a local variable foo to a string 'qux'. This value cannot be referenced outside of the function.
def set_foo():
	foo = 'qux'
	print(foo) # prints qux

set_foo()		# Invokes the function.
print(foo)		# Prints the current value of the variable foo which is set to the string 'bar'. Therefore, prints bar.