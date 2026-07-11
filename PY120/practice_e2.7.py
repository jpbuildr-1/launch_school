class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()                           # Instantiates a Television instance and assigns to the local variable tv
print(tv.manufacturer())                    # Output 'Amazon'
print(tv.model())                           # Output 'Omni Fire'

print(Television.manufacturer())            # Output 'Amazon'
print(Television.model())                   # Raise a TypeError because model method is not a class method and is missing a Television instance