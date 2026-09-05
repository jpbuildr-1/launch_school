'''
Write a function named later that takes two arguments: a function, func, and an argument for 
that function, argument. The return value should be a new function that calls func with argument 
as its argument. Here's an example of how it might be used:
'''

def later(func, arg):
    def run_it():
        return func(arg)
    
    return run_it

def printer(message):
    print(message)

print_warning = later(printer, "The system is shutting down!") # returns the function printer, and saves the argument
print_warning()  # The system is shutting down!