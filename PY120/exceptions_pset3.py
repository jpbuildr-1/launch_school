try:
    number1 =  float(input("Please provide a number: "))
    number2 = float(input("Please provide a second number: "))
    result = number1 / number2
except Exception as e:
    print(e)
else:
    print(f"The result is {result}.")
finally:
    print("End of the program.")