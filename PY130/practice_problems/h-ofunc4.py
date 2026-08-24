'''
Use the reduce function shown in the answer to the previous question to 
compute the sum of the squares in a list of numbers.
'''
def reduce(callback, iterable, initial_value):
    accum = initial_value

    for item in iterable:
        accum = callback(item, accum)
    
    return accum

numbers = [1, 2, 3, 4, 5]
print(reduce(lambda number, accum: number**2 + accum, numbers, 0)) # 55
