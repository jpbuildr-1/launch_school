class Cat:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return f'I am a {self.type}'

print(Cat('hairball'))