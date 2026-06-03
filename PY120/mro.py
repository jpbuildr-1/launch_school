class LandDwellingMixin:
    pass

class LanguageMixin:
    pass

class BipedalismMixin:
    pass

class Creature:
    pass

class Mammal(Creature):
    def foo(self):
        pass

class Primate(LandDwellingMixin, Mammal):
    pass

class Human(BipedalismMixin,
            LanguageMixin,
            Primate):
    pass

paul = Human()
paul.foo()

'''
No it goes from left to right. The way the MRO works is it 
searches the methods until it reaches the method that was called.
For example in the case of the code below, `paul.foo()` returns
`None`, however, it reaches `foo()` by going from the class `Human`
to the class `Mammal` and searches for the method `foo()` going from
left to right. It searches through the `Human` class, then
`BipedalismMixin` class, then `LanguageMixin`, then `Primate`, then
`LandDwellingMixin`, then `Mammal` and it finds the `foo()` method.
'''