"""
In Python, every object has a unique identity that can be accessed using
the id() function. This function returns the identity of an object, which
is guaranteed to be unique for the object's lifetime. For certain basic
immutable data types like short strings or integers, Python might reuse
the memory address for objects with the same value. This is known as
"interning".
"""

# Give the following code, predict the output:
a = 42
b = 42
c = a

my_set = {'member1', 'member2'}

print(id(a) == id(b) == id(c)) # False

# Identify the bug. The list should not be mutated.
lst = [1, 2, 3]

def remove_lst(lst):
    empty_lst = list(lst) # lst[:]

    for _ in range(len(lst)):
        empty_lst.pop()
    
    print("empty_lst: ", empty_lst)
    return lst

remove_lst(lst) # []
print("lst: ", lst) # [1, 2, 3]

"""
An object is a value in memory
"""
a = 1 # 1 is the object or value in meory