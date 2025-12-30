# What coercion is happening here? Is it implicit or explicit?
a = 1
b = 2
print(a + b)

# Neither, because print is displaying the result 3 as string.
# The result is not coerced in the sense that coersion is
# returning a new value and in this case there is no new
# value returned.