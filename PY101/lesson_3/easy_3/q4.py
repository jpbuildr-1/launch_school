# What would the following code output?
my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy() # my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5] my_list2 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2[0]['first'] = 42 # my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5] my_list2 = [{"first": 42, {"second": "value2"}, 3, 4, 5]
print(my_list1) # my_list1 = [{"first": 42}, {"second": "value2"}, 3, 4, 5]