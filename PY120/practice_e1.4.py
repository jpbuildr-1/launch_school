class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

small_car = Car()
small_car.go_fast()
# I am a super fast Car!

'''
The Car instance assigned to `small_car` invoked the `go_fast` method which is inherited
from the `SpeedMixin` class and it is automatically assigned to `self`. The Car instance
is then referred to inside of the brackets in the f-string `self.__class__.__name__`. 
The full expression `self.__class__.__name__` returns the class name as a string which is 'Car'

To be precise `self.__class__.__name__` evaluates like this
`self`                      # The small_car object
`self.__class__`            # <class 'Car'>
`self.__class__.__name__`   # the string 'Car'

'''