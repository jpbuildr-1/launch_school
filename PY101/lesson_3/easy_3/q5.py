# The following function unnecessarily uses two `return` statements
# to return boolean values. Can you rewrite this function so it
# only has one `return` statement and does not explicitly use
# either `True` or `False`

def is_color_valid1(color):
    return color == "blue" or color == "green"

print(is_color_valid("green"))
print(is_color_valid("red"))

def is_color_valid2(color):
    return color in ["blue", "green"]

print(is_color_valid("green"))
print(is_color_valid("red"))