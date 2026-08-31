'''
Create a function named register that takes exactly three arguments:
username as positional-only, password as keyword-only, and age as either
a positional or keyword argument. It should return a dictionary that 
includes username, password, and age keys with the values passed to the function.
'''

def register(username, /, age, *, password):
    return {"username": username, "age": age, "password": password}

print(register('user1', age=12, password='pass123'))            # {'username': 'user1', 'age': 12, 'password': 'pass123'}