def get_all_the_items(filename):
	# this function takes the filename and opens it as a text file and converts all lines to words and sends back a list 
	#Get all the items
	#1. Open file
	file = open(filename, "r")
	#2. Check the file is available
	if file.mode == 'r':
		#3. Read
		lines = file.read()
	else:
		lines = ''
	#4. Return back the items
	items = lines.split()
	file.close()
	return items

def lookup_price_of_item(item):
	# this function takes the item as a string and checks it in the dictionary
	prices = {'milk': 30, 'oranges': 20, 'quinoa': 5}
	item_cost = prices.get(item.lower())
	if item_cost is None:
		cost = 'Item NOT AVAILABLE'
	else:
		cost = item_cost
	return cost

def remove_all_not_vege(non_vege_filename, list_of_items_to_check):
	# this is the PROPER way to keep as COPY the original list and then you will not keep thinking you are changing the original
	sanitized_list = list_of_items_to_check
	# Remove all the bad products
	# Get the list of bad items
	#1. Open file
	file = open(non_vege_filename, "r")
	#2. Check the file is available
	if file.mode == 'r':
		#3. Read
		lines = file.read()
	else:
		lines = ''
	#4. Return back the bad items
	bad_items = lines.split()
	file.close()
	# Check the items
	#1. for loop through the list of items
	for item in list_of_items_to_check:
		if item in bad_items:
			sanitized_list.remove(item)
		else:
			# Here we are getting the price by checking its cost on the dictionary
			print("The cost for your item of ", item, "is", lookup_price_of_item(item))
	return sanitized_list

def save_the_list(filename, good_list):
	# Save all the items in from the list
	outputfile = open(filename, 'w+')
	for item in good_list:
		outputfile.write(item)
	outputfile.close()

#MainLINE
name_of_file='unchecked_grocery_list.txt'
list_of_items = get_all_the_items(name_of_file)
#remove anything that is not vegetarian based on a list
non_vege_file = 'non_vege_list.txt'
good_list = remove_all_not_vege(non_vege_file, list_of_items)
#save all the items in a file
name_of_output_file = 'checked_grocery_list.txt'
save_the_list(name_of_output_file, good_list)