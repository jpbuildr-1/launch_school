fruits = ("apple", "banana", "cherry", "date", "banana")

# How would you count the number of occurences of "banana" in the tuple?
# input: tuple of fruits
# outputs: number of occurences of "banana" in the tuple
# rules: 
    # explicit
    # implicit
        # tuples are ordered collections
        # 'banana' is case sensitive
# Example/Test Cases: 
    # print(banana_count(fruits))     # outputs 2
    # print(banana_count(('cherry'))) # 0
    # print(banana_count(()))         # 0
# Data structure:
    # integer
# Algorithm
    # Initialize `count` to 0
    # For each `fruit` in `fruits`
        # if `fruit` is 'banana' then add 1 to `count`
    # return count

def banana_count(fruits):
    count = fruits.count('banana')
    return count

print(banana_count(fruits)) # outputs 2