'''
Using the code from the previous exercise, add a parameter to __init__ that provides a name for the Cat object. 
Use an instance variable to print a greeting with the provided name. (You can remove the code that displays I'm a cat!.)
'''
class Cat:
    def __init__(self, name):
        self._name = name 
        print(f'Hello! My name is {self._name}!')
        
kitty = Cat('Sophie')

'''
On line 9 the Cat class instantiates a new object and passes an argument 'Sophie'. During initialization, the argument is assigned to `name`.
Inside of the `__init__`, an instance variable `self._name` is assigned the value assigned to `name`, 'Sophie'. Then there is an f-string that 
contains the instance variable `self._name` variable which evaluates to 'Hello! My name is Sophie!'. The string is then passed to the print 
invocation to output Hello! My Name is Sophie!
'''