class Vehicle:
    
    count = 0
    
    def __init__(self):
        Vehicle.count += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.count

class SignalMixin:
    
    def signal_left(self):   
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')

class Car(SignalMixin, Vehicle):
    
    def __init__(self):
        super().__init__()


class Truck(SignalMixin, Vehicle):
    
    def __init__(self):
        super().__init__()

class Boat(Vehicle):
    
    def __init__(self):
        super().__init__()



classes = [Car, Truck, Boat, Vehicle]
for cl in classes:
    print(cl.mro())
