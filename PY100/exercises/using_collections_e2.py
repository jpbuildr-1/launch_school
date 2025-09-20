# Use slicing to write Python code to print a 6-character substring of 
# 'Launch School' that begins with the first c.

# string = 'Launch School'

# print(string[4:10])

my_str = 'Launch School'
start = my_str.find('c')

print(my_str[start:start + 6])

