class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

# The initializer in Fruit would not create an instance variable
# because the `my_name` variable does not include the prefix self

# The initializer in Pizza would create an instance variable
# because the `my_name` variable does include the prefix self