"""

Write a program named age.py that asks the user to enter their age, 
then calculates and reports the future age 10, 20, 30, and 40 years from now. 
Here's the output for someone who is 27 years old.

"""

age = int(input("How old are you? "))
print()
print(f'You are {age} years old.')

add_to_age = [10, 20, 30, 40]

for number in add_to_age:
	print(f'In {number} years, you will be {age + number} years old.')