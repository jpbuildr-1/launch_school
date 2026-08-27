def describe_pet(animal_type, *, name=""):
    name = f" {name} " if name else " "
    print(f"The pet{name}is a happy and lazy {animal_type}.")

describe_pet("dog", name="cheers") # The pet cheers is a happy and lazy dog.
describe_pet("dog", "cheers")      # TypeError: two positional arguments given