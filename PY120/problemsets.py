class Person:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert

'''
line 15 the local variable bob is assigned a Person object with the instance variable name of 'bob'. What happens is the Person class
is invoked and a new instance in created using the `__init__` method which passes 'bob' and assigns it to an instance variable.

line 16 outputs the name instance variable 'bob' via calling the behavior that gets the name instance variable 'bob' from the Person object that is
assigned to the local variable bob.

line 17 sets the name instance variable assigned to the local variable bob from 'bob' to 'Robert'

line 18 out puts the name instance variable 'Robert' via calling the behavior that gets the name instance variable 'Robert' from the Person
object that is assigned to the local variable bob.
'''