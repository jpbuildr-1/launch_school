'What will the following code print?'

def make_greeting():
    greeting = "Hello"

    def greet_func(name, greet=None):
        if not greet:
            return f"{greeting} {name}!"

        return f"{greet} {name}!"

    return greet_func

greet_person = make_greeting()              # contains greet_func
print(greet_person("John", "Goodbye"))      # Goodbye John!
print(greet_person("Jane"))                 # Hello Jane!
