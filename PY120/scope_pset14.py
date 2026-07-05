class A:
    def __init__(self):
        self.var_a = "A class variable"

class B(A):
    def __init__(self):
        self.var_b = "B class variable"

b = B()
print(b.var_a)      # Raises AttributeError because B.__init__ overrides A.__init__ so A.__init__ never runs and var_a never initialized