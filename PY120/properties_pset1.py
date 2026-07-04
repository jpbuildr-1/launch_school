class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError(f'{name} is not a string.')

        self._name = name

jeff = Person('Jeff')
print(jeff.name)        # Jeff

jeff.name = 'Jeff Jeff'
print(jeff.name)        # Jeff Jeff

jeff.name = 1           # TypeeError: 1 is not a string
