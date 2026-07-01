class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() != other.name.casefold()

cocoa = Cat('Cocoa')
cheddar = Cat('Cheddar')
cocoa2 = Cat('cocoa')

print(cocoa == cheddar)         # False
print(cocoa != cheddar)         # True
print(cocoa == cocoa2)          # True