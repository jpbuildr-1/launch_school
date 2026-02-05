# Determine the minimum age from dictionary below:
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# input: dictionary
# output: integer
# explicit
    # determine the minimum age
# implicit
    # checking each value for the lowest number
# examples
    # print(minimum_age(ages)) # 10
    # print(minimum_age({}))   # errors
# data structure
    # integer
# algorithm
    # possibility 1
    # intialize `numbers` and assign it the values of ages
    # initialize `lowest_number` to the first element of `numbers`
    # iterate through `numbers`
        # if the current element of `numbers` is less than `lowest_number` set the current element to `lowest_number`
    # return the value of `lowest_number`

    # possibility 2
    # invoke built-in function `min` on values of `ages`
# code

def minimum_age(ages):
    numbers = []
    for age in ages.values():
        numbers.append(age)
    lowest_number = numbers[0]
    for num in numbers:
        if num < lowest_number:
            lowest_number = num
    return lowest_number

print(minimum_age(ages)) # 10

def minimum_age2(ages):
    return min(ages.values())

print(minimum_age2(ages)) # 10