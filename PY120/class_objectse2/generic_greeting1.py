class Cat:
    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

Cat.generic_greeting()

# Further exploration
kitty = Cat()
type(kitty).generic_greeting() 
# The type call returns the `Cat` class. The class method `generic_greeting` is invoked on the Cat class which then outputs "Hello! I'm a cat!"