"""
Sort Strings by Most Adjacent Consonants
Given a list of strings, sort the list based on the highest number of adjacent consonants a string contains 
and return the sorted list. If two strings contain the same highest number of adjacent consonants, 
they should retain their original order in relation to each other. Consonants are considered adjacent if 
they are next to each other in the same word or if there is a space between two consonants in adjacent words.
"""

# Inputs: list of strings
# Outputs: sorted list of strings based on the highest number of adjacent consonants a string contains
# Explicit
#     Sort the list based on the highest number of adjacent consonants a string contains
#     Adjacent consonants are consonants beside one another 
#     Adjacent consonants can be the last consonant and first consontant of two adjacent words
#     If two strings have the same highest number of adjacent consonants, they will retain their original order in the list
# Implicit
#    A string may contain zero characters, one character or multiple characters with spaces between them
# Questions
#     Should the current list be mutated or can a new list object be created?
#     Can a list be empty? 
#     Can a string contain one or more words? 
#     Does the string with highest number of adjacent consonants come first or last in the sorted string?
#     Does case sensitivity or special characters matter?

##
'''
'''
# Given a grid of values represented by an array of arrays, e.g.:
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9]

# Return the largest sum of a column of values in the grid.
# In this example, the largest sum is 18.

'''
Given: Grid of values
Return: Largest sum of column of values in the grid
Notes:
row[0][0] + row[1][0] + row[2][0]
row[0][1] + row[1][1] + row[2][1]
row[0][2] + row[1][2] + row[2][2]
DS: 
Algo:
create an empty list of sum_of_columns to 
iterate through row in grid:
    iterate through each column in row:
        add 
        
'''

# TEST CASES
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    # 12, 15, 18

b = [[1, 2, 3, 4],
     [5, 6, 7, 8]]
    # 6, 8, 10, 12

c = [[1, 0, 0],
     [5, 8, 10],
     [3, 5, 1]]
    # 8, 13, 11

print(largest_column(a) == 18)
print(largest_column(b) == 12)
print(largest_column(c) == 13)

def largest_column(a)


'''
given: string of lowercase characters
return: longest alphabetical substring
notes:
will be at least one letter long
return the one that appears first
a is less than b so a to z is lowest to greatest
ds: list, return string
algo:
    - edge case if lowercase character is 1 then return it
    - add each alphabetical ordered characters from the lowercase characters to a list
    set current index to 0
    for each character starting from 2nd character in lowercase characters
        if character is alphabetical
            append to the list
        add one to index
    - return the first longest set of ordered characters from the list

    - alphabetical
        return current character is after previous character
    
    - construct a list of all substrings of string
    - discard any substrings that are not alphabetical
    - identify and return the longest substring that occurs first
'''


# Given two words, how many letters do you have to remove from them to make them anagrams?
'''
given: two words
return: number of letters removed 
notes:
anagram - same characters, order does not matter
ds: set, 
algo: 
CREATE A DICTIONARY FOR EACH WORD CONTAINING LETTER KEYS AND COUNT VALUES
    set dict_word1 to create_dictionary
    set dict_word2 to create_dictionary
COMPARE THE DICTIONARIES FOR THE SAME LETTERS AND COUNT VALUES
    set differences to 0
    for each letter in dict_word1
        if letter is not in dict_word2
            add the count value to differences
        if letter is in dict_word2
            add the absolute value difference of the letter counts to differences
    for each letter in dict_word2
        if letter is not in dict_word1
            add the count value to differences
RETURN THE DIFFERENCES
    return differences


CREATE A DICTIONARY
    set dict_word to an empty dictiionary
    for each char in word
        if char not in dict_word
            add char to dict_word with count value 0
        add 1 the to count value at char
    return dict_word
'''

def anagram_difference(word1, word2):
    dict_word1 = create_dict(word1)
    dict_word2 = create_dict(word2)

    differences = 0
    for letter in dict_word1:
        if letter not in dict_word2:
            differences += dict_word1[letter]
        elif letter in dict_word2:
            differences += abs(dict_word1[letter] - dict_word2[letter])
    for letter in dict_word2:
        if letter not in dict_word1:
            differences += dict_word2[letter]
    return differences

def create_dict(word):
    dict_word = {}
    for char in word:
        if char not in dict_word:
            dict_word[char] = 0
        dict_word[char] += 1
    return dict_word

print(anagram_difference('', '') == 0)
print(anagram_difference('a', '') == 1)
print(anagram_difference('', 'a') == 1)
print(anagram_difference('ab', 'a') == 1)
print(anagram_difference('ab', 'ba') == 0 )
print(anagram_difference('ab', 'cd') == 4)
print(anagram_difference('aab', 'a') == 2 )
print(anagram_difference('a', 'aab') == 2 )
print(anagram_difference('codewars', 'hackerrank') == 10 )
print(anagram_difference("oudvfdjvpnzuoratzfawyjvgtuymwzccpppeluaekdlvfkhclwau", "trvhyfkdbdqbxmwpbvffiodwkhwjdjlynauunhxxafscwttqkkqw") == 42)
print(anagram_difference("fcvgqognzlzxhmtjoahpajlplfqtatuhckxpskhxiruzjirvpimrrqluhhfkkjnjeuvxzmxo", "qcfhjjhkghnmanwcthnhqsuigwzashweevbegwsbetjuyfoarckmofrfcepkcafznykmrynt") == 50)



'''
reword it helps
consistently
given: array of numbers 
return: all pairs of numbers wher
rules are the explicit rules that you can analyze from the test cases
clarification issues

algorithm and code should be last

Low Level
    Set sorted_array to the input array sorted from lowest to greatest numbers
    Set possible_pairs to an empty array
    For each number in sorted_array and stopping at the second to last number
        Set number as current_number
        For each number in sorted_array starting from current_number's index + 1
            Set number as next_number
            Append the current_number and next_number as a subarray to possible_pairs
    Set result to an empty array
    For each pair in possible_pairs
        If the pair is difference of 2
            append to result
    Return possible_pairs

same level of difficulty

'''


# Question 1:
# Write a function that takes a string as an argument. 
# The function should return the third character from the string that
# is not a vowel. If no such character exists, the function should return None.
'''
Checking each character, return the 3rd non-vowel otherwise return None
given: string
return: string as a 3rd non-vowel otherwise None

Notes:
non-vowel - number, letter, not spaces
No 3rd non-vowel return None

ds: string

algo:
- check for 3 non-vowel characters
- save the 3rd non-vowel character
- return the 3rd non-vowel character otherwise None

Set result to an empty string
Set counter to 0
For each character in string
    if the character is non-vowel and counter is less than 3
        add 1 to counter
    elif counter is equal to 3
        append the previous character to result
        break from the loop
if result is not an empty string
    return result
return None
'''

VOWELS = 'aeiou'

def third_non_vowel(s):
    result = ''
    counter = 0
    for i, char in enumerate(s):
        if char.lower() not in VOWELS and counter < 3:
            counter += 1
        elif counter == 3:
            result += s[i - 1]
            break
    if result != '':
        return result
    return None

# print(third_non_vowel("Hello World") == "l")
# print(third_non_vowel("Programming is fun!") == "g")
# #                     '0123'
# print(third_non_vowel("Launch School") == "c")
#                     '0123'
print(third_non_vowel("AEIOUbcd")) # == "d")
#                     'bcd'
# print(third_non_vowel("1a2b3c4d5e") == "b")
# print(third_non_vowel("") == None)
# print(third_non_vowel("aeiou") == None)


'''
problem: 9:15 minutes
DAC: 36 minutes
Return an index where the sum of values at the indices less than index equals to
the sum of values at indices greater than index

given: list of integers
return: index
notes:
assume list is more than 2 values
if there is no index that would make this work return -1
if there are multiple answers, return the smallest valued index
sum of numbers to the left of index 0 is 0 and right of the last index is 0

ds: list of results since we would return the index with the lowest value
algo:
CREATE AN EMPTY LIST FOR RESULTS
ITERATE THROUGH EACH INDEX AND FIND WHERE THE SUM OF VALUES ARE EQUAL
RETURN INDEX RESULT WITH LOWEST VALUE OTHERWISE RETURN -1

    Set result_dict to an empty dictionary
    For each index in list of integers
        If index is equal to 0
            Append the index and value if the sum of numbers to the right of
            index 0 is equal to 0
        If index is equal to last index
            Append the index and value if the sum of numbers to the left of
            the last index is equal to 0
        else
            Append the index and value if the sum of numbers to the left of
            the current index are equal to the sum of the numbers to the right
            of the current index
    If result_dict is not empty
        Set result to first index in result_dict
        Set lowest_value to first in result_dict
        For each index and value in result
            if value is less than lowest_value
                Set result to current index
    Return result if result else -1
'''
def equal_sum_index(integers):
    result_dict = {}
    for idx in range(len(integers)):
        if idx == 0 and sum(integers[1:]) == 0:
            result_dict[0] = 0
        elif idx == len(integers) - 1 and sum(integers[:-1]) == 0:
            result_dict[len(integers) - 1] = 0
        elif sum(integers[idx + 1:]) == sum(integers[:idx]):
            result_dict[idx] = integers[idx]
    if result_dict:
        result = list(result_dict.keys())[0]
        lowest_value = list(result_dict.values())[0]
        for idx, value in result_dict.items():
            if value < lowest_value:
                result = idx
    return result if result_dict else -1


'''
Problem: 7 minutes
DAC: 11 minutes and 18 seconds
Find the lowest sum of 5 consecutive number from a given list of integers
given: list of integers
return: lowest sum of 5 consecutive numbers or None if list has less than 5 elements
Notes:
Return None if length of list is less than 5
DS: list of sublist of sums
Algo:
CREATE A SUBLISTS FROM LIST THAT CONTAIN 5 CONSECUTIVE NUMBERS
CREATEA A LIST THAT CONTAIN THE SUMS OF EACH 5 CONSECUTIVE NUMBERS
RETURN THE LOWEST SUM FROM THE LIST
    If the length of integers is less than 5 return None
    Set sublist to an empty list
    For each number in integers
        Append the first 5 integers starting from number to sublist
    Set 5_consecutives to an empty list
    For all numbers in sublist
        if the length of numbers is equal to 5
            append them to 5_consecutives
    Set sum_of_5_consecutives to an empty list
    For all numbers in 5_consecutives
        sum the numbers and append to sum_of_5_consecutives
    Return the lowest sum from sum_of_5_consecutives
'''
def minimum_sum(integers):
    if len(integers) < 5:
        return None
    sublist = []
    for idx, number in enumerate(integers):
        sublist.append(integers[idx:idx + 5])

    sum_of_5_consecutives = [sum(numbers) for numbers in sublist
                                          if len(numbers) == 5]
    return min(sum_of_5_consecutives)


'''
Problem: 6 minutes
DAC: 12 minutes 56 seconds
Return true if string is a pangram otherwise return false
notes:
Pangrams are sentences that have all letters of the alphabet at least once
Not case sensitive
we will have global variable ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
DS: set, list
Algo:
ADD ALL LETTERS TO A NEW SET
COMPARE IF ALL LETTERS ARE EQUAL TO ALPHABET
    letters to an empty set
    For each character in sentence
        if character is a letter
            add lowercase character to letters
    If all letters are equal to ALPHABET return True else False
'''
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def is_pangram(sentence):
    letters = set()
    for character in sentence:
        if character.isalpha():
            letters.add(character.lower())
    return ''.join(list(sorted(letters))) == ALPHABET


'''
Time to complete: 13 minutes 51 seconds
Given a list of numbers, for each number count how many times it is smaller
and return it in a list
Notes:
Count unique values
Algo:
ITERATE THROUGH THE LIST AND COUNT EACH NUMBER LESS THAN CURRENT NUMBER
SAVE THE COUNT TO A LIST FOR EACH NUMBER
RETURN THE COUNT
    Set result to an empty list
    Set numbers_copy to a copy of list of numbers of unique values
    For each number in list of numbers
        Set count to zero
        For each number_copy in numbers_copy
            Else if number is greater than numbers_copy
                Add one to count
        Append count to result
    Return result
'''
def smaller_numbers_than_current(numbers):
    result = []
    numbers_copy = set(numbers)
    for number in numbers:
        count = 0
        for number_copy in numbers_copy:
            if number > number_copy:
                count += 1
        result.append(count)

    return result

print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)

'''
Time taken: 16 minutes 54 seconds
Given a string return a copy where every second character in every third word
is converted to uppercase
Notes:
Other characters are unchanged
DS: string, list
Algo
CREATE A LIST OF WORDS
EVERY THIRD WORD CHANGE TO WEIRD CASE
CREATE A NEW STRING FROM LIST
RETURN LIST

    Set words to a list of words using string
    For every 3rd word in words (range)
        Change to weird case
    Set new_string to a joined string from words using spaces
    Return new_string

    Change to weird case
    Set letters to a list from word
    For every 2nd character in letters (range)
        convert to uppercase
    Return a joined list as a string with no spaces
'''
def to_weird_case(string):
    words = string.split()
    for idx in range(2, len(words), 3):
        words[idx] = change_word(words[idx])
    return ' '.join(words)

def change_word(word):
    letters = list(word)
    for idy in range(1, len(letters), 2):
        letters[idy] = letters[idy].upper()
    return ''.join(letters)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)


'''
Total: 24 minutes 19 seconds

Given list of integers return a tuple of two numbers that are closest in equality
Notes:
Return the pair that occurs first
DS: tuple, list, dictionary (tuple: absolute difference between the tuples)
Algo:
CREATE A LIST OF TUPLE PAIRS
CREATE A LIST OF ABSOLUTE DIFFERENCES FROM THE TUPLE PAIRS
RETURN THE TUPLE PAIR AT THE INDEX OF THE FIRST CLOSEST VALUES IN ABSOLUTE DIFFERENCES

    Set tuple_pairs to a an empty list
    For each index and number in integers:
        For each index and sub_number in integers:
            if sub_number is not equal to the same index as number
                Add number and sub_number as a tuple to tuple_pairs
    Set abs_differences to an empty list
    For each pair in tuple_pairs
        Get the absolute difference and add to abs_differences
    Set minimum_value to the minimum value in abs_differences
    For each index and difference in abs_differences
        if difference is equal to minimum_value
            Set target_index to index
            Break from loop
    Return tuple_pairs at target_index
'''
def closest_numbers(integers):
    tuple_pairs = []
    for idx, number in enumerate(integers):
        for idy, sub_number in enumerate(integers):
            if idx != idy:
                tuple_pairs.append((number, sub_number))
    abs_differences = []
    for pair in tuple_pairs:
        abs_differences.append(abs(pair[0] - pair[1]))
    minimum_value = min(abs_differences)
    for idz, difference in enumerate(abs_differences):
        if difference == minimum_value:
            target_index = idz
            break
    return tuple_pairs[target_index]
print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))



'''
Alex: helper function for is bouncy, convert each integer to a string, 
iterate through each string, compare each digit with the next and keep track of whether 
the digits go up and down (could use flags to do this)

    Set strings to a new list of integers as strings
    Set count to 0
    For each string in strings with length greater than 3
        if length of string is greater than 3 and is_bouncy
            add one to count
    return count

is_bouncy
    Set up to false
    Set down to false
    For each digit in string starting from 2nd digit
        If current digit is greater than previous digit:
            Set up to true
        If current digit is less than previous digit
            set down to true
    if up and down
        return True
    else
        Return False

'''


'''
Given a string return the most occurring character that appears 
first in the string. Not case sensitive
DS: dictionary (character: occurence), list, sort
Algo:
CREATE AN EMPTY DICTIONARY TO HOLD CHARACTERS AND OCCURRENCES
FOR EACH CHARACTER IN STRING ADD THE CHARACTER AND OCCURRENCES TO A DICTIONARY
CREATE A LIST OF CHARACTERS WITH THE MOST OCCURRENCES
FOR EACH CHARACTER IN STRING CHECK IF IT IS IN MOST OCCURENCES LIST
RETURN THE CHARACTER

    Set characters to an empty dictionary
    For each character in string
        Set character equal to casefold
        If character is not in characters
            Add character.lower() to characters with value 1
        Else
            Add 1 to the value at character.lower() in characters
    Set max to the max value of characters
    Set most_occuring_char to an empty list
    For each value, character in characters
        If value is equal to max
            Append character to most_occuring_char
    For each character in string
        if character in most_occuring_char
            return character
'''
def most_common_char(string):
    characters = {}
    for char in string:
        char = char.casefold()
        if char not in characters:
            characters[char] = 1
        else:
            characters[char] += 1
    max_value = max(characters.values())
    most_occuring_char = [char for char, value in characters.items()
                               if value == max_value]
    for char in string:
        char = char.casefold()
        if char in most_occuring_char:
            return char

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

