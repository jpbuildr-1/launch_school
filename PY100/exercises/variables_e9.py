# Repeat the previous question but, this time, 
# use augmented assignment to compute the final
# result one year at a time.

balance = 1000		# starting balance

balance *= 1.05 	# year 1
balance *= 1.05		# year 2
balance *= 1.05		# year 3
balance *= 1.05		# year 4
balance *= 1.05		# year 5

print(balance)		# prints balance at end of year 5