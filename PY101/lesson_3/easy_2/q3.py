# Programmatically determine whether `42` lies between `10` and `100`, inclusive. Do the
# same for the values `100` and `101`.

def check_number(number):
    for i in range(10, 101):
        if number == i:
            return f"{number} lies between 10 and 100, inclusive"
    
    return f"{number} does not lie between 10 and 100"

print(check_number(42))
print(check_number(100))
print(check_number(101))