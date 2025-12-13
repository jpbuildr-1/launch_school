# Write two distinct ways of reversing the list without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# numbers_copy = numbers.copy()
# numbers_copy.reverse()
# print(numbers_copy)
# print(sorted(numbers, reverse=True))
# print(numbers)

reverse_numbers = numbers[-1:-6:-1]
reverse_numbers = list(reversed(numbers))
