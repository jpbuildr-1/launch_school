# """
# intellisense on


# PEDAC:
# rules
# algo

# order that you do things matter
# test every chance you get
# or i expect this to run something

# usually ask about maybe test case
# shorten vocab
# indentation in PEDAC
# good variable names reduce working memory

# iterating and manipulating should be easy
# nested iteration - first and second
# speak as if you are talking to someone

# 2 problems - different in style (logic vs procedural) medium in 20 minutes
# """

# # inputs:
# # outputs: 2 x list -> each list has elements of integers
# # are you effectively trying to recreate zip function for lists

# def zip_lists(lst1, lst2):

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print(zip_lists(list1, list2)) # => [1, 4, 2, 5, 3, 6]

# def parts(string):
#     # implementation

# word = 'Sesquipedalianism'
# print(parts(word)) # ['S', 'Se', 'Ses', 'Sesq', 'Sesqu', 'Sesqui', 'Sesquip', 'Sesquipe', ...]
# # ['S', 'Se', 'Ses', 'Sesq', 'Sesqu', 'Sesqui', 'Sesquip', 'Sesquipe', 'e', 'es', 'esq', ...]

# # Algo
"""
Problem
"""
# # SQUARE DIGITS
# # You are asked to square every digit of a number.
# # For example, if we run 9119 through the function, 811181 will come out, because 9^2 is 81 and 1^2 is 1.
# # Input: integer
# # Output: integer
# # Rules:
#    # 1s, 10s, 100s
#    # length gives you the times you need modulo
# # Data Structure
#    # integer > list > string > integer

# print(square_digits(0) ==    0)
# print(square_digits(64) ==   3616)
# print(square_digits(1111) == 1111)
# print(square_digits(2222) == 4444)
# print(square_digits(3333) == 9999)
# print(square_digits(3212) == 9414)
# print(square_digits(1234) == 14916)
# print(square_digits(77455754) == 4949162525492516)
# print(square_digits(99999999) == 8181818181818181)

"""
Problem
"""

# PERCENTAGE OF EVENTS
# Given a positive integer, return the percentage of even numbers between
# 1 and that integer, rounded to two decimal places.

# print(even_percent(1) == '0')
# print(even_percent(2) == '0.5')
# print(even_percent(3) == '0.33')
# print(even_percent(12) == '0.5')
# print(even_percent(13) == '0.46')

# BONUS: Solve in one line

"""
Problem
"""

# /*
# BOUNCY COUNT
# Some numbers have only ascending digits, like 123, 3445, 2489, etc.
# Some numbers have only descending digits, like 321, 5443, 9842, etc.
# A number is "bouncy" if it has both ascending and descending digits, like 313, 92543, etc.
# Write a method that takes a list of numbers and counts how many of them are bouncy.
# 


# Python test cases:
print(bouncy_count([]) == 0)
print(bouncy_count([11, 0, 345, 21]) == 0)
print(bouncy_count([121, 4114])  == 2)
print(bouncy_count([176, 442, 80701644]) == 2)
print(bouncy_count([176, 121000000000, 80701644]) == 3)

"""
Problem
"""

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_matrix = # invoke func on matrix

# input: nested list
# output: list
# explicit: 
# implicit: 
# data structure: list
# algo:
# Init `lst`
# iterate through matrix and its elements and access through indexing
# iterate through list to append element to a new list

# create empty result
# Iterate through the matrix.
    # For each sublist:
        # append it into result
# code:
def flat_list(matrix):
    flattened_list = []
    for sublist in matrix:
        for idx, element in enumerate(lst_element):
            print()
            lst.append([idx])


print(flattened_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
Problem
"""
#
my_words = ['foo', 'bar', 'baz']
print(wordsofLengthN(my_words, 3))
print(wordsofLengthN(my_words, 2))

"""
Problem
"""

target_letters = ['a', 'b', 'c', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

dictionary = {
    'a': { 'present': False, 'count': 0},
    'b': { 'present': False, 'count': 0},
    'c': { 'present': False, 'count': 0},
    'd': { 'present': False, 'count': 0},
    'e': { 'present': False, 'count': 0},
}

"""
Problem
"""

lst = [14, 15, 16, 17, 18, 19, 20, 21, 123, 11111]

print(lst)  # [5, 6, 7, 8, 9, 10, 2, 3, 6, 5]

add_digits

"""
Problem
"""
def zip_lists(lst1, lst2):

list1 = [1, 2, 3, 2]
list2 = [4, 5, 6]
print(zip_lists(list1, list2))  # => [1, 4, 2, 5, 3, 6, 2]



"""
Problem
"""

# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.

def longest(string):


print(longest('asd') == 'as')
print(longest('nab') == 'ab')
print(longest('abcdeapbcdef') ==  'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag') == 'fgikl')
print(longest('z') == 'z')
print(longest('zyba') == 'z')


"""
Problem
"""

'''
Alphabet Symmetry
Consider the word "abode".
The letter `a` is in position 1 and `b` is in position 2.
In the alphabet, `a` and `b` are also in positions 1 and 2.

The letters `d` and `e` in "abode" occupy the positions they would occupy in the alphabet, which are positions 4 and 5. 

Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

solve(["abode","ABc","xyzD"]) // [4, 3, 1]

Input will consist of alphabetic characters, both uppercase and lowercase. No spaces.
'''

# // // Python test cases
# // print(solve(["abode","ABc","xyzD"]) == [4,3,1]) # True
# // print(solve(["abide","ABc","xyz"]) == [4,3,0]) # True
# // print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]) == [6,5,7]) # True
# // print(solve(["encode","abc","xyzD","ABmD"]) == [1, 3, 1, 3]) # True

# 
# Input: list of words
# Output: list of integers

"""
Problem
"""
'''
PERCENTAGE OF EVENS (medium)
Given an array of integers, consider the "running sum" of each element: the sum of all the elements up to and including that element. For instance:
[1, 5, 3]
the running sum of 1 is 1
the running sum of 5 is (1 + 5) = 6
the running sum of 3 is (1 + 5 + 3) = 9

Return the percentage of running sums in the array that are even, rounded to two decimal places.

Python test cases:
print(evenPercent([1, 2, 4]) # 0.0
print(evenPercent([1, 3]) # 0.5
print(evenPercent([1, 5, 3]) # 0.333...
print(evenPercent([2, 4, 6]) # 1.0
print(evenPercent([12]) # 1.0
print(evenPercent([13]) # 0.0
print(evenPercent([]) # 1.0

'''

"""
Problem
"""
'''
Sum of Numbers
Implement a function that calculates the sum of numbers inside of a string.
Example: "L12aun3ch Sch3oo45l" should output 63.
1 + 2 + 3 = 6      3 + 4 + 5 = 12

"L 12 aun 3 ch Sch 3 oo 45 l" 

You can expect that the string will include only positive numbers.
'''

# Test Cases
print(sum_of_numbers("HI") == 0)
print(sum_of_numbers("HE2LL3O W1OR5LD") == 11)
print(sum_of_numbers("L12aun3ch Sch3ool45") == 63)
print(sum_of_numbers("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog") == 3635)

# input: string with only positive numbers
# output: integer which is the sum of the numbers in the input
# explicit: only pos numbers, calculating sum of numbers
# implicit: 

# data structure: integer

# algo:
# intialize sum to zero
# iterate through the string
    # check if character is a number
        # add to sum
# return sum

# practice no more
# space into brain
# keep talking about the struggle
# Scratch pad


"""
Problem
"""

'''
Unique String Characters
Given two strings, return the characters that are not common in the two strings.
'''

# input: two strings as two separate arguments
# output: one string of unique characters
# explicit: return the characters that are not common in the two strings
# implicit: the 1st string unique letters should be concatenated to the new string

# algo
# Initialize unique_string = ""
# For each char in 1st string
    #  if char is not in 2nd string
        # concatenate to unique_string
# return unique_string

def unique_string_characters(str1, str2):
    unique_string = ''
    for char in str1:
        if char not in str2:
            unique_string += char
    for char in str2:
        if char not in str1:
            unique_string += char
    return unique_string


# Python test cases
print(unique_string_characters("xyab","xzca") == "ybzc")
print(unique_string_characters("a","z") == "az")
print(unique_string_characters("abcd","de") == "abce")
print(unique_string_characters("abc","abba") == "c")
print(unique_string_characters("xyz","zxy") == "")


"""
Problem
"""

'''
Given an integer n, find the maximal number you can obtain by deleting exactly one digit of the given number.

'''
# input: integer
# output: maximal integer
# explicit: find the maximal number by deleting exactly one digit of the given number
# implicit: maximal number is a largest number after deleting one digit, assumption is we must delete one digit and cannot keep it as is

# data structure: integer
# algo:
# compare each digit

# TEST CASES
print(delete_digit(791983) == 91983)
print(delete_digit(152) == 52)
print(delete_digit(1001) == 101)
print(delete_digit(10) == 1)

# left most digits and compare both

"""
Problem
"""
# Find the longest substring in alphabetical order.
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
# The input will only consist of lowercase characters and will be at least one letter long.
# If there are multiple solutions, return the one that appears first.

'''
P:
I: string
O: longest alphabetical substring
IMP:
    alphabetical is from a to z
    a is less than z in string format
    abc or abt as long as it is descending order
    aaab or abbd so the order can contain duplicates
EXP: 
    find the longest substring in alphabetical order
    lowercase characters only and will be at least one letter long
    return the first solution that appears

Ideas:
keep adding to current sub string until previous character is greater than current character
then compare to longest substring and substitute

D: string

A:
if the length of string is 1 return the string
Initialize `longest_substring` to an empty string
Intialize `current_substring` to 1st character of string
For remaining characters in the string:
    if last element of `current_substring` is less than or equal to char
        add char to `current_substring`
    if it is the last element
    if length of `current_substring` is greater than length of `longest_substring`
        set `longest_substring` to `current_substring`
        set `current_substring` to char
if length of `current_substring` is greater than length of `longest_substring`
    set `longest_substring` to `current_substring`
    set `current_substring` to char
return `longest_substring`

C:

'''

def longest(string):
    if len(string) == 1:
        return string
    longest_substring = ""
    current_substring = string[0]
    for idx in range(1, len(string)):
        char = string[idx]
        previous_char = current_substring[-1]
        if previous_char <= char:
            current_substring += char
        elif len(current_substring) > len(longest_substring):
            longest_substring = current_substring
            current_substring = char
        elif previous_char > char:
            current_substring = char
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring
    return longest_substring

# TEST CASES
print(longest('asd') == 'as')
print(longest('nab') == 'ab')
print(longest('abcdeapbcdef') ==  'abcde')
print(longest('asdfaaaabbbbcttavvfffffdf') == 'aaaabbbbctt')
print(longest('asdfbyfgiklag') == 'fgikl')
print(longest('z') == 'z')
print(longest('zyba') == 'z')



'''
PROBLEM

'''

"""We want to alter an array of letters according to a code. In this code, given the command `"9a"`, we should change the character at index 9 of the array to `"a"`.
Write a method that takes an array and a list of these commands, and mutates the string accordingly."""

PYTHON
test_1 = ["d", "o", "g"]
encode(test_1, ["0f"]) # index 0 of the array to f
print(test_1 == ["f", "o", "g"])

test_2 = ["p", "a", "r", "r", "o", "t"]
encode(test_2, ["0m", "3m", "8m"]) # index 0 to m, index 3 m, index 8 to m (does not exist, pass)
print(test_2 == ["m", "a", "r", "m", "o", "t"])

test_3 = ["w", "e", "i", "m", "a", "r", "a", "n", "e", "r"]
encode(test_3, ["0p", "2t", "3p", "6t"])
print(test_3 == ["p", "e", "t", "p", "a", "r", "t", "n", "e", "r"])

test_4 = ["i", "n", "c", "o", "r", "r", "e", "c", "t", " ", "l", "o", "n", "g", " ", "s", "t", "r", "u", "n", "g"]
encode(test_4, ["0a", "1 ", "18i"])
print(test_4 == ["a", " ", "c", "o", "r", "r", "e", "c", "t", " ", "l", "o", "n", "g", " ", "s", "t", "r", "i", "n", "g"])

'''
given: list and list of commands
return: mutated list
notes:
Alter an array of letters according to a code (index and letter)
data structure: list
algo:
    for code in list of commands:
        if the length of the list is less than the index from code
            modify list based on code at index change existing letter to modifying letter
    return list
edge cases:
'''
######
'''
PROBLEM
'''

'''
BOUNCY COUNT
Some numbers have only ascending digits, like 123, 3445, 2489, etc.
Some numbers have only descending digits, like 321, 5443, 9842, etc.
A number is "bouncy" if it has both ascending and descending digits, like 313, 92543, etc.
Write a method that takes a list of numbers and counts how many of them are bouncy.

'''
'''
given: list of digits
return: count of how many of the digits are bouncy
notes:
A number is 'bouncy' if it has both ascending and descending digits
ascending means 123
descending means 321

data structure: integer to measure count
algo:
    Init `count` to 0
    For each number in the list of digits
        Add 1 to count if bouncy
    return `count`

    Add 1 to count if bouncy
        for each digit in number
            is the digit greater than next digit
edge case:
'''

Python test cases:
print(bouncyCount([]) == 0)
print(bouncyCount([11, 0, 345, 21]) == 0)
print(bouncyCount([121, 4114]) == 2)
print(bouncyCount([176, 442, 80701644]) == 2)

######
'''
PROBLEM
'''

'''
Where My Anagrams At?
Two words are anagrams of each other if they both contain the same letters.

Write a method that will find all the anagrams of a word from a list.
You will be given two inputs a word and an array with words.
You should return an array of all the anagrams or an empty array if
there are none.
*/

// # Python test cases
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']));
// # ['aabb', 'bbaa']

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']));
// # ['carer', 'racer']

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'Racer']));
// # ['carer', 'Racer']

print(anagrams('laser', ['lazing', 'lazy',  'lacer']));
// # []
'''

'''
given: key_word, list of words
return: list of anagrams
notes:
Two words are anagrams of each other if they both contain the same letters


data structure: list, 
algo:
    init 'anagrams' = []
    for each word in list of words
        if the sorted key_word is in sorted word
            add to anagrams
    return anagrams

edge cases:
'''
#####
'''
PROBLEM
'''
"""
Write a method that takes an array of consecutive letters as input and returns the missing letter.
"""
'''
given: list of consecutive letters
return: missing letter as upper or lower based on what given list is lower or upper respectively
notes:
'abcdefghijklmnopqrstuvwxyz'
1st and last letter and find index from alphabet using the 1st and last letter

data structure: string
algo:
    for letter in list
'''



print(determine_missing_letter(['a','b','c','d','f']) == 'E')
print(determine_missing_letter(['o','q','r','s']) == 'P')
print(determine_missing_letter(['H','J','K','L']) == 'i')
print(determine_missing_letter([]) == [])


'''

'''

# /*
# Difference of Two
# The objective is to return all pairs of numbers from a given array of numbers that have a difference of 2.
# The result array should be sorted in ascending order of values.
# Assume there are no duplicate numbers in the array.
# The order of the numbers in the input array should not matter.
# */



# // # Python Test cases
# // print(differenceOfTwo([1, 2, 3, 4]) == [[1, 3], [2, 4]])
# // print(differenceOfTwo([4, 1, 2, 3]) == [[1, 3], [2, 4]])
# // print(differenceOfTwo([1, 23, 3, 4, 7]) == [[1, 3]])
# // print(differenceOfTwo([4, 3, 1, 5, 6]) == [[1, 3], [3, 5], [4, 6]])
# // print(differenceOfTwo([2, 4]) == [[2, 4]])
# // print(differenceOfTwo([1, 4, 7, 10, 13]) == [])

'''
given: array
return: all pairs of numbers from a given array of numbers that have a difference of 2
notes:
return array should be sorted in ascending order of values
no duplicate numbers in the array
Number order in the given array should not matter ()

sort the input array first then loop through input array
for each number check if they have a difference of 2 when compared with the other numbers

ds: array
algo:
    Initialize an empty array
    for current number in sorted array
        for additional number in other indices
            if the difference between the current number and additional number is 2
                add the current number and additional number to empty array

'''

"""
Next problem
"""
# Alphabet Symmetry
# Consider the word "abode".
                    #12345
# The letter `a` is in position 1 and `b` is in position 2.
# In the alphabet, `a` and `b` are also in positions 1 and 2.

# ..x..
# abode
# abcdefghi

#  0, 1, 2, 3, 4
# [a, b, c, d, e]

# The letters `d` and `e` in "abode" occupy the positions they would occupy in the alphabet, which are positions 4 and 5. 

# Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

# solve(["abode","ABc","xyzD"]) // [4, 3, 1]

# Input will consist of alphabetic characters, both uppercase and lowercase. No spaces.
'''
given: array of words
return: array of the number of letters that occupy their positions in the alphabet
notes:
Alphabetic characters, no spaces, uppercase and lowercase

ds: array

algo:

'''

# // Python test cases
# print(solve(["abode","ABc","xyzD"]) == [4,3,1]) # True
# print(solve(["abide","ABc","xyz"]) == [4,3,0]) # True
# print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]) == [6,5,7]) # True
# print(solve(["encode","abc","xyzD","ABmD"]) == [1, 3, 1, 3]) # True

# // Ruby test cases
# puts solve(["abode","ABc","xyzD"]) == [4,3,1] # true
# puts solve(["abide","ABc","xyz"]) == [4,3,0] # true
# puts solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]) == [6,5,7] # true
# puts solve(["encode","abc","xyzD","ABmD"]) == [1, 3, 1, 3] # true


'''
NEXT PROBLEM
'''

# We want to alter an array of letters according to a code. In this code, given the command `"9a"`, 
# we should change the character at index 9 of the array to `"a"`.
# Write a method that takes an array and a list of these commands, and mutates the string accordingly.

# TEST CASES

# PYTHON
# test_1 = ["d", "o", "g"]
# encode(test_1, ["0f"])
# print(test_1 == ["f", "o", "g"])

# test_2 = ["p", "a", "r", "r", "o", "t"]
# encode(test_2, ["0m", "3m", "8m"])
# print(test_2 == ["m", "a", "r", "m", "o", "t"])

# test_3 = ["w", "e", "i", "m", "a", "r", "a", "n", "e", "r"]
# encode(test_3, ["0p", "2t", "3p", "6t"])
# print(test_3 == ["p", "e", "t", "p", "a", "r", "t", "n", "e", "r"])

# test_4 = ["i", "n", "c", "o", "r", "r", "e", "c", "t", " ", "l", "o", "n", "g", " ", "s", "t", "r", "u", "n", "g"]
# encode(test_4, ["0a", "1 ", "18i"])
# print(test_4 == ["a", " ", "c", "o", "r", "r", "e", "c", "t", " ", "l", "o", "n", "g", " ", "s", "t", "r", "i", "n", "g"])

'''
given: array of letters, command in an array
return: mutated array of letters
notes:
Mutate an array of letters according to a command
A command would change the character at index NUM of the array to 'char'

CHECK EACH COMMAND AGAINST ARRAY OF LETTERS

UPDATE ARRAY OF LETTERS AT EACH COMMAND

IF THE INDEX IN COMMAND IS NOT IN ARRAY OF LETTERS SKIP TO NEXT COMMAND

IF THE INDEX

ds:
algo:
'''

'''
PROBLEM
'''
# Given a grid of values represented by an array of arrays, e.g.:
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]

# Return the largest sum of a column of values in the grid.
# In this example, the largest sum is 18.

# TEST CASES
# a = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# [12, 15, 18]
# b = [[1, 2, 3, 4],
#     [5, 6, 7, 8]]
# [6, 8, 10, 12]

# c = [[1, 0, 0],
#      [5, 8, 10],
#      [3, 5, 1]]
# [9, 13, 11]

# PYTHON
# print(largest_column(a) == 18)
# print(largest_column(b) == 12)
# print(largest_column(c) == 13)

'''
given: grid of values (array of arrays)
return: largest sum of a column of values in the grid (integer)
notes:
Sum the 1st of each array, then 2nd of each array,...
Save the largest sum of each added array
Create a new sub array where the indices match
[1, 4, 7], [2, 5, 8], [3, 6, 9]

ds: integer
algo:

'''

'''
PROBLEM
'''

# Re-order the characters of a string, so that they are concatenated into a new string in "case-insensitively-alphabetical-order-of-appearance" order.
# Whitespace and punctuation shall simply be removed!
# The input is restricted to contain no numerals and only words containing the english alphabet letters.


'''
given: string of characters
return: string "case-insensitively-alphabetical-order-of-appearance" order
notes:
- whitespace and punctuation are to be removed
- given does not have numbers
- given contains english alphabet letters

CREATE A NEW STRING
    Initialize `new_string` to an empty string

ADD EACH ALPHA CHAR TO NEW STRING
    For each character in string
        If the character is alpha
            Concatenate to `new_string`

SORT BY CASE INSENSITIVE ALPHABETICAL ORDER
    Sort by using the lowercase value of character in `new_string`

'''
def alphabetized(string):
    new_string = ''

    for char in string:
        if char.isalpha():
            new_string += char
    return ''.join(sorted(new_string, key=str.lower))
# Tests
print(alphabetized("The Holy Bible") == "BbeehHilloTy")
print(alphabetized("!@$%^&*()_+=-`,") == "")
print(alphabetized("CodeWars can't Load Today") == "aaaaCcdddeLnooorstTWy")


# Problem
'''

'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_matrix = [number for sublist in matrix
                           for number in sublist]
"""
First element of each list
Second element of each list
Third element of each list
"""

for column_idx in range():
    for subidx, number in enumerate(sublist):
        flattened_matrix.append(sublist[subidx])


print(flattened_matrix)  # [1, 4, 7, 2, 5, 8, 3, 6, 9]

# pattern is use a flag

'''
'''
# Imagine you're analyzing data from a game's scoring system. The scores are stored in nested lists, 
# representing different rounds of the game. Your objective is to determine if, in any of the rounds, 
# all the scores are greater than a threshold (in this case, 4). If in any round all scores exceed this threshold, 
# you will need to highlight these rounds for further analysis.

# Given the list `rounds`, write the function `high_scores_in_round` to determine which rounds, 
# if any, have all scores greater than 4. You should use a list comprehension.


rounds = [[6, 8], [2, 9], [15, 11], [4, 100]]

def high_scores_in_round(rounds):
    return [round_scores for round_scores in rounds if all([score > 4 for score in round_scores])]

high_scores_in_round(rounds) # [[6, 8], [15, 11]]

# # Check if all scores in a "round" are greater than four
# # given a list, return true if all numbers in that list are greater than 4

# round_scores = [5, 2, 7, 9]
# all([True, False, True, True])
# result = [score > 4 for score in round_scores]
# print(result)

# # Filtering a list of rounds based on that criteria


'''
'''
=begin
Basic nested iteration problems
=end

sample = [1, 2, 3, 4, 5]

# Generate all sequential pairs of the array

p sequentialPairs(sample) == [[1, 2], [2, 3], [3, 4], [4, 5]]

# Group the array into sequential pairs. "Consume" elements - if they're part of one pair, they can't be part of any other

p groupedPairs(sample) == [[1, 2], [3, 4], [5]]

# Group the array into concentric pairs - the first and last elements, then the second and second-last, etc. Consume elements as before.

p groupedPairs(sample) == [[1, 5], [2, 4], [3]]

# Generate all possible pairs of the array

p allPairs(sample) == [[1, 2], [1, 3], [1, 4], [1, 5],
                       [2, 1], [2, 3], [2, 4], [2, 5],
                       [3, 1], [3, 2], [3, 4], [3, 5],
                       [4, 1], [4, 2], [4, 3], [4, 5],
                       [5, 1], [5, 2], [5, 3], [5, 4]]

# Generate all possible pairs of the array, but only in ascending order (that is, the element earlier in the argued array should come first in its subarray)

p allAscendingPairs(sample) == [[1, 2], [1, 3], [1, 4], [1, 5],
                                [2, 3], [2, 4], [2, 5],
                                [3, 4], [3, 5],
                                [4, 5]]

# Generate the cross product of an array with itself. This is similar to pairs, but we include the pair of the element with itself.

p crossProduct(sample) == [[1, 1], [1, 2], [1, 3], [1, 4], [1, 5],
                           [2, 1], [2, 2], [2, 3], [2, 4], [2, 5],
                           [3, 1], [3, 2], [3, 3], [3, 4], [3, 5],
                           [4, 1], [4, 2], [4, 3], [4, 4], [4, 5],
                           [5, 1], [5, 2], [5, 3], [5, 4], [5, 5]]

# Generate all consecutive subarrays beginning from the first array element
p firstSubarrays(sample) == [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5]]

# Generate all consecutive subarrays ending with the last array element
p lastSubarrays(sample) == [[1, 2, 3, 4, 5], [2, 3, 4, 5], [3, 4, 5], [4, 5], [5]]

# Generate all consecutive subarrays of the array
p consecutiveSubarrays(sample) == [[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5],
                                   [2], [2, 3], [2, 3, 4], [2, 3, 4, 5],
                                   [3], [3, 4], [3, 4, 5],
                                   [4], [4, 5],
                                   [5]]

# Rotate the argued array so that the rows are now columns and vice versa. The object returned by argued_array[x][y] should be the same object returned by rotated_array[y][x]
nested_sample = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
p rotation(nested_sample) = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]


# PERCENTAGE OF EVENS
# Given a positive integer, return the percentage of even numbers between 1 and that integer, rounded to two decimal places.

'''
Given: positive integer
Return: percentage of even numbers between 1 and that integer, rounded to two decimal places
Notes:
create a list of integers from 1 to n
check the number of even numbers in the list of integers
divide the number of even numbers by the length of the list
DS:
Algo:
    Init an empty numbers list
    Init even_numbers to 0
    for number in a range of numbers starting from 1 to positive integer inclusive
        add number to numbers
    for number in numbers
        if the number is an even number
            add 1 to even_numbers
    return  length of numbers divided by even_numbers rounded to two decimals
'''
def even_percent(number):
    if number == 1:
        return '0'
    numbers = []
    even_numbers = 0
    for number in range(1, number + 1):
        numbers.append(number)
    for number in numbers:
        if number % 2 == 0:
            even_numbers += 1
    return str(round(even_numbers / len(numbers), 2))



# Python test cases:
print(even_percent(1)) # == '0') # 1 -> 0 / 1 
print(even_percent(2) == '0.5') # 1, 2 -> 1/2
print(even_percent(3) == '0.33') # 1, 2, 3 -> 1/3
print(even_percent(12) == '0.5') # 1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12 -> 6/12
print(even_percent(13) == '0.46') # 1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11, 12, 13 -> 6/13


# problem types
# 2 problems what type of problems are they?
# logical, crux how do i solve this, hoops
# procedural, ok i know how, just need to implement
# usually 1 problem takes longer than the other because we are naturaly good at 1 type of problem

'''
Given a list of integers return the number of pairs of integers in the list

Notes:
If the list is empty or contains one value return 0
If number occurs more than twice, count each complete pair once

DS: list, sublist of pairs, dictionary (index: integer)

Algo:
CREATE A DICTIONARY OF INDEX: INTEGER PAIRS
FILTER DICTIONARY TO INCLUDE MATCHING VALUES
FILTER DICTIONARY TO INCLUDE ONLY INDEX PAIRS WHERE THE INDEX IS NOT PAIRED AGAIN
RETURN THE COUNT OF THE FILTERED DICTIONARY

    Set a dict_pairs to an empty dictionary
    Set matching_values to an empty dictionary
    Set pair count to 0
    Set unique_indices to an empty list
    For each integer in list of integers
        For each integer starting from the 2nd integer until the last integer in list of integers
            Add the integers as a dictionary pair to dict_pairs
    For each pair in dict_pair
        If the values are equal to each other
            Add the pair to matching_values
    For each pair in matching_values
        If indices are not in unique_indices 
            Add 1 to pair count
            Append the indices to unique_indices
    Return pair count

'''
def pairs(integers):
    if len(integers) < 2:
        return 0
    dict_pairs = []
    matching_values = []
    unique_indices = []
    pair_count = 0
    for i in range(0, len(integers) - 1):
        for j in range(i + 1, len(integers)):
            dict_pairs.append({i: integers[i], j: integers[j]})
    for pair in dict_pairs:
        numbers = list(pair.values())
        if numbers[0] == numbers[1]:
            matching_values.append(pair)
    for pair in matching_values:
        indices = list(pair.keys())
        if indices[0] not in unique_indices and indices[1] not in unique_indices:
            pair_count += 1
            unique_indices.extend(indices)
    return pair_count
print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

'''
Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase 
alphabetic characters. The function should return the length of the longest vowel substring. The vowels of 
interest are "a", "e", "i", "o", and "u".
'''

'''
Given a string of lowercase characters return the length of the longest vowel substring
vowels are 'aeiou'
Notes:
The string will be non-empty
DS: list, string, sublist
Algo:
CREATE A LIST OF SUBSTRINGS
FILTER SUBSTRINGS TO INCLUDE VOWELS ONLY
CREATE A NEW LIST OF LENGTHS OF SUBSTRING
RETURN THE LONGEST LENGTH OF SUBSTRINGS
    Set substrings to an empty list
    Set substrings_vowels to an empty list
    Set vowels_lengths to an empty list
    For each character in string ending at the 2nd to last character
        For each subcharacter in string starting from the 2nd character to the last character
            Add the character plus the subcharacter and additional slicing as needed to substring
    For each substring in substrings
        Append substring to substrings_vowels if all of the characters of substring are vowels
    For each substring in substring_vowels:
        Append the length to vowels_lengths
    Return the max of vowels_lengths
'''
VOWELS = 'aeiou'
def longest_vowel_substring(string):
    substrings = [string[i:j + 1] for i in range(len(string))
                                  for j in range(i, len(string))]
    vowels_lengths = [len(substring) for substring in substrings
                                     if all_vowels(substring)]
    if not vowels_lengths:
        return 0
    return max(vowels_lengths)

def all_vowels(substring):
    for char in substring:
        if char not in VOWELS:
            return False
    return True


print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

'''
Create a function that takes two string arguments and returns the number of times that the second string 
occurs in the first string. Note that overlapping strings don't count: 'babab' contains 1 instance 
of 'bab', not 2.

You may assume that the second argument is never an empty string.
'''

'''
Given two strings return the number of occurences of the second string in the first string.
Overlapping does not count. Once you count the characters in the string once, you cannot count it again.
Second string will never be an empty string.


DS: integer, string, 

Algo:
COUNT EACH TIME THE 2ND STRING IS EQUAL TO THE SLICED PORTION OF THE 1ST STRING
SLICED PORTION MATCHES THE LENGTH OF THE 2ND STRING
IF THE SLICED PORTION IS EQUAL TO THE 2ND STRING THEN ADD 1 TO COUNT 
    AND CHECK AGAIN STARTING FROM THE LAST INDEX + 1 OF THE MATCHED PORTION
IF THE SLICED PORTION IS NOT EQUAL TO THE 2ND STRING THEN CHECK AGAIN
    STARTING FROM THE BEGINNING INDEX + 1 OF THE SLICED PORTION

    Set count to 0
    Set index to 0
    Set length_of_2ndstr to the length of 2nd string
    While index is less than the length of the 1st string
        Set sliced_portion to sliced 1st string starting from index to index + length_of_2ndstr
        if the sliced portion is equal to the 2nd string
            Add 1 to count
            Add length_of_2ndstr to index
        else
            Add 1 to index
    Return count

'''
def count_substrings(str1, str2):
    count = 0
    index = 0
    length_of_2ndstr = len(str2)
    while index < len(str1):
        sliced_portion = str1[index:index + length_of_2ndstr]
        if sliced_portion == str2:
            count += 1
            index += length_of_2ndstr
        else:
            index += 1
    return count

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)


'''
Create a function that takes a string of digits as an argument and returns the number of even-numbered 
substrings that can be formed. For example, in the case of '1432', the even-numbered substrings are '14', 
'1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.
'''
'''
Given digits as a string return the count of even substrings
Duplicates count as an occurrence

DS: list, string, integer

Algo:
CREATE A SUBSTRING OF INTEGERS
FILTER OUT THE ODD INTEGERS FROM SUBSTRING OF INTEGERS
RETURN THE COUNT OF THE REMAINING SUBSTRING OF EVEN INTEGERS

    Set integers_substring to an empty list
    Set even_integers to an empty list
    For each digit in string of digits starting from the 1st element to length of string of digits
        For each digit in string of digits starting from current element + 1 to length of string of digits
            Append the sliced string from the current element to current element + 1 converted to an integer
    For each integer in integers_substring
        Append the even integers to even_integers
    Return the count of even_integers
        
'''
def even_substrings(digits):
    integers_substring = [int(digits[i:j]) for i in range(len(digits))
                                           for j in range(i + 1, len(digits) + 1)]
    even_integers = [integer for integer in integers_substring
                                      if integer % 2 == 0]
    return len(even_integers)

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)


'''
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a 
string and an integer. If we call the string argument s, the string component of the returned tuple t, 
and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k.
The values of t and k should be the shortest possible substring and the largest possible repeat count that 
satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.
'''

'''
Given a nonempty lowercase only string return a tuple that has a unique expression of string and the number of times
the unique expression is in the string

DS: list, string, join, dictionary (substring: number of occurences)

Algo:
CREATE A DICTIONARY OF SUBSTRINGS: NUMBER OF OCCURENCES
CHECK WHICH SUBSTRING MULTIPLIED BY NUMBER OF OCCURENCES IS EQUAL TO THE STRING
RETURN THE SUBSTRING AND NUMBER OF OCCURENCES AS A TUPLE

    Set substring_occurrence to an empty dictionary
    Set substring_match to an empty dictionary
    For letter in string:
        For letter in string start from next letter and ending at the length of string
            If string sliced from current letter to next letter is not in substring_occurrence
                Add string and occurrence of 1 to substring_occurrence
            Else
                Add 1 to the occurrence at sliced string in substring_occurrence
    For substring and number of occurrences in substring_occurrence
        if substring * number of occurrences is equal to string
            Add the substring and number of occurrences to substring_match
    Set min_length to the first substring's length
    For substring in substring_match
        if length of substring is less than min_length
            change min_length to the length of substring
    For substring and number of occurrences in subsring_match
        if length of substring is equal to min_length
            return the tuple of substring and number of occurrences
'''
def repeated_substring(string):
    substring_occurrence = {}
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i:j + 1] not in substring_occurrence:
                substring_occurrence[string[i:j + 1]] = 1
            else:
                substring_occurrence[string[i:j + 1]] += 1
    substring_match = {substring: occurrences for substring, occurrences in substring_occurrence.items()
                                              if substring * occurrences == string}
    shortest_substring = sorted(substring_match, reverse=False, key=len)[0]
    return shortest_substring, substring_match[shortest_substring]
    
print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))



'''
Create a function that takes a string as an argument and returns True if the string is a pangram, 
False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. For example, the 
sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. 
Note that case is irrelevant.
'''

'''
Given a string return True if the string is a pangram (sentence that includes all letters of alphabet) 
else return False.
Case insensitive
DS: set
Algo
CREATE A SET OF LETTERS FROM SENTENCE
CHANGE SET TO A STRING OF LETTERS
RETURN TRUE IF SET IS EQUAL TO THE ALPHABET ELSE FALSE

    Set letters to an empty set
    For each character in sentence
        If character is a letter
            Add the lowercase version of character to letters
    Return True if letters is equal to the alphabet otherwise return false

CHANGE SET TO A STRING OF LETTERS
    Set string_letters to an empty string
    For each letter in letters
        Append letter to string_letters
    Return string_letters sorted from a - z

'''
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def is_pangram(sentence):
    letters = set()
    for char in sentence:
        if char.isalpha():
            letters.add(char.lower())
    return (True if set_to_str(letters) == ALPHABET else False)

def set_to_str(letters):
    string_letters = ''
    for letter in letters:
        string_letters += letter
    return ''.join(sorted(string_letters))

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)


'''
Create a function that takes two strings as arguments and returns True if some portion of the characters 
in the first string can be rearranged to match the characters in the second. Otherwise, the function should 
return False.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will 
be empty.
'''

'''
Given two strings return True if characters from first string can be moved to match the second string.
You cannot use a letter from first string more than once to match the 2nd string
Lowercase and Alphabetic only

DS: list, string, join
Algo:
CREATE A LIST OF CHARACTERS USING THE FIRST STRING TO MATCH THE 2ND STRING
    Set matching_char to an empty string
    For char in first string:
        if char is in the 2nd string
            Append char to matching_char
    Return True if the length of matching_char is equal to the length of the 2nd string

'''
def unscramble(str1, str2):
    matching_char = ''
    for char in str1:
        if char in str2:
            matching_char += char
    return True if len(matching_char) == len(str2) else False

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)

'''
Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 
11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these 
multiples is 75.

If the argument is negative, return 0.
'''
'''
Given an integer return the sum of all multiples of 7 or 11 that are less than the integer.
Sum the multiple just once if it is both a multiple of 7 and 11
Return 0 if the argument is less than 0
DS: list, integer
Algo:
CREATE A LIST OF INTEGERS FROM 1 TO INTEGER EXCLUSIVE
ITERATE THROUGH THE LIST AND COUNT IF THE NUMBER IS AN MULTIPLE OF 7 OR 11
RETURN THE COUNT
    Set integers to an empty list
    Set sum_of_multiples to 0
    For number starting from 1 to integers (exclusive)
        Append number to integers
    For each number in integers:
        if integer is multiple of 7 or is multiple of 11
            Add integer to sum_of_multiples
    Return count

    is_multiple_of(num, multiple)
        if mutiple % num is equal to 0
            return True
        return False
'''
def seven_eleven(integer):
    integers = []
    sum_of_multiples = 0
    for num in range(1, integer):
        integers.append(num)
    for num in integers:
        if is_multiple_of(7, num) or is_multiple_of(11, num):
            sum_of_multiples += num
    return sum_of_multiples

def is_multiple_of(num, multiple):
    return multiple % num == 0

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

'''
Create a function that takes a string argument that consists entirely of numeric digits and computes 
the greatest product of four consecutive digits in the string. The argument will always have more than 
4 digits.
'''

'''
Given a string greater than 4 digits return the computation of the four greatest consecutive digits 
in the string
DS: list, sublist, 
Algo:
CREATE A SUBLIST OF 4 CONSECUTIVE DIGITS
CALCULATE THE MAX PRODUCT OF THE SUBLIST
    Set consecutive_digits to an empty list
    Set the max to None
    For each digit in digits
        Append the 4 consecutive digits to consecutive_digits
    Return max_product(consecutive_digits)

    max_product
        Set max to 0
        For each digits in consecutive_digits
            Set product equal to 1
            if the length of digits > 4
                for each digit in digit
                    Mutliple digit (integer) to product
            if product > max:
                Set max equal to product
        return max
'''
def greatest_product(digits):
    consecutive_digits = []
    for i in range(len(digits)):
        consecutive_digits.append(digits[i:i+4])
    return max_product(consecutive_digits)

def max_product(consecutive_digits):
    max_prod = 0
    for digits in consecutive_digits:
        product = 1
        if len(digits) == 4:
            for digit in digits:
                product *= int(digit)
        if product > max_prod:
            max_prod = product
    return max_prod

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

'''
Create a function that returns the count of distinct case-insensitive alphabetic characters and 
numeric digits that occur more than once in the input string. You may assume that the input string 
contains only alphanumeric characters.
'''
'''
given a string of alphanumeric characters return the number of characters that occur more than once
DS: dictionary of occurrences, string, integer
Algo:
CREATE A DICTIONARY OF OCCURRENCES
ITERATE THROUGH DICTIONARY AND COUNT HOW MANY OCCUR MORE THAN ONCE
RETURN THE COUNT
    Set occurences to an empty dictionary
    Set count = 0
    For each character in string
        If character is not in occurences
            Add character with a value of 1
        Else
            Add 1 to the value at character
    For each char and occurrence in occurrences
        If occurrence is greater than 1
            Add 1 to count
    Return count
'''
def distinct_multiples(string):
    occurrences = {}
    count = 0
    for char in string:
        char = char.casefold()
        if char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1
    for occurrence in occurrences.values():
        if occurrence > 1:
            count += 1
    return count
print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5


'''
Create a function that takes a list of integers as an argument. The function should determine the 
minimum integer value that can be appended to the list so the sum of all the elements equals the 
closest prime number that is greater than the current sum of the numbers. 
For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. 
Thus, we can add 1 to the list to sum to 7.

Notes:

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.
'''
'''
Given a list of integers return the difference between the sum of the integers and its nearest prime number
DS: integer, bool
Algo:
SUM ALL OF THE INTEGERS
FIND THE NEAREST PRIME NUMBER STARTING FROM THE SUM + 1
RETURN THE DIFFERENCE BETWEEN THE SUM AND PRIME NUMBER
    Set sum_of_integers to the sum of integers
    Set nearest_number to sum_of_integers + 1
    While nearest_number is not prime
        nearest_number += 1
    Return nearest_number - sum_of_integers
IS PRIME NUMBER
    For each number starting from 2 to nearest_number
        if nearest_number % number == 0
            return True
    return False
'''
def nearest_prime_sum(integers):
    sum_of_integers = sum(integers)
    nearest_number = sum_of_integers + 1
    while not_prime(nearest_number):
        nearest_number += 1
    return nearest_number - sum_of_integers

def not_prime(nearest_number):
    return any(number for number in range(2, nearest_number)
                          if nearest_number % number == 0)

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)


'''
Create a function that takes a list of integers as an argument. Determine and return the index N for 
which all numbers with an index less than N sum to the same value as the numbers with an index greater than N. 
If there is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the 
last element is 0.
'''
'''
Given a list of integers return the index where the sum of all the numbers with an index less than 
the current index are equal to the sum of all the numbers with an index greater than the current index

DS: list to save the index where the sums equal each other, slicing, integer, sum
Algo:
ITERATE THROUGH THE INDICES AND FIND IF THE SUM OF THE INTEGERS ARE EQUAL
SAVE THE INDICES THAT THE SUMS ARE EQUAL TO EACH OTHER TO A LIST
RETURN THE MINIMUM INDEX FROM THE LIST

    Set indices to an empty list
    For each index in list of integers
        if index is equal to 0
            if sum of all indices from 1 to end is equal to 0 append index to indices
            continue
        if index is equal to the length of list of integers - 1
            if sum of all indices from 0 to last index - 1 is equal to 0 append index to indices
            continue
        if sum of all indices from 0 to current index is equal to current index + 1 to the end of the list
            append index to indices
    Return the minimum value from indices if indices else return -1
'''
def equal_sum_index(integers):
    indices = []
    length = len(integers)
    for idx in range(length):
        if idx == 0:
            if sum(integers[1:length]) == 0:
                indices.append(idx)
        elif idx == length - 1:
            if sum(integers[0:length - 1]) == 0:
                indices.append(idx)
        if sum(integers[0:idx]) == sum(integers[idx + 1:]):
            indices.append(idx)
    return min(indices) if indices else -1
        

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)

'''
Create a function that takes a list of integers as an argument and returns the integer that appears 
an odd number of times. There will always be exactly one such integer in the input list.
'''
'''
Given a list of integers return the integer that occurs an odd number of times.
DS: dictionary, integer
Algo:
CREATE A DICTIONARY OF OCCURRENCES
RETURN THE INTEGER THAT HAS AN ODD OCCURRENCE

    Set occurrences to an empty dictionary 
    For each integer in integers
        If integer is not in occurrences
            Add integer with a value of 1 to occurrences
        Else
            Add 1 to the value at integer in occurrences
    For integer, occurrence in occurrences:
        Return integer if occurrence is odd
'''
def odd_fellow(integers):
    occurrences = {}
    for integer in integers:
        if integer not in occurrences:
            occurrences[integer] = 1
        else:
            occurrences[integer] += 1
    for integer, occurrence in occurrences.items():
        if is_odd(occurrence):
            return integer

def is_odd(integer):
    return integer % 2 > 0

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

'''
Create a function that takes a list of numbers, all of which are the same except one. 
Find and return the number in the list that differs from all the rest.

The list will always contain at least 3 numbers, and there will always be exactly one number that 
is different.
'''
'''
Given a list of numbers return the number that is unique
DS: Dictionary
Algo:
CREATE A DICTIONARY OF NUMBERS AND THEIR OCCURRENCES
RETURN THE NUMBER WITH THE OCCURRENCE EQUAL TO 1
    Set result to an empty dictionary
    For each integer in integers:
        if integer is not in result
            Add the integer and occurrence to result
        else
            Add 1 to occurrence at integer in result
    For integer, occurrence in result
        Return integer if the occurrence is equal to1
'''
def what_is_different(integers):
    result = {}
    for integer in integers:
        if integer not in result:
            result[integer] = 1
        else:
            result[integer] += 1
    for integer, occurrence in result.items():
        if occurrence == 1:
            return integer


print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)
'''
'''

AMAA_GROSS_PROFIT = [
  {'amazon': 114.9},
  {'meta': 94.8},
  {'apple': 170.7},
  {'alphabet': 97.7},
]

def key_function(profit_dict):
    for profit in profit_dict.values():
        return profit

def profit_sort(profits_list):
    return sorted(profits_list, key=key_function, reverse=True)

print(profit_sort(AMAA_GROSS_PROFIT))
# [
#   {'apple': 170.7},
#   {'amazon': 114.9},
#   {'alphabet': 97.7},
#   {'meta': 94.8},
# ]

numbers = [1, 2, 3, 2, 1, 4, 5, 5]
numbers_str = []
for number in numbers:
    if str(number) not in numbers_str:
        numbers_str.append(str(number))

unique_numbers = numbers_str

concatenated_string = ''.join(unique_numbers)
print(concatenated_string) # 12345

'''
'''
AMAA_GROSS_PROFIT = [
  {'amazon': 114.9},
  {'meta': 94.8},
  {'apple': 170.7},
  {'alphabet': 97.7},
]

def dictionary_generator(profits_list):
    return {company: profit for companies in profits_list
                            for company, profit in companies.items()}

print(dictionary_generator(AMAA_GROSS_PROFIT))
# {'amazon': 114.9, 'meta': 94.8, 'apple': 170.7, 'alphabet': 97.7}

'''
'''
def enemies_present(characters):
    return any([character["character_type"] == "enemy" for character in characters])

enemies_present([
  {"character_type": "enemy", "hit_points": 100, "defense": 3},
  {"character_type": "NPC", "hit_points": 80, "defense": 6},
  {"character_type": "teammate", "hit_points": 300, "defense": 7},
])  # Should return True

enemies_present([
  {"character_type": "NPC", "hit_points": 20, "defense": 1},
  {"character_type": "NPC", "hit_points": 80, "defense": 6},
  {"character_type": "teammate", "hit_points": 300, "defense": 7},
  {"character_type": "Quest Giver", "hit_points": 1000, "defense": 10},
])  # Should return False

'''
'''
input_list = ["apple", "banana", "cherry", "date"]

word_length = {word: len(word) for word in input_list}

print(word_length)

'''
'''
def names_youngest_to_oldest(people):
    names = list(people.keys())

    return sorted(ages)

# Test Cases
people_1 = {'jim': 50, 'jill': 25, "artemis": 42, 'johnny': 37, 'earl': 65}
people_2 = {'alexandra': 5, 'bob': 94, "jolene": 44, 'demosthenes': 26}
people_3 = {'sigmund': 10, 'jane': 21, "colin": 17}

print(names_youngest_to_oldest(people_1) == ['jill', 'johnny', 'artemis', 'jim', 'earl'])
print(names_youngest_to_oldest(people_2) == ['alexandra', 'demosthenes', 'jolene', 'bob'])
print(names_youngest_to_oldest(people_3) == ['sigmund', 'colin', 'jane'])


'''
'''

frozenset1 = frozenset({1, 2, 3, 4, 5})
frozenset2 = frozenset({4, 5, 6, 7, 8})
frozenset3 = frozenset({4, 5})

print(frozenset1.isequalto(frozenset2))   # False
print(frozenset1.hasthefollowing(frozenset3))   # True

'''
'''

'''
Given a 2D array containing a bomb determined by a 1 return the row index and column index 
of where the bomb is found
DS: list, integer
Algo:
ITERATE THROUGH EACH ROW AND COLUMN TO FIND WHERE THE BOMB IS
SAVE THE ROW INDEX AND COLUMN INDEX TO A LIST
RETURN THE LIST CONTAINING ROW INDEX AS 1ST ELEMENT AND COLUMN INDEX AS 2ND ELEMENT
    Set bomb_location to an empty list
    For row in grid
        For column in grid
            If element at column is equal to 1
                Append bomb_location with row and column
    Return bomb_location
'''
def mine_location(grid):
    row_location = [row_idx for row_idx in range(len(grid))
                             for column_idx in range(len(grid[row_idx]))
                             if grid[row_idx][column_idx] == 1]
    column_location = [column_idx for row_idx in range(len(grid))
                                  for column_idx in range(len(grid[row_idx]))
                                  if grid[row_idx][column_idx] == 1]
    return row_location + column_location

# The below tests should each print True.
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0])
print(mine_location([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == [1, 1])
print(mine_location([[0, 0, 0], [0, 0, 0], [0, 1, 0]]) == [2, 1]) 
print(mine_location([[1, 0], [0, 0]]) == [0, 0])
print(mine_location([[1, 0, 0], [0, 0, 0], [0, 0, 0]]) == [0, 0]) 
print(mine_location([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]) == [2, 2])

'''
'''
'''
Given string 1 and string 2 return True if string 1 characters can be rearranged to match string 2 character
Algo:
IF CHARACTERS IN STRING 1 ARE IN STRING 2 SAVE TO A NEW STRING
CHECK IF THE NEW STRING IS THE SAME LENGTH AS STRING 2
    Set new_string to an empty string
    Set occurrences to an empty dictionary
    For each character in string 2
        If character is not in occurrences
            Add character with value of 1 to occurrences
        Else
            Add 1 to the value at character in occurrences
    For each chatacter in string 1
        If character is in string 2 and the occurences is greater than 0
            Append the character to string 1
            Subtract 1 from the value of character in occurrences
    return length of new_string is equal to length of string 2
'''
def scramble(str1, str2):
    new_string = ''
    occurrences = {}
    for char in str2:
        if char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1
    for char in str1:
        if char in str2 and occurrences[char] > 0:
            new_string += char
            occurrences[char] -= 1
    return len(new_string) == len(str2)

# The below tests should each print True.
print(scramble('rkqodlw', 'world') == True)
print(scramble('cedewaraarossoqqyt', 'carrot') == True)
print(scramble('scriptjava', 'javascript') == True)
print(scramble('scriptingjava', 'javascript') == True)
print(scramble('katas', 'steak') == False)

'''
'''
'''
Given a string return a dictionary of occurrences of each character sorted by the highest to lowest
Characters are alpha only, sorted alphabetical and not case sensitive
DS: dictionary (num_occurrences: [letters]), list, integer, string, set
Algo:
CREATE A DICTIONARY OF LOWERCASE LETTERS AND ITS OCCURRENCES
CREATE A DICTIONARY OF OCCURRENCES AND ITS LETTERS AS A LIST
SORT DICTIONARY OF OCCURRENCES AND LETTERS AS A LIST
    Set letter_occurrences to an empty dictionary
    Set occurrence_keys to an empty_dictionary
    For each letter in string
        If letter is not in letter_occurrences
            Add letter with a value of 1 to letter_occurrences
        else
            Add 1 to the value of letter in letter_occurrences
    For each letter and occurrence in letter_occurrences
        If occurrence is not in occurrence_keys
            Add the occurence as a key and letter inside of a list as a value
        else
            Add the letter to the list at the occurrrence key
    Sort occurrence_keys from highest to lowest keys
    Sort occurrence_keys lists as values from highest to lowest

    For each list in occurrence keys
        return list
'''
def get_char_count(string):
    letter_occurrences = {}
    occurrence_keys = {}
    for char in string:
        char = char.lower()
        if char.isalnum():
            if char not in letter_occurrences:
                letter_occurrences[char] = 1
            else:
                letter_occurrences[char] += 1
    occurrences = sorted(list(set(letter_occurrences.values())), reverse=True)
    for occurrence in occurrences:
        for letter, value in letter_occurrences.items():
            if occurrence not in occurrence_keys and value == occurrence:
                occurrence_keys[occurrence] = [letter]
            elif value == occurrence:
                occurrence_keys[occurrence].append(letter)
    for values in occurrence_keys.values():
        values.sort()
    return occurrence_keys

# The below tests should each print True.
print(get_char_count("Mississippi") == {4: ['i', 's'], 2: ['p'], 1: ['m']})
print(get_char_count("Hello. Hello? HELLO!!") == {6: ['l'], 3: ['e', 'h', 'o']})
print(get_char_count("aaa...bb...c!") == {3: ['a'], 2: ['b'], 1: ['c']})
print(get_char_count("aaabbbccc") == {3: ['a', 'b', 'c']})
print(get_char_count("abc123") == {1: ['1', '2', '3', 'a', 'b', 'c']})

'''
'''
'''
Given a string and sometimes minor words convert the string to title case with words in minor words to be
ignored and kept as lower case

DS: string, list (split)

Algo:
CREATE A LIST OF MINOR_WORDS FROM 2ND PARAMETER IF IT IS THERE
CREATE A LIST OF WORDS FROM STRING
CREATE A LIST OF TILE FROM WORDS
RETURN THE LIST OF TITLE

    Set minor_words to a list of minor words split by a space
    Set words to a list of words from string split by a space
    Set title to an empty list
    For each word in words
        if word is in minor_words
            Append lowercase version of word to title
        else
            Append the title case version of word to title
    return the title as a string joined by a space

'''
def title_case(string, minor=[]):
    if minor:
        minor = minor.lower().split()
    words = string.split()
    title = []
    for idx, word in enumerate(words):
        if idx == 0:
            title.append(word.title())
        elif word.casefold() in minor:
            title.append(word.lower())
        else:
            title.append(word.title())
    return ' '.join(title)

# The below tests should each print True.
print(title_case('a clash of KINGS', 'a an the of') == 'A Clash of Kings')
print(title_case('THE WIND IN THE WILLOWS', 'The In') == 'The Wind in the Willows')
print(title_case('the quick brown fox') == 'The Quick Brown Fox')

'''
'''
'''
Given a positive integer return the number of times you multiply each of the digits to reach a single digit
DS: string, integer
Algo:
KEEP MULTIPLYING THE DIGITS UNTIL THERE IS ONLY ONE
    Set digits to string version of positive integer
    Set count equal to 0
    While the length of digits is greater than 1:
        Set number equal 1
        For each digit in digits:
            multiply number by the integer version of digit
        Set digits equal to the string version of number
        Add 1 to count
    Return count      
'''
def persistence(number):
    digits = str(number)
    count = 0
    while len(digits) > 1:
        number = 1
        for digit in digits:
            number *= int(digit)
        digits = str(number)
        count += 1
    return count


# The below tests should each print True.
print(persistence(39) == 3) # should return 3, because 3*9=27, 2*7=14, 1*4=4 and 4 has only one digit
print(persistence(999) == 4) # should return 4, because 9*9*9=729, 7*2*9=126, 1*2*6=12, and finally 1*2=2
print(persistence(4) == 0) # should return 0, because 4 is already a one-digit number
print(persistence(25) == 2) # should return 2, because 2*5=10, and 1*0=0

'''
'''
'''
Given a number return an expanded form as a string.
DS: String, join, list
Algo: turn into a string take out each digit with additional 0s and append to list then join them
CONVERT NUMBER INTO A STRING
TAKE OUT EACH DIGIT WITH ADDTL 0S AND ADD TO A LIST
RETURN THE JOIN LIST
    Set digits to a string conversion of number
    Set numbers to an empty list
    Set numbers_with_zeros to an empty list
    For each digit in digits
        Append digit from current digit to end of digits
    For number in numbers:
        Set length equal to the length of number
        Set number_with_zeros to the first element of number
        While the length of number_with_zero is less than length
            Append zero to number_with_zeros
        Append number_with_zeros to numbers_with_zeros
    Return the joined numbers_with_zeros using ' + '
'''
def expanded_form(number):
    digits = str(number)
    numbers = []
    numbers_with_zeros = []
    numbers_filter_zeros = []
    for idx in range(len(digits)):
        numbers.append(digits[idx:])
    for idy in range(len(numbers)):
        length = len(numbers[idy])
        number_with_zeros = numbers[idy][0]
        while len(number_with_zeros) < length:
            number_with_zeros += '0'
        numbers_with_zeros.append(number_with_zeros)
    for number in numbers_with_zeros:
        if int(number) > 0:
            numbers_filter_zeros.append(number)
    return ' + '.join(numbers_filter_zeros)

# The below tests should each print True.
print(expanded_form(12) == '10 + 2')
print(expanded_form(42) == '40 + 2')
print(expanded_form(70304) == '70000 + 300 + 4')

'''
'''
'''
Given a string of one or more words return a string with words of five or more letters reversed
DS: split, list, string
Algo:
CREATE A LIST OF WORDS
ITERATE THOUGH WORDS AND REVERSE WORDS WITH MORE THAN 5 LETTERS
RETURN NEW LIST
    Set words to a split version of string
    Set words_reverse to an empty list
    For word in words
        If the length of words is greater than or equal to 5
            Append the reverse version of word to words_reverse
        Else
            Append word to words_reverse
    Return a join version of words_reverse using ' '
'''
def spin_words(string):
    words = string.split()
    words_reverse = []
    for word in words:
        if len(word) >= 5:
            words_reverse.append(word[::-1])
        else:
            words_reverse.append(word)
    return ' '.join(words_reverse)

# The below tests should each print True.
print(spin_words("Hey fellow warriors") == "Hey wollef sroirraw")
print(spin_words("This is a test") == "This is a test")
print(spin_words("This is another test") == "This is rehtona test")

'''
'''
'''
Given a list of directions return True if the directions take 10 minutes (len of 10) and it returns
you back to the starting point otherise return False
'n' = +1
's' = -1
'w' = +1
'e' = -1
DS: list, integer
Algo:
FIND THE LENGTH OF THE DIRECTION
ITERATE THROUGH THE DIRECTION AND ADD/SUBTRACT THEM UP
    Set direction_length to the length of directions
    Set count = 0
    If the direction_length is not equal to 10
        Return False
    For each direction in directions
        If direction is equal to 'n' or 'w'
            Add 1 to count
        Elif direction is equal to 's' or 'e'
            Subtract 1 from count
    Return count is equal to 0
'''
def is_valid_walk(directions):
    direction_length = len(directions)
    count = 0
    if direction_length != 10:
        return False
    for direction in directions:
        if direction in 'nw':
            count += 1
        elif direction in 'se':
            count -= 1
    return count == 0

# The below tests should each print True.
print(is_valid_walk(['n','s','n','s','n','s','n','s','n','s']) == True)
print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']) == False)
print(is_valid_walk(['w']) == False)
print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']) == False)


'''
LSBOT stuff
'''

'''
Problem 1
given a string and a characer return the index os the second occurence of char in text if it appears
otherwise return -1
Algo:
FINDS THE INDEX AT THE 2ND OCCURRENCE OF CHAR IN TEXT

'''
def find_second_occurrence(text, char):
    first_index = text.find(char)
    second_index = text.find(char, first_index + 1)
    return second_index

print(find_second_occurrence('aba', 'a') == 2)
print(find_second_occurrence('ab', 'a') == -1)
print(find_second_occurrence('acbacad', 'a') == 3)

'''
Problem 2
Given a string return a stripped version with old susbstring replaced with new substring
STRIP THE STRING
REPLACE THE OLD WITH NEW
'''
def clean_and_replace(text, old, new):
    return text.strip().replace(old, new)

'''
Problem 3
Given a list of numbers return a the list of numbers with the sum of the two middle elements if even
or middle element twice if odd appended to between the two middle elements if even or before the middle
element if odd

Algo:
SUM THE TWO MIDDLE NUMBERS OR MIDDLE NUMBER TWICE
INSERT THE SUM TO THE LIST
RETURN THE LIST
    Set length equal to length of numbers
    If the length is even
        Set right_index to length integer divided by 2
        Set left_index to right_index subtract 1
        Set sum_of_elements equal to the sum of the two middle elements at right_index and left_index
        Insert sum_of_elements in between the two middle elements
    If the length is odd
        Set middle_index to length integer divided by 2
        Set sum_of_elements equal to the sum of the middle element twice at middle_index
        Insert sum_of_elements before the middle element
    Return numbers
'''

def insert_middle_sum(numbers):
    length = len(numbers)
    if length % 2 == 0:
        right_index = length // 2
        left_index = right_index - 1
        sum_of_elements = numbers[left_index] + numbers[right_index]
        numbers.insert(right_index, sum_of_elements)
    elif length % 2 != 0:
        middle_index = length // 2
        sum_of_elements = numbers[middle_index] + numbers[middle_index]
        numbers.insert(middle_index, sum_of_elements)
    return numbers

print(insert_middle_sum([10, 20, 30, 40]) == [10, 20, 50, 30, 40])
print(insert_middle_sum([1, 2, 3]) == [1, 4, 2, 3])

'''
Problem 4
Given list1 and list2 return nothing, but mutate list1 to include list2 and sort in descending order
'''
def merge_and_sort_desc(list1, list2):
    list1.extend(list2)
    list1.sort(reverse=True)

lista = [1]
listb = [2]

print(merge_and_sort_desc(['a'], ['b']) == None)
print(merge_and_sort_desc(lista, listb) == None)
print(lista == [2, 1])

'''
Problem 5

The key difference between the built-in `sorted()` function and the `list.sort()` method is that
the `sorted()` function returns a new list while `list.sort()` method returns None.

I would choose `sorted()` function if I needed a new list and needed to return a new list
and maintain the old list
I would choose `list.sort()` method if I needed to mutate the list that the method was
called upon in order to return the same list that the method was called upon.

In code it will look like this
'''
old_list_ascending = [1, 2, 3]
new_list_descending = sorted(old_list_ascending, reverse=True)
print(old_list_ascending, new_list_descending) # [1, 2, 3] [3, 2, 1]

letters = ['a', 'b', 'c']
letters.sort(reverse=True)
print(letters) # ['c', 'b', 'a']

'''
Problem 6
'''

numbers = [1, 3, 2, 5, 4, 7, 6]

for number in numbers[:]:
    if number % 2 != 0:
        numbers.remove(number)

print(numbers)
# Actual Output: [3, 2, 4, 6]
# Expected Output: [2, 4, 6]

'''
The code fails because as the code iterates through numbers and removes a num so the current num is going
to move to the next index even if the intent is to just remove num and move to next number not next index.
So in order to fix that we need to iterate through the list until there are no more odd numbers by
controlling the index using a while loop instead of a for loop and adding an check to see if
there are any more odd numbers inside of numbers
'''

'''
Problem 7
Given a string return a dictionary where keys are the characters and values are their frequencies
use dict.get() with a default value to simplify the code
'''
def character_frequency(text):
    dictionary = {}
    for character in text:
        dictionary[character] = dictionary.get(character, 0) + 1
    return dictionary

print(character_frequency('abc') == {'a': 1, 'b': 1, 'c': 1})
print(character_frequency('xxyyyzzzz') == {'x': 2, 'y': 3, 'z': 4})
print(character_frequency('joepen') == {'j': 1, 'o': 1, 'p': 1, 'e': 2, 'n': 1})

'''
Problem 8
Given a list of words return a dictionary of first letter of each word as a key and
corresponding words from the list of words that start with that letter
'''

def build_word_index(words):
    dict_words = {}
    for word in words:
        first_letter = word[0]
        dict_words.setdefault(first_letter, [])
        dict_words[first_letter].append(word)
    return dict_words

print(build_word_index(['ayo', 'ally', 'airplane', 'billy', 'bob', 'banjo']) == {'a': ['ayo', 'ally', 'airplane'], 'b': ['billy', 'bob', 'banjo']})

'''
Problem 9
You have two dictionaries, defaults = {'theme': 'light', 'font_size': 12} 
and user_prefs = {'font_size': 14, 'language': 'en'}. 
Write a single line of code that modifies the defaults dictionary to include the settings from 
user_prefs, overwriting any existing keys. Which dictionary method would you use?
'''
defaults = {'theme': 'light', 'font_size': 12} 
user_prefs = {'font_size': 14, 'language': 'en'}
defaults.update(user_prefs)
print(defaults)

'''
Problem 10
Describe the difference between the dict.pop(key) and dict.popitem() methods. What are their return values? 
What happens if you call pop() with a key that doesn't exist, 
and how can you prevent a KeyError in that scenario?

The difference between dict.pop(key) and dict.popitem() methods is that dict.pop(key) would remove
the key and values at key in dict and returns the value. dict.popitem() would remove the last entered
key and value in dict and returns the (key, value)
If you call pop() with a key that doesn't exist the code will raise a KeyError. In order to prevent a
KeyError the second argument of pop() should include a 2nd argument
'''

'''
Problem 11
1. A set of students who are in both clubs
2. A set of students who are only in the math clubs
3. A frozenset of all unique students from both clubs
'''

math_club = ['Alice', 'Bob', 'Charlie']
science_club = ['Bob', 'Diana', 'Eve']


def analyze_clubs(math_students, science_students):
    maths = set(math_students)
    sciences = set(science_students)
    intersect = maths.intersection(sciences)
    difference = maths.difference(sciences)
    mathfs = frozenset(maths)
    sciencefs = frozenset(sciences)
    unique = mathfs.union(sciencefs)
    return intersect, difference, unique 

print(analyze_clubs(math_club, science_club))

'''
Problem 12
What is the primary difference between a set and a frozenset? 
Explain a situation where using a frozenset is necessary or more appropriate than using a set.

Primary difference between a set and frozenset is the mutability. A set is mutable and a frozenset is 
immutable. A frozenset would be necessary if the unique members should not be changed, modified,
updated or of the sorts. For example, for a set of color like ROYGBIV I would want that to be
a frozenset because I do not want to change what is defined as ROYGBIV. However, if I do want to add
in another color then I would make it a set instead.
'''

'''
Problem 13
Write a function has_required_skills(required, candidate) that takes two sets of strings: 
required skills for a job and candidate skills.The function should return True if the candidate 
possesses all the required skills, and False otherwise. Which set method is most appropriate here?

issuperset would work because it could check if candidate skills are a superset of required skills
issubset would work because it could check if required skills is a subset of candidate skills

I went with issuperset so it matches to question if the candidate possesses all required skills
aka candidate is superset of required.
'''
def has_required_skills(required, candidate):
    return set(candidate).issuperset(set(required))

print(has_required_skills('abc', 'abce') == True)
print(has_required_skills('abc', 'abcd') == True)
print(has_required_skills('abcde', 'abcd') == False)

'''
Problem 14
Given a list of tuples, where each tuple contains a product name, price, and quantity 
(e.g., [('Apple', 0.50, 10), ('Banana', 0.25, 5)]), use a for loop with tuple unpacking to iterate 
through the list and print the total cost for each product in the format: "10 Apples will cost $5.00".
'''
tuple_list = [('Apple', 0.50, 10), ('Banana', 0.25, 5)]
for product, price, quantity in tuple_list:
    print(f"{quantity} {product}s will cost ${price * quantity:.2f}.")

'''
Problem 15
Write a function sum_every_other(numbers) that returns the sum of the elements at even indices (0, 2, 4, ...).
Implement this once using enumerate and a conditional check, and a second time using list slicing.
'''
def sum_every_other(numbers):
    result = 0
    for idx, number in enumerate(numbers):
        if idx % 2 == 0:
            result += number
    return result

def sum_every_other(numbers):
    return sum(numbers[::2])

print(sum_every_other([1, 2, 3, 4, 5]) == 9)

'''
Problem 16
Write a function is_valid_matrix(matrix) that takes a list of lists (a matrix). 
It should return True if all inner lists have the same, non-zero length. 
Otherwise, it should return False. Use the all() function and a list comprehension or generator expression 
for a concise solution.

Example:
is_valid_matrix([[1,2], [3,4]]) should return True.
is_valid_matrix([[1,2], [3,4,5]]) should return False.
is_valid_matrix([[], []]) should return False.
'''

'''
Save the first length of first inner list and check if it matches
Check if each inner list has the same  non-zero length
'''

def is_valid_matrix(matrix):
    if not matrix or not matrix[0]:
        return False

    return all(len(row) == len(matrix[0]) for row in matrix)

print(is_valid_matrix([[1,2], [3,4]]) == True)
print(is_valid_matrix([[1,2], [3,4,5]]) == False)
print(is_valid_matrix([[], []]) == False)

'''
Problem 17
Given a list of strings, write a function sort_by_length(words) that sorts the list in-place from 
shortest string to longest. Use the key parameter of the list.sort() method.
'''

def sort_by_length(words):
    words.sort(key=len)

words = ['aaaa', 'aa', 'aaa', 'a']
sort_by_length(words)

print(words == ['a', 'aa', 'aaa', 'aaaa'])

'''
Problem 18
You have a list of dictionaries, each representing a 
person: people = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 30}].
Write code to sort this list first by age in descending order (reverse=True), and then by name 
alphabetically for people with the same age.
'''

people = [{'name': 'Charlie', 'age': 30}, {'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
people.sort(key=lambda person: person['name'])
people.sort(key=lambda person: person['age'], reverse=True)
print(people)


'''
19. (Basic) Dictionary Comprehension

Given a list of words ['apple', 'banana', 'cherry'], use a dictionary comprehension to create a dictionary 
where the keys are the words and the values are the lengths of the words. The result should be 
{'apple': 5, 'banana': 6, 'cherry': 6}.
'''
print({fruit: len(fruit) for fruit in ['apple', 'banana', 'cherry']})


'''
20. (Advanced) Shallow vs. Deep Copy

Consider the following code. After it executes, what will be the final values of list_a, list_b, and list_c? 

Explain why the modification to list_a affects list_b but not list_c.

import copy

list_a = [['X', 'O'], ['O', 'X']]
list_b = list_a.copy()
list_c = copy.deepcopy(list_a)

list_a[0][0] = 'Z'

list_a = [['Z', 'O'], ['O', 'X']] # references same sublists as list_b
list_b = [['Z', 'O'], ['O', 'X']] # references same sublists as list_a
list_c = [['X', 'O'], ['O', 'X']] # references new list and sublists

The modification to list_a affects list_b because the copy method creates a shallow copy of the list_a
so list_b will reference the same sublists as list_a. However, for list_c the copy.deepcopy method
creates a deepy copy of list_a so list_c references its own list and sublists.

'''

'''
Given a list of numbers return an all pairs

    Set ordered_array to a ordered input array from least to greatest
    Set sub_arrays to an empty array
    Set difference_of_2 to an empty array
    For each number in ordered_array starting from the first number ending at the 2nd to last number
        For each number in ordered_array starting from 2nd number ending at the last number
            Append pairs as a list to sub_arrays
    For each pair in sub_arrays
        If pairs have a difference of 2
            Append pair to difference_of_2
    Return difference_of_2

    Set sub_arrays to an empty array
    Set difference_of_2 to an empty array
    For each number in ordered_array starting from the first number ending at the 2nd to last number
        For each number in ordered_array starting from 2nd number ending at the last number
            Append pairs as a list to sub_arrays
    For each pair in sub_arrays
        If pairs have a difference of 2
            Append pair to difference_of_2 sorted from least to greatest
    Return difference_of_2 sorted by sum
'''
def differenceOfTwo(array):
    sub_arrays = []
    difference_of_2 = []
    for idx in range(len(array) - 1):
        for idy in range(1, len(array)):
            sub_arrays.append([array[idx], array[idy]])
    for pair in sub_arrays:
        if abs(pair[0] - pair[1]) == 2:
            difference_of_2.append(sorted(pair))
    
    return sorted(difference_of_2, key=sum)


print(differenceOfTwo([1, 2, 3, 4]) == [[1, 3], [2, 4]])
print(differenceOfTwo([4, 1, 2, 3]) == [[1, 3], [2, 4]])
print(differenceOfTwo([1, 23, 3, 4, 7]) == [[1, 3]])
print(differenceOfTwo([4, 3, 1, 5, 6]) == [[1, 3], [3, 5], [4, 6]])
print(differenceOfTwo([2, 4]) == [[2, 4]])
print(differenceOfTwo([1, 4, 7, 10, 13]) == [])

'''
EXAMPLE LOOP:
[1, 2, 3, 4] outer = 0, inner = 1
 ^  ^  = no match

[1, 2, 3, 4] outer = 0, inner = 2
 ^     ^  = match. `results` = [[1, 2]]

[1, 2, 3, 4] outer = 0, inner = 3
 ^        ^  = no match. `results` = [[1, 2]]

[1, 2, 3, 4] outer = 1, inner = 2
 ^  ^  = no match. `results` = [[1, 2]]

[1, 2, 3, 4] outer = 1, inner = 3
 ^     ^  = match. `results` = [[1, 2], [2, 4]]

[1, 2, 3, 4] outer = 2, inner = 3
    ^  ^  = no match. `results` = [[1, 2], [2, 4]]
'''

'''
Write a function that takes a string as input and counts the occurrences of each lowercase letter in the 
string. Return the counts in a dictionary where the letters are keys and their counts are values.
'''
'''
'''
def letter_count(string):
    string = sorted(list(string))
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result.setdefault(char, 1)
    return result

print(letter_count('launchschool') == { 'a': 1, 'c': 2, 'h': 2, 'l': 2, 'n':1, 'o': 2, 's':1, 'u': 1 })

'''
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, 
in descending order of the number of occurrences.

Assumptions:

A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)
Matches should be case-insensitive, and the words in the result should be lowercased.
Ties may be broken arbitrarily.
If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a 
lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps 
on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.")

# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words(" //wont won't won't")
# => ["won't", "wont"]

Given text with punctuation and line-breaks return an array of the top 3, 2, or 1 most frequent words in lowercase going from greatest to lowest
Return an empty array if a text contains no words
A word is one letter or more separated by a space and can contain on or more apostrophes


DS: list, dictionary, integer

Algo:
CREATE A LIST OF WORDS
COUNT EACH WORD AND SAVE TO A DICTIONARY OF WORDS (KEY) FREQUENCY (VALUE)
CREATE A LIST OF WORDS FROM GREATEST TO LEAST FREQUENCY

    Set words to an list of words split by spaces using text and should contain a lowercase version of letters and apostrophes
    Set frequency to an empty dictionary
    Set result to an empty list
    For each word in words
        if word is not in frequency
            Add word with value of 1 to frequency
        else
            Add 1 to the value of word in frequency
    Sort frequency by frequency values and return the list
    For each word and frequency in words
'''
def top_3_words(text):
    words = [word.lower() for word in text.split()]
    updated_words = []
    frequency = {}
    
    for word in words:
        updated_word = ''
        for char in word:
            if char.isalpha() or char == "'":
                updated_word += char
        if check_alpha(word):
            updated_words.append(updated_word)
    
    for word in updated_words:
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
    
    frequency = dict(sorted(list(frequency.items()), key=lambda frequency: frequency[1], reverse=True))
    
    return [count for count in frequency.keys()][0:3]

def check_alpha(word):
    result = ''
    for char in word:
        if char.isalpha():
            result += char
    return result

def sort_by_frequency(d):
    return d[1]

print(top_3_words("a a a b c c d d d d e e e e e")) # == ["e", "d", "a"])
# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e") == ["e", "ddd", "aa"])
# print(top_3_words(" //wont won't won't ") == ["won't", "wont"])
# print(top_3_words(" , e .. ")== ["e"])
# print(top_3_words(" ... ") == [])
# print(top_3_words(" ' ") == [])
# print(top_3_words(" ''' ") == [])
# print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing. An olla of rather more beef than mutton, a salad on most nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra on Sundays, made away with three-quarters of his income.""") == ["a", "of", "on"])

ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

def sorted_by_age(ages):
    return [name[0] for name in sorted(list(ages.items()), key=lambda ages: ages[1])]

print(sorted_by_age(ages))


books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def sort_by_published(books):
    return int(books['published'])

books.sort(key=sort_by_published)

print(books)


lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = [list() for i in range(len(lst))]

for idx, sublst in enumerate(lst):
    for idy, num in enumerate(sublst):
        if num % 3 == 0:
            new_lst[idx].append(num)

print(new_lst == [[], [3, 12], [9], [15, 18]])

'''
given a list return the middle element(s) in a new list
if odd return middle element
if even return both middle elements
if empty return an empty list
ds: list, integer
algo:
IF ODD GET THE MIDDLE ELEMENT
IF EVEN GET THE MIDDLE ELEMENTS
IF EMPTY RETURN AN EMPTY LIST
    If length of lst is odd
        Set middle element to length of list // 2
        Return the middle element in a new list
    If length of lst is even
        Set right element to length of list // 2
        Set left element to right element - 1
        Return the middle elements in a new list
    If lst is empty
        Return an empty list
'''

def middle_elements(lst):
    length = len(lst)
    if length == 0:
        return []
    elif length % 2 != 0:
        middle_element = length // 2
        return [lst[middle_element]]
    elif length % 2 == 0:
        right_element = length // 2
        left_element = right_element - 1
        return [lst[left_element], lst[right_element]]

print(middle_elements([1, 2, 3, 4, 5])) # Expected: [3]
print(middle_elements(['a', 'b', 'c', 'd'])) # Expected: ['b', 'c']
print(middle_elements([True, False])) # Expected: [True, False]
print(middle_elements([])) # Expected: []


def filter_long_strings(lst):
    return [element for element in lst
                    if convert_el(element) > 5]

def convert_el(element):
    if isinstance(element, list):
        return len(element)
    else:
        return len(str(element))

data = [10, 'hello', 'Python', 3.14, 'Launch School', False, [1, 2], 'hi']
filter_long_strings(data) # Expected: ['Python', 'Launch School']




d = {'a': 1, 'b': 2}
sorted(list(d.items()), key=lambda d: d[1])

def rand(number):
    pass

class Pet:

    def __init__(self, name):
        self.name = name
        type_name = self.__class__.__name__
        print(f'I am {name}, a {type_name}')

    def eat(self):
        print(f'{self.name}: Yum-yum=yum!')

class Dog(Pet):

    def speak(self):
        print(f'{self.name} says Woof!')

    def roll_over(self):
        print(f'{self.name} is rolling over.')

class Cat(Pet):
    
    def speak(self):
        print(f'{self.name} says Meow!')

class Parrot(Pet):

    def speak(self):
        print(f'{self.name} wants a cracker!')

sparky = Dog('Sparky')
fluffy = Cat('Fluffy')
polly = Parrot('Polly')

sparky.roll_over()

for pet in [sparky, fluffy, polly]:
    pet.speak()
    pet.eat()

class GoodDog:

    def __init__(self, name):
        # self.name is an instance variable (state)
        self.name = name
        print(f'Constructor for {self.name}')
    
    # speak is an instance method (behavior)
    def speak(self):
        # We're using the self.name instance variable
        print(f'{self.name} says Woof!')
    
    # roll_over is an instance method (behavior)
    def roll_over(self):
        # We're using the self.name instance variable
        print(f'{self.name} is rolling over.')

sparky = GoodDog('Sparky')
sparky.speak()
sparky.roll_over()

rover = GoodDog('Rover')
rover.speak()
rover.roll_over()

# sparky = GoodDog('Sparky', 5)
# rover = GoodDog('Rover', 3)


class Car:                      # (1) class object

    def __init__(self, make):   # (2) initializer used to create instances
        self.make = make        # (3) instance variable

    def honk(self):             # (4) method or instance behavior connected to class object
        print(f'{self.make} says Beep!')


toyota = Car('Toyota')          # (5) instance object of Car
honda  = Car('Honda')           # (6) instance object of Car

toyota.honk()                   # (7) instance using behavior

class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def description(self):
        return f'"{self.title}" by {self.author}'

    def is_written_by(self, name):
        return self.author == name


book1 = Book('The Pragmatic Programmer', 'Andy Hunt')
book2 = Book('Clean Code', 'Robert Martin')

print(book1.description())
print(book2.is_written_by('Robert Martin'))