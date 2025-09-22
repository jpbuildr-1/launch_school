# Explain why the code below prints different values on the print lines
                            |              	   
text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))  
# 8 because we are initially indexing the string from 21:35
# so the method rfind find 'f' starting from the empty space
# before for
print(text.rfind('f', 21, 35)) 
# 29 because we have the whole string available to find 'f'
# so the method rfind is starting from the beginning of the 
# string at I