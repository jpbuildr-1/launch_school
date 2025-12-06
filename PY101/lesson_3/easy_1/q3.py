# Starting with the string:

famous_words = "seven years ago..."

# Show two different ways to create a new string with "Four score and"
# prepended to the front of the string referenced by `famous_words`.

# Use concatenation
famous_words = "Four score and" + " " + famous_words
print(famous_words)

famous_words = "seven years ago..." # reset

# Use an f string
famous_words = f"Four score and {famous_words}"
print(famous_words)