def set_foo():
    foo = 'bar'

set_foo()   # intializes a local variable foo to a string 'bar' which cannot be referenced to outside of the function and returns None
print(foo)  # foo is not defined outside of the function therefore an error will be shown