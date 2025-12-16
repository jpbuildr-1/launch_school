# What is the output of the following code?
answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer) # 50

print(answer - 8) # 42 - 8 = 34

"""
The output of the code is 34. Although the global variable answer is passed through the mess_with_it function 
as an argument, the value 42 that is initially assigned to it did not change. Therefore, when print is invoked,
the expression answer - 8 would evaluate to 34 then the program would print 34.
"""