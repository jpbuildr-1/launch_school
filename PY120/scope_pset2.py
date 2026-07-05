class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return self._breed

goldie = Dog('Golden Retriever')
poodl = Dog('Poodle')

print(f'Goldie breed: {goldie.get_breed()}')
print(f'Poodl breed: {poodl.get_breed()}')