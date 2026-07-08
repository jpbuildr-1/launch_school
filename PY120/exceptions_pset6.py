def inverse(numbers):
    inversed = []

    for number in numbers:
        try:
            inversed.append(1 / float(number))
        except ZeroDivisionError:
            inversed.append(float('inf'))
    
    return inversed

print(inverse([1, 2, 0, -1, 3]))