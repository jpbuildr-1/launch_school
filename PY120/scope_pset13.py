class Tree:
    def __init__(self):
        self.type = "Generic"

class Pine(Tree):
    def __init__(self):
        super().__init__()
        self.type = "Pine Tree"

# When an instance of `Pine` is created the value of its type would be "Pine Tree" because the attribute was reassigned after the super function call