# list comprehension
# readlines
# lines
"""
You need to process a log file named app.log that contains entries from different services. Your task is to write a function find_error_logs that reads this file and returns a list of all log entries originating from the "DATABASE" service.

Your function should also handle the case where the file does not exist by returning an empty list. Assume the log file has the following format, with each part separated by a pipe (|): TIMESTAMP|SERVICE|MESSAGE

Example app.log content:

2023-10-27T10:00:00|AUTH_SERVICE|User login successful
2023-10-27T10:01:15|DATABASE|Query executed successfully
2023-10-27T10:02:30|API_GATEWAY|Request routed
2023-10-27T10:03:00|DATABASE|Connection to replica failed

Requirements:

1. Define a function find_error_logs(file_path).
2. Use a with statement to ensure the file is handled correctly.
3. Use a try...except FileNotFoundError block to handle a missing file.
4. The function should return a list of strings, where each string is a full log line from the "DATABASE" service.
"""


# 'aaabbaaa' strip()

# def find_error_logs(file_path):
#     result = []

#     try:
#         with open(file_path) as file:
#             for log in file:
#                 log = log.strip()
#                 # print(log.split('|'))
#                 if 'DATABASE' == log.split('|')[1]:
#                     result.append(log.strip())
        
#         return result
#     except FileNotFoundError:
#         return []
        
        




# # *** Example usage ***

# with open('app.log', 'w') as file:
#     file.writelines([
#         '2023-10-27T10:00:00|AUTH_SERVICE|User login successful\n',
#         '2023-10-27T10:01:15|DATABASE|Query executed successfully\n',
#         '2023-10-27T10:02:30|API_GATEWAY|Request routed\n',
#         '2023-10-27T10:03:00|DATABASE|Connection to replica failed\n',
#         '2023-10-27T10:03:00|RANDOM|DATABASE\n',
#     ])

# database_logs = find_error_logs('app.log')
# print(database_logs)

# # Example with a non-existent file
# missing_logs = find_error_logs('non_existent.log')
# print(missing_logs)

# # *** Expected output ***
# # [
# #   '2023-10-27T10:01:15|DATABASE|Query executed successfully',
# #   '2023-10-27T10:03:00|DATABASE|Connection to replica failed'
# # ]
# # []

'''
Side Effects and Pure Functions
'''
# What actions performed by a function make it have side efffects
# What does it mean to be a non-local variable or program?
# What does it mean when an error isn't caught?
# What does it mean when a function as a side effect through other function?
# What should a function do? Define them precisely.
# What is a pure function? Why are they useful? Give an example.
# Define the lifetime of a function

'''
Decorators
'''
# Why are decorators useful? Name the specific situation(s)

'''
 What is closure in Python? 
 
 Demonstrate the concept with a simple program 
'''

num3 = 1

def holder(func):
    # free variables: func, num2 
    num2 = 100
    # num3 = 2
    def nested_func():
        # num = 3
        # func(num2)
        func(num3)
    return nested_func

print(holder(print).__closure__)
# closure object
# holder(print)() # nested_func()

# <cell at 0x7fd7e8c92050: builtin_function_or_method object at 0x7fd7ebeaa430>
# <cell at 0x7fd7e90cc6d0: int object at 0x7fd7ec99fb70>
# <cell at 0x7fd7e8cb4940: int object at 0x7fd7ec99ef30>

'''
Write a function create_pokemon_evolver that takes a Pokémon's name and its evolution_name. This function should return a new function, level_up, which represents the Pokémon gaining experience.

The level_up function should accept an integer xp as an argument. It needs to keep track of the total experience points. When the total XP reaches or exceeds 100 for the first time, it should print a message like "{name} is evolving into {evolution_name}!". On any subsequent calls, even if the XP is over 100, it should not print the evolution message again. It should, however, always return the current total XP.
'''

def create_pokemon_evolver(name, evolution_name):
    total_xp = 0
    did_message = False
    def level_up(xp):
        nonlocal total_xp, did_message
        total_xp += xp

        if total_xp >= 100 and not did_message:
            did_message = True
            print(f"{name} is evolving into {evolution_name}!")
        
        return total_xp
    
    return level_up


# Example Usage:
charmander_evolver = create_pokemon_evolver("Charmander", "Charmeleon")

# Gain some XP
print(f"Current XP: {charmander_evolver(30)}")  
# Expected Output: Current XP: 30
print(f"Current XP: {charmander_evolver(50)}")  
# Expected Output: Current XP: 80

# This call should trigger the evolution message
print(f"Current XP: {charmander_evolver(25)}")
# Expected Output:
# Charmander is evolving into Charmeleon!
# Current XP: 105

# Subsequent calls should not print the message again
print(f"Current XP: {charmander_evolver(10)}")  
# Expected Output: Current XP: 115

'''
Can you explain what PFA (partial function application) is? 

Can you come up with a simple code example that demonstrates PFA?
'''

'''
Partial function application (PFA) is a programming technique, commonly used in functional programming, that involves the process of fixing a number of arguments to a function, producing another function of smaller arity (fewer arguments). 

The partially applied function is a version of the original function with some arguments already set.
'''

def add(a, b):
    return a + b 

def multiply(a, b):
    return a * b

def fix_first_argument(func, first_num):
    def inner(second_num):
        return func(first_num, second_num)

    return inner 

add1 = fix_first_argument(add, 1)
multiply5 = fix_first_argument(multiply, 5)
# print(add(5, 5)) #

print(add1(100))    # 101
print(multiply5(5)) # 25


def holder(func):
    def nest_func(arg):
        func(arg)
    return nest_func

'''
LSBOT feedback

That code is not an example of Partial Function Application (PFA).

As discussed in the Closures lesson, PFA is the process of fixing one or more arguments to a function, which produces a new function with fewer arguments (a smaller arity).

Your holder function is a higher-order function that takes a function as an argument and returns a new function. However, it doesn't "fix" or pre-set any arguments. The returned nest_func simply calls the original func with whatever argument it receives. The arity of the returned function is the same as the original function it wraps.

This pattern is the basic structure of a decorator. It wraps a function to add behavior, but in this simple case, it just passes the call through.

For contrast, here is an example of PFA from the curriculum:

def make_adder(x):
    def adder(y):
        return x + y
    return adder

add5 = make_adder(5) # Returns a new function `adder` where x is fixed to 5
print(add5(10)) # Outputs: 15


Here, make_adder creates and returns a new function, adder, that has one of its required arguments, x, already fixed. The original concept requires two arguments (x and y), but the returned function only requires one (y).

How could you change your holder function so that it does demonstrate PFA for a function that takes two arguments?
'''




''' LSBOT feedback 2 (for Shin's example)
Yes, that is a perfect example of Partial Function Application (PFA) in Python.

Your fix_first_argument function takes a function and an argument, and returns a new function that is a specialized version of the original. The original functions, add and multiply, both require two arguments. The new functions you create, add1 and multiply5, only require one.

This reduction in the number of required arguments (the function's arity) is the defining characteristic of PFA. As the Closures lesson from PY130 explains, PFA is the process of fixing some arguments to a function, which produces another function with fewer arguments.

Your code is a great, generalized implementation of the make_adder example from that lesson. Python also has a built-in utility for this called functools.partial which achieves the same result.
'''