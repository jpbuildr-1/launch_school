number = float(input("Please enter a positive number: "))

if number < 0:
    raise ValueError("Number is negative.")
print(f"Here is your number: {number}")