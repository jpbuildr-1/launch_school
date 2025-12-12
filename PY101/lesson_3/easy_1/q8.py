# In the previous problem, our first answer added 'Dino' to the list like this:
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
# flintstones.append("Dino")
# How can we multtiple items to our (e.g., 'Dino' and 'Happy')? Replace the call
# to `append` with another method invocation.

# sequence.extend(iterable, /)
items = ['Dino', 'Hoppy']
flintstones.extend(items)
print(flintstones)