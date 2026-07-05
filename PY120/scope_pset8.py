class Car:
    manufacturer = 'Honda'

    def __init__(self):
        self.manufacturer = 'Toyota'

    def show_manufacturer(self):
        print(f'{Car.manufacturer=}')
        print(f'{self.manufacturer=}')

car = Car()
car.show_manufacturer()     # Honda Toyota