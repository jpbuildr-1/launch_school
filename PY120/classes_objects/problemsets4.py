class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @name.setter
    def name(self, name):
        parts = name.split()
        self.first_name = parts[0]
        if len(parts) > 1:
            self.last_name = parts[1]
        else:
            self.last_name = ''

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, name):
        self._first_name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, name):
        self._last_name = name

bob = Person('Robert Smith')
rob = Person('Robert Smith')
# get name from bob and rob and see if they are the same
print(bob.name == rob.name)

'''
Line 35 creates a new Person instance that assigns 'Robert' to the `_first_name` instance variable and 'Smith' to the `_last_name instance variable
via the setter methods `first_name` and `last_name`, respectively. The `name` setter method splits the string 'Robert Smith' into a list of two
elements and assigns it to parts. The first element, 'Robert' is assigned to the `_first_name` instance variable via the `first_name` 
setter method. The second element, 'Smith' is assigned to the `_last_name` instance variable via the `last_name` setter method.

Line 36 creates a new Person instance that assigns 'Robert' to the `_first_name` instance variable and 'Smith' to the `_last_name instance variable
via the setter methods `first_name` and `last_name`, respectively. The `name` setter method splits the string 'Robert Smith' into a list of two
elements and assigns it to parts. The first element, 'Robert' is assigned to the `_first_name` instance variable via the `first_name` 
setter method. The second element, 'Smith' is assigned to the `_last_name` instance variable via the `last_name` setter method.

Line 38 is where `name` getter method return the values of bob and rob, checks its equivalency which is True, and print invocation outputs True.
So `name` getter method accesses the `first_name` and `last_name` getter methods which access the instance variables `_first_name` and
`_last_name` which are assigned 'Robert' and 'Smith', respectively. The values of the instance variables are then returned to the f-string 
inside of the `name` getter method and striped of any trailing and leading spaces. It does this twice for `bob.name` and `rob.name`. The values
return are both 'Robert Smith'. And then the `==` operator checks if the values are equal to each other which they are so it return `True`.
Finally, the print invocation outputs `True`.
'''