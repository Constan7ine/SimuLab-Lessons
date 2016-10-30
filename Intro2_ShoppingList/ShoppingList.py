
# Initialising variables that need to be in full scope
shoppinglist = []
command = ""

# Read in the file and prevent us from entering new things
f = open("shoppinglist.txt", 'r')
for line in f:
	shoppinglist.append(line.rstrip()) # Removes newline character, show why we need this
	command = "done"
f.close()

# We're going to loop until the user has entered all the items they want
while command != "done":
	command = input("Please enter a shopping item, or 'done' if you are finished: ")
	if command != "done":
		shoppinglist.append(command)

# Each loop iteration is one shopping purchase. You tell the user what needs to be purchased, and let them purchase
while len(shoppinglist) > 0:
	print(" ")
	print("Your Shopping List")

	# Print the current shopping list and save it out to a file
	f = open("shoppinglist.txt", 'w')
	for id, item in enumerate(shoppinglist):
		f.write("{}\n".format(item))
		print("{0} - {1}".format(id+1, item))
	f.close()

	# Effectively purchase an item
	command = input("Enter an item code to remove it (done to finish): ")
	if command == "done":
		quit()
	else:
		del shoppinglist[int(command)-1]

print("You have completed your shopping list")

