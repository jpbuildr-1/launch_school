"""
Write Python code to replace all the : characters in the string below with +.

Try this problem using the methods you've learned about in this chapter. Once 
you have that working, use the Python documentation for the str type to find 
an alternative solution.


"""

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

print(info.replace(':', '+'))

# temp_list = info.split(':')
# info = '+'.join(temp_list)