a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# How would you obtain a set that contains all the unique values from both sets?
c = set()
c = a | b
print(c)
d = set(list(a) + list(b))
print(d)
e = a.union(b)
print(e)
