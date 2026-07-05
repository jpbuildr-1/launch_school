class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)           # fixes the AttributeError that was caused by Sparrow.__init__ overriding Bird.__init__
        self.color = color

birdie = Sparrow("sparrow", "brown")
print(birdie.species)                   # sparrow