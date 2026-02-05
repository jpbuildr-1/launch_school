# Calculate the total age given the following dictionary:
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

# input : dictionary
# output : integer
# explicit
    # calculate total age
# implicit
    # return an integer
    # add all values from each key
# test cases
    # total_age(ages) # 6174
    # total_age({})   # 0
# data structure
    # integer
# algorithm
    # Intialize sum_age to 0
    # Iterate through each key value pair of ages (name, age)
        # Add age to sum_age
    # Return the final value of sum_age
# code
def total_age(people):
    sum_age = 0
    for name, age in people.items():
        sum_age += age
    return sum_age

print(total_age(ages)) # 6174

def total_age2(people):
    return sum(people.values())

print(total_age2(ages)) # 6174