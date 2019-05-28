# This is my grocery list with a while
def increment_list():
	number_of_numbers = input("What is the number of items in your list? ")
	new_item_list = []
	for counter in range(int(number_of_numbers)):
		number = (counter * 0.5) + 1.5 
		new_item_list.append(number)
	print(new_item_list)

increment_list()




