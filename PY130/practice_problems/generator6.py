'''
Create a generator function that generates the capitalized version of every
string in a list of strings whose length is less than 5. Use a single print
invocation to print all the capitalized strings as a set.
'''
def capitalized(strings):
    for string in strings:
        if len(string) < 5:
            yield string.capitalize()

strings = ['abc', 'defg', 'hijkl', 'mnop']
capitalized_strings = capitalized(strings)
print(set(capitalized_strings))