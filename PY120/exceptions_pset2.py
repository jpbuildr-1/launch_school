try:
    number1 =  float(input("Please provide a number: "))
    number2 = float(input("Please provide a second number: "))
    result = number1 / number2
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter valid numbers!")
else:
    print(f"The result is {result}.")
finally:
    print("End of the program.")