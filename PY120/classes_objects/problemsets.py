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
On line 15 a Person object is initialized with 'bob' as an argument. During initialization, the instance setter property `name` is invoked
and sets the instance variable `_name` to 'bob' for this specific instance of the Person class.

line 16 outputs bob via the instance get property `name` which return the instance variable `_name`. The instance variable `_name`
of the Person instance assigned to bob is 'bob' so when the `name` property is invoked on bob it will return 'bob' which then is
passed to the print invocation that then outputs bob.

line 17 invokes the instance setter property `name` on bob which is assigned a Person instance that contain the instance variable 'bob'.
The instance property setter updates the `_name` instance variable from 'bob' to 'Robert'.

line 18 outputs Robert via the instance get property that is invoked on the Person instance assigned to bob. The `name` property returns
the instance variable `_name` assigned to bob which is 'Robert` and then the print invocation outputs Robert.
'''