numbers = [1, 2, 3, 4, 5]

def sixth_lbyl(numbers):
    if len(numbers) > 5:
        return numbers[5]
    
    return None

def sixth_afnp(numbers):
    try:
        return numbers[5]
    except IndexError:
        return None

print(sixth_lbyl(numbers))      # None
print(sixth_afnp(numbers))      # None