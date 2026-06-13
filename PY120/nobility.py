class WalkMixin:
    def walk(self):
        return f"{self.full_name()} {self.gait()} forward"

class Animal(WalkMixin):
    def __init__(self, name):
        self.name = name
    
    def full_name(self):
        return self.name


class Person(Animal):
    def gait(self):
        return "strolls"

class Cat(Animal):
    def gait(self):
        return "saunters"

class Cheetah(Cat):
    def gait(self):
        return "runs"

class Noble(Person):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title

    def full_name(self):
        return f"{self.title} {self.name}"

    def gait(self):
        return "struts"


byron = Noble("Byron", "Lord")
print(byron.walk())         # "Lord Byron struts forward"
print(byron.name)           # "Byron"
print(byron.title)          # "Lord"

# What is the tradeoff of using __str__ or a `name` or `full_name` method?
# __str__ is good for general display method
# `full_name` is good for an explicitly defined method