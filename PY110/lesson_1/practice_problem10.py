# what does the following code print and why?
dictionary = {'a': 'ant', 'b': 'bear'}
print(dictionary.popitem()) # ('b', 'bear')

# because it was the last item entered into dictionary and popitem()
# removes the last item from a dictionary and returns its value as a tuple