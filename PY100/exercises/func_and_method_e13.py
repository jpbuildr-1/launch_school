# Without running the following code, what do you think it will do?

def foo(first, second=3, third):
	print(first)
	print(second)
	print(third)

# The function above would invoke an error as the parameter after second is not a subsequent default value. 
# Once you have a default value for a parameter, every subsequent parameter must have a default value.

foo(42) 