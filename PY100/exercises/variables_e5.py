# Write a program names greeter.py that greets
# 'Victor' three times. Your program should
# use a variable and not hard code the string
# value 'Victor' in each greeting. Here's an
# example run of the program

"""

python greeter.py
Good Morning, Victor.
Good Afternoon, Victor.
Good Evening, Victor.

"""

name = 'Victor'

# concatenation here is hard to read
print('Good Morning, ' + name + '.')
print('Good Afternoon, ' + name + '.')
print('Good Evening, ' + name + '.')

# F string makes the code easier to read
print(f'Good Morning, {name}.')
print(f'Good Afternoon, {name}.')
print(f'Good Evening, {name}.')