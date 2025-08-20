# What will the following code do? Why?
int('3.1415')
# the code will emit an error due to
# int can only convert strings that
# are whole numbers. Since the string
# contains a decimcal point, Python
# would not consider the value a valid
# string of an integer.