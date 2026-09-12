# list comprehension
# readlines
# lines
"""
You need to process a log file named app.log that contains entries from different services. Your task is to write a function find_error_logs that reads this file and returns a list of all log entries originating from the "DATABASE" service.

Your function should also handle the case where the file does not exist by returning an empty list. Assume the log file has the following format, with each part separated by a pipe (|): TIMESTAMP|SERVICE|MESSAGE

Example app.log content:

2023-10-27T10:00:00|AUTH_SERVICE|User login successful
2023-10-27T10:01:15|DATABASE|Query executed successfully
2023-10-27T10:02:30|API_GATEWAY|Request routed
2023-10-27T10:03:00|DATABASE|Connection to replica failed

Requirements:

1. Define a function find_error_logs(file_path).
2. Use a with statement to ensure the file is handled correctly.
3. Use a try...except FileNotFoundError block to handle a missing file.
4. The function should return a list of strings, where each string is a full log line from the "DATABASE" service.
"""


# 'aaabbaaa' strip()

# def find_error_logs(file_path):
#     result = []

#     try:
#         with open(file_path) as file:
#             for log in file:
#                 log = log.strip()
#                 # print(log.split('|'))
#                 if 'DATABASE' == log.split('|')[1]:
#                     result.append(log.strip())
        
#         return result
#     except FileNotFoundError:
#         return []
        
        




# # *** Example usage ***

# with open('app.log', 'w') as file:
#     file.writelines([
#         '2023-10-27T10:00:00|AUTH_SERVICE|User login successful\n',
#         '2023-10-27T10:01:15|DATABASE|Query executed successfully\n',
#         '2023-10-27T10:02:30|API_GATEWAY|Request routed\n',
#         '2023-10-27T10:03:00|DATABASE|Connection to replica failed\n',
#         '2023-10-27T10:03:00|RANDOM|DATABASE\n',
#     ])

# database_logs = find_error_logs('app.log')
# print(database_logs)

# # Example with a non-existent file
# missing_logs = find_error_logs('non_existent.log')
# print(missing_logs)

# # *** Expected output ***
# # [
# #   '2023-10-27T10:01:15|DATABASE|Query executed successfully',
# #   '2023-10-27T10:03:00|DATABASE|Connection to replica failed'
# # ]
# # []

'''
Side Effects and Pure Functions
'''
# What actions performed by a function make it have side efffects
# What does it mean to be a non-local variable or program?
# What does it mean when an error isn't caught?
# What does it mean when a function as a side effect through other function?
# What should a function do? Define them precisely.
# What is a pure function? Why are they useful? Give an example.
# Define the lifetime of a function

'''
Decorators
'''
# Why are decorators useful? Name the specific situation(s)

