def calculate_average(*args):
    return sum(args) / len(args) if args else None

print(calculate_average(1, 2, 3, 4, 5))      # 3.0
print(calculate_average())                   # None