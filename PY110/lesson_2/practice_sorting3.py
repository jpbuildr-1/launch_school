# Repeat problem 2 but, this time, sort the list as string values. Both the list passed 
# to the sorting function and the returned list should contain numbers, not strings.

def to_string(number):
    return str(number)

lst = [10, 9, -6, 11, 7, -16, 50, 8]
print(sorted(lst, key=to_string))
print(sorted(lst, key=to_string, reverse=True))

[-16, -6, 10, 11, 50, 7, 8, 9]          # Ascending sort
[9, 8, 7, 50, 11, 10, -6, -16]          # Descending sort