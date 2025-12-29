"""
Which variable is coerced? 

Is it implicit or explicit coercion?
"""

x = 3.5   # float
y = 5     # int
z = x + y # y is implicitly coerced to a float

"""
In the expression, `y` is implicitly coerced to a float so that Python can
add it to `x`. This is implicit coercion because Python does the conversion
automatically without us calling something like `float(y)`.
"""