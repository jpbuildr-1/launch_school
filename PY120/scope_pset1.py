class Dog:
    def __init__(self, breed):
        self.breed = breed

goldie = Dog('Golden Retriever')
poodl = Dog('Poodle')

print(f'Goldie breed: {goldie.breed}')
print(f'Poodl breed: {poodl.breed}')