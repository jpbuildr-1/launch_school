"""

If we pass a compound data structure, like a list, into a function and we
mutate an object within that list, though not the list itself, would that
be considered pass-by-reference or pass-by-value behavior?
"""

"""
This would be considered pass-by-reference behavior. The function 
receives a reference to the original list, and the nested object 
list is the same object. When we mutate that nested object, the original
structure that was passed into the function is changed.
"""