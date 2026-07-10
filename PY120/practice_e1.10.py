class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count

# `_cats_count` is a class variable it keeps track of how many Cat instances have been created.
# That is each time a `Cat` instance is initialized, 1 is added to the `_cats_count`.

for i in range(2):
    Cat('tabby')

print(Cat.cats_count())     # 2