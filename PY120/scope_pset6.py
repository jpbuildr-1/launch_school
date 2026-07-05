class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

bob = Student('Bob')
billy = Student('Billy')

print(bob.name, bob.__class__.school_name)
print(billy.name, billy.__class__.school_name)