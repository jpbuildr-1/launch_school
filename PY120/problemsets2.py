class Person:
    def __init__(self, first_name, last_name=''):
        self.first_name = first_name
        self.last_name = last_name

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

    @property
    def name(self):
        return f'{self._first_name} {self._last_name}'.strip()

    

'''
Modify the class definition from above to facilitate the following methods. 
Note that there is no name= setter method now.
'''

bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

'''
Line 33 the Person class initializes a new instance that passes the 1st argument 'Robert' which the `first_name` setter method uses
to assign to the instance variable `_first_name`. Additionally, the 2nd argument is a '' default value because nothing was passed
which the `last_name` setter method uses to assign to the `_last_name` instance variable.

Line 34 the code outputs Robert because the getter method `name` is invoked on bob which is assigned a Person instance that contains the
instance variables `_first_name` and `_last_name` that are assigned the values 'Robert' and '', repsectively. The name getter method
uses these instance variables to return an f-string that is stripped of any exterior spaces, 'Robert'. The return value 'Robert' is then
used as an argument for the print invocation to output Robert.

Line 35 the code outputs Robert because the getter method `first_name` that is invoked on bob, a Person instance with the instance variables
`_first_name` and `_last_name`. The getter method returns the instance variable `_first_name` which is assigned 'Robert'. 'Robert' is then
passed as argument to the print invocation to output 'Robert'

Line 36 the code outputs and empty string because the value return from the `last_name` getter method is an empty string. The getter method
is invoked on bob which is assigned a Person instance that contains the instance variable `_lastname` and assigned the value of ''. So
the getter method returns the value of the instance variable `_last_name` which is ''. The value '' is then passed to the repr method
which outputs an empty string '' and then that value is passed to the print invocation which outputs the empty string ''.

Line 37 the code invoked the `last_name` setter method on bob which updates the `_last_name` instance variable from '' to 'Smith'.

Line 38 the code invoked the `name` getter method on bob which return an f-string of the `_first_name` and `_last_name` instance
variables which are assigned 'Robert' and 'Smith', respectively. Specifically the value is 'Robert Smith', the strip method removes
all trailing spaces. The value is then passed to the print invocation to ouput 'Robert Smith'.
'''