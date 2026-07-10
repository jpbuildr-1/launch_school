my_obj.foo()

# For the code above, Python uses the Method Resolution Order or MRO
# which can be found using the code below.

my_obj.__class__.mro()

# The above code returns a list of classes that Python checks through
# starting from the `my_obj`'s class to its superclasses and finally the
# `object` class. If `foo` cannot be found in any of the classes then
# Python raises an AttributeError.
