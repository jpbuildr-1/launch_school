class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def get_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def get_wheels(self):
        return 2

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        return 6


car = Car('Toyota', 'Camry')
truck = Truck('Toyota', 'Tacoma', 21)
motorcycle = Motorcycle('Honda', 'Fury')

print(car.info())                 # Toyota Camry
print(car.get_wheels())           # 4
print(truck.info())               # Toyota Tacoma
print(truck.get_wheels())         # 6
print(motorcycle.info())          # Honda Fury
print(motorcycle.get_wheels())    # 2
