# What is the output of this code, and why? What is the concept covered here?

str1 = "Hello, world!"
sub1 = str1[8:12]
print(sub1) # orld!
sub2 = str1[::-1]
print(sub2) # !lo olH
sub3 = str1[::2]
print(sub3) # Hl r!

# Output is above. The [:] demonstrates the concept of slicing through
# the string str1 and assigning the values to sub1, sub2, and sub3

