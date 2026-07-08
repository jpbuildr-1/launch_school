class NegativeNumberError(Exception):
    def __init__(self, message):
        super().__init__(message)

number = float(input("Please enter a positive number: "))

if number < 0:
    raise NegativeNumberError("Number is negative.")
print(f"Here is your number: {number}")