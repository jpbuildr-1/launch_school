def multiply(a, b, /):
    return a * b

multiply_2s = multiply(2, 2)
print(multiply_2s)      # 4, cannot include keyword arguments like multiply(a=2, b=2)