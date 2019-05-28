def get_all_the_items(filename):
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
	return sanitized_list

def save_the_list():
	# Save all the items in from the list

#mainline
#get my items to buy
name_of_file = 'unchecked_grocery_list.txt'
list_of_items = get_all_the_items(name_of_file)
#remove anything that is not vegetarian based on a list
good_list = remove_all_not_vege(non_vege_file, list_of_items)
#save all the items in a file
save_the_list()













