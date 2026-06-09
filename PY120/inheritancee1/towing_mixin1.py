class TowingMixin:
    def tow(self):
        print('I can tow a trailer!')

class Truck(TowingMixin):
    pass

class Car:
    pass

truck1 = Truck()
truck1.tow()          # I can tow a trailer!

car1 = Car()
try:
    car1.tow()
except AttributeError as exception:
    print(exception)
# 'Car' object has not attribute 'tow'