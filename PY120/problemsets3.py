class Person:

    def __init__(self, name):
        self._name_split(name)

    def _name_split(self, name):
        name = name.split()
        self.first_name = name[0]
        
        if len(name) > 1:
            self.last_name = name[1]
        else:
            self.last_name = ''

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'.strip()

    @name.setter
    def name(self, name):
        self._name_split(name)

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


bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams

'''
From what changed in prior problem there has been additional lines from line 47 to 53. There is now a `name` setter method needed for the code
to start running starting from line 47 which I added to line 19-21. I also added a helper method that splits the name and easier to use
for repeated times within the class. 

So from line 47 the `name` setter method is invoked to reassign the instance variables `self._first_name` and `self._last_name` from
'Robert' and 'Smith' to 'Prince' and ''. The `name_split` method helps with reassigning them by spliting the string by space and 
creating a list that can be accessed and assigned to the instance variables by accessing them via the setter methods, `first_name` and `last_name`.

On line 48 the `first_name` getter method accesses the `_first_name` instance variable and returns the value 'Prince' which the print invocation
outputs

On line 49 the `last_name` getter method accesses the `_last_name` instance variable and return the value '' which the print invocation outputs

On line 51 the `name` setter method is invoked to reassign the instance variables, `_first_name` and _last_name` from 'Prince' and '' to 'John' and 'Adams'

On line 52 the `first_name` getter method access `_first_name` instance variable and returns 'John' which the print invocation outputs.

On line 53 the `last_name` getter method accesses the `_last_name` instance variable and returns 'Adams' which the print invocation outputs.
'''