# Pracice Problem 1
# Sort the following list of numbers first in ascending numeric order, 
# then in descending numeric order. Do not mutate the list.
lst = [10, 9, -6, 11, 7, -16, 50, 8]

# input: list
# output: list in descending and ascending order
# explicit: do not mutate the list
# implicit: output the results
# data structure: list
# algo:
# invoke print on the function call sort on the list
# invoke print on the function call sort on the list with additional argument reverse

def descending_sort(numbers):
    return sorted(numbers)[-1::-1]

# create a separate function to sort the list in descending order
# you sort the list then slice from -1 to beginning of list and step count -1
print(sorted(lst))
print(sorted(lst,reverse=True))
print(lst)

# expected result
[-16, -6, 7, 8, 9, 10, 11, 50]          # Ascending sort
[50, 11, 10, 9, 8, 7, -6, -16]          # Descending sort