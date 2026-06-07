class Cat:

    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()

'''
On line 9, the `Cat` class instantiates a new object. Python automatically calls `__init__` which passes the new object as `self`
and 'Sophie' as the `name` argument. Inside the `__init__` method the instance variable `self.name` is assigned 'Sophie'. 
The object is then assigned to `kitty`.

On line 10, the instance method `greet` is invoked on the Cat object assigned to the `kitty` variable. Inside the method the print function
is invoked on an f-string that contains the instance variable `self.name` which outputs "Hello! My name is Sophie!"
'''