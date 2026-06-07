class Cat:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()

'''
Line 12 instantiates a new Cat object where Python class the `__init__` method and passes the object and 'Sophie' to `self` and `name`. The
instance variable `_name` is assigned 'Sophie'. The new object is assigned to the variable `kitty`

Line 13 the instance method `greet` is invoked on the `Cat` object assigned to kitty. The instance method automatically passed the object
and inside the method there is a print invocation on an f-string that contain a `name` getter method. The getter method returns the value 
assigned to the instance variable `_name` which is 'Sophie'. The f-string returns the string "Hello! My name is Sophie!" and the print
invocation outputs the string.
'''
