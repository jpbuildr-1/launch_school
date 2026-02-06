"""
Given the following string, create a dictionary that 
represents the frequency with which each letter occurs. 
The frequency count should be case-sensitive:
"""
statement = "The Flintstones Rock"

"""
The output should resemble the following:
"""

# Pretty printed for clarity
answer = {
    'T': 1,
    'h': 1,
    'e': 2,
    'F': 1,
    'l': 1,
    'i': 1,
    'n': 2,
    't': 2,
    's': 2,
    'o': 2,
    'R': 1,
    'c': 1,
    'k': 1
}

# input: string
# output: dictionary of each case-sensitive letter occurence
# explicit:
    # each unique letter key contains an integer value
    # the integer value is a frequency count that is case sensitive
# implicit
    # case sensitive means uppercase and lowercase letters are counted separately
    # do not include spaces
# examples
    # frequency_count(statement) # see printed for clarity
    # frequency_count({})        # {}
# data structure: dictionary
# algorithm
    # Initalize `frequency_dictionary` to an empty dictionary
    # Iterate through the statement
        # If the char exists in `frequency_dictionary` add one to the value
        # Otherwise if the char to `frequency_dictionary` with a value of 1
    # return the value assigned to `frequency_dictionary`
# code
def frequency_count(statement):
    frequency_dict = {}
    for char in statement:
        if char in frequency_dict:
            frequency_dict[char] += 1
        elif char.isalpha():
            frequency_dict[char] = 1
    return frequency_dict

print(frequency_count(statement) == answer)

# algorithm
    # Initalize `frequency_dictionary` to an empty dictionary
    # Replace the spaces in statement with an empty string reassign to local variable
    # Iterate through statement
        # check that each letter is in `frequency_dictionary` and add 1 or add 1
    # return the value assigned to `frequency_dictionary`
# code
def frequency_count(statement):
    frequency_dict = {}
    statement = statement.replace(' ', '')
    for char in statement:
        frequency_dict[char] =  frequency_dict.get(char, 0) + 1
    return frequency_dict

print(frequency_count(statement) == answer)