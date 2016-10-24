
# Initialising variables that need to be in full scope
shoppinglist = []
command = ""

# We're going to loop until the user has entered all the items they want
while command != "done":
	command = raw_input("Please enter a shopping item, or 'done' if you are finished: ")
	if command != "done":
		shoppinglist.append(command)

# Each loop iteration is one shopping purchase. You tell the user what needs to be purchased, and let them purchase
while len(shoppinglist) > 0:
	print(" ")
	print("Your Shopping List")
	for id, item in enumerate(shoppinglist):
		print("{0} - {1}".format(id+1, item))

	# Effectively purchase an item
	command = raw_input("Enter an item code to remove it: ")
	del shoppinglist[int(command)-1]

print("You have completed your shopping list")

