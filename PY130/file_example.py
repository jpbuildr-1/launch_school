'''
Reading from a file
'''
# example of read() method
# file = open('example.txt', 'r')
# content = file.read()
# file.close()

# print(repr(content))
# # 'Running dog\nSleeping cat\nSwimming fish\nSinging bird'

# # example of readlines() method
# file = open('example.txt', 'r')
# content = file.readlines()
# file.close()

# print(repr(content))
# # ['Running dog\n', 'Sleeping cat\n',
# # 'Swimming fish\n', 'Singing bird']

# # example of readline() method
# file = open('example.txt', 'r')
# print(repr(file.readline()))    # 'Running dog\n'
# print(repr(file.readline()))    # 'Sleeping cat\n'
# print(repr(file.readline()))    # 'Swimming fish\n'
# print(repr(file.readline()))    # 'Singing bird
# print(repr(file.readline()))    # ''
# print(repr(file.readline()))    # ''
# file.close()

# example of for loop
# file = open('example.txt', 'r')
# for line in file:
#     print(repr(line))
# 'Running dog\n'
# 'Sleeping cat\n'
# 'Swimming fish\n'
# 'Singing bird'

# file.close()

'''
Writing to a File
'''
# example of writing to a file
# file = open('output.txt', 'w')
# file.write('Hello, world!\n')

# lines = ['First line\n', 'Second line\n']
# file.writelines(lines)

# file.close()

# # example of appending a file
# file = open('output.txt', 'a')
# file.write('Third line!\n')
# file.write('Last line!\n')
# file.close()

'''
Using the `with` statement
'''
# with open('example.txt', 'r') as file:
#     for line in file:
#         print(line)

'''
Error Handling
'''
try:
    with open('example1.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print('The file does not exist')

def greet(name, color="blue"):
    if color:
        print(f"Hello {name}. Your favorite color is {color}.")
    else:
        print(f"Hello {name}. You don't have a favorite color.")

greet("Pete") # Hello Pete. You don't have a favorite color.