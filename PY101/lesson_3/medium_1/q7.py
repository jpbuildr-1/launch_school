# One day, Spot was playing with the Munster family's home computer, and he wrote
# a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "femable"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

mess_with_demographics(munsters)

"""
The code would raise an exception, IndexError. When the function mess_with_demographics is
invoked the function passes the global variable munsters and assigns the dictionary value to 
a local variable demo_dict. The for loop goes through the dictionary and attempts to change
the value with key "age" and the Python interpreter then raises an exception as the key was
not assigned.
"""