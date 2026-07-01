'''
>   ==> (__gt__())
*   ==> (__mult__())
<=  ==> (__le__())
!=  ==> (__ne__())
+=  ==> (__iadd__())
**= ==> (__ipow__())
//  ==> (__floordiv__())
'''

class Math:
    def __init__(self, number):
        self.number = number

    def __gt__(self, other):
        return self.number > other.number

    def __mul__(self, other):
        return self.number * other.number

    def __le__(self, other):
        return self.number <= other.number

    def __ne__(self, other):
        return self.number != other.number

    def __iadd__(self, other):
        self.number += other.number
        return Math(self.number)

    def __pow__(self, other):
        return self.number ** other.number

    def __ipow__(self, other):
        self.number **= other.number
        return Math(self.number)

    def __floordiv__(self, other):
        return self.number // other.number

number1 = Math(1)
number2 = Math(2)
print(number1 > number2)        # False
print(number1 * number2)        # 2
print(number1 <= number2)       # True
print(number1 != number2)       # True
number1 += number2
print(number1.number)           # 3
number1 **= number2
print(number1.number)           # 9
print(number1 // number2)       # 4



