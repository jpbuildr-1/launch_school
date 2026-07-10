import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

oracle = Oracle()
print(oracle.predict_the_future())

# The code will output a string that says either
# 'You will eat a nice lunch.'
# 'You will take a nap soon.'
# 'You will stay at work late.'
# 'You will adopt a cat.'

# We get this result the instance method predict_the_future is invoked on the
# Oracle instance assigned to the variable oracle. The instance method
# includes a return statement that contains an instance method choices
# which returns a list of choices that is passed to the random.choice function call
# that return a random string element from the returned list. The string
# is then included in the f-string and the string is returned. Finally,
# the print function call outputs the returned string.