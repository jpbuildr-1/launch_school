'''
Create a generator function that generates the reciprocals of the numbers
from 1 to n, where n is an argument to the function. Use a for loop to print each value.
'''
def generate_reciprocals(n):
    for number in range(1, n + 1):
        yield 1 / number

for reciprocal in generate_reciprocals(7):
    print(reciprocal)
