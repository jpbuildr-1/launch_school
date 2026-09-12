'''
Which of the following functions are pure functions?
'''

# Function 1 (not a pure function because of print)
def sum(a, b):
    print(a + b)
    return a + b

# Function 2 (pure function)
def sum(a, b):
    a + b

# Function 3 (it is a pure function will always return the same value)
def sum(a, b):
    return a + b

# Function 4 (not a pure function because uses random to perform action)
import random

def sum(a, b):
    return a + b + random.random()

# Function 5 (it is a pure function will always return the same value)
def sum(a, b):
    return 3.1415