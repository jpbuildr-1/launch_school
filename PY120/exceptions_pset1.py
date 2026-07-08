number1 =  input("Please provide a number: ")
number2 = input("Please provide a second number: ")

try:
    print(int(number1) / int(number2))
except ZeroDivisionError:
    print("Second number is a zero. Cannot divide by zero.")
except ValueError:
    print("Value entered is not of base 10.")