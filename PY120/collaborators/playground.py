class Person:
    def __init__(self, name):
        self.name = name

class Pet:
    def jump(self):
        return 'How high?'

class Dog(Pet):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    pass

class Cat(Pet):
    pass

bob = Person('Robert')
kitty = Cat()
bud = Bulldog()
bob.pets = [kitty, bud]
print(bob.pets)      
# [<__main__.Cat object at 0x...>
# <__main__.Bulldog object at 0x...>]
for pet in bob.pets:
    print(pet.jump())
# How high?
# How high?