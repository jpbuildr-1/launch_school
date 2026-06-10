class SwimMixin:
    def swim(self):
        return 'swimming!'

class Pet:
    def speak(self):
        pass

class Mammal(Pet):
    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'

class Fish(SwimMixin, Pet):
    pass

class Dog(SwimMixin, Mammal):
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Cat(Mammal):
    def speak(self):
        return 'meow!'

print(Fish.mro()) # [<class '__main__.Fish'>, <class '__main__.SwimMixin'>, <class '__main__.Pet'>, <class 'object'>]