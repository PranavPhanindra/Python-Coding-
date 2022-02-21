# Create a list of all global variables using
# globals( ) function, To store the built-in
# global variables.
not_my_data = set(globals())

# Declare some global variables
foo5 = "hii"
foo6 = 7

# Declare a function.
def func():
	
	# Declare some local variables inside it.
	var2 = "Welcome to geeksforgeeks"
	var3 = {"1": "a", "2": "b"}
	var4 = 25
	var5 = [1, 2, 3, 4, 5]
	var6 = (58, 59)

	# Store all the local variables in a list,
	# using locals keyword.
	locals_stored = set(locals())
	
	# Iterate over the list and print the local
	# variables.
	print("Printing Local Variables")
	for name in locals_stored:
		val = eval(name)
		print(name, "is", type(val), "and is equal to ", val)

	# Store the global variables in a list using
	# globals keyword and subtract the previously
	# created list of built-in global variables from it.
	globals_stored = set(globals())-not_my_data
	
	# Print the global variables
	print("\nPrinting Global Variables")
	for name in globals_stored:
		
		# Excluding func and not_my_data as they are
		# also considered as a global variable
		if name != "not_my_data" and name != "func":
			val = eval(name)
			print(name, "is", type(val), "and is equal to ", val)


# Call the function.
func()

