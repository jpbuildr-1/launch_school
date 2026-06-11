class Pet:
    def __init__(self, species, name):
        self.species = species
        self.name = name

    def info(self):
        return f"a {self.species} named {self.name}"


class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
    
    def add_pet(self, pet):
        self.pets.append(pet)
    
    def number_of_pets(self):
        return len(self.pets)

    def print_pets(self):
        for pet in self.pets:
            print(pet.info())


class Shelter:
    def __init__(self):
        self.owners = {}

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        if owner.name not in self.owners:
            self.owners[owner.name] = owner

    def print_adoptions(self):
        for name, owner in self.owners.items():
            print(f"{name} has adopted the following pets:")
            owner.print_pets()
            print()


cocoa = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, cheddar)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
