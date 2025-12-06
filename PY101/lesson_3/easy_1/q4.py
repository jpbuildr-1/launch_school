# Using the following string, print a string that contains the
# same value, but using all lowercase letters except for the
# first character, which should be capitalized.

munsters_description = "the Munsters are CREEPY and Spooky."
# => 'The munsters are creepy and spooky.'
new_munsters_description = ''

for i in range(0, len(munsters_description)):
    if i == 0:
        new_munsters_description += munsters_description[i].upper()
    else:
        new_munsters_description += munsters_description[i].lower()

print(munsters_description.capitalize())
print(new_munsters_description)