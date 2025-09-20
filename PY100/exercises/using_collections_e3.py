# Write Python code to create a new tuple from (1, 2, 3, 4, 5).
# The new tuple should be in reverse order from the original. It
# should also exclude the first and last members of the original.
# The result should be the tuple (4, 3, 2).

old_tuple = (1, 2, 3, 4, 5)

# temp_list = list(old_tuple)

# temp_list = temp_list[1: -1]
# temp_list.reverse()
# new_tuple = tuple(temp_list)

result = old_tuple[-2:0:-1]
print(result)

