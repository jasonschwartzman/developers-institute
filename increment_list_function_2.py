# This is my grocery list with a while
def increment_list(how_many):
	my_new_item_list = []
	for counter in range(int(how_many)):
		number = (counter * 0.5) + 1.5 
		my_new_item_list.append(number)
	return my_new_item_list

#Mainline
number_of_numbers = input("What is the number of items in your list? ")
new_item_list = increment_list(number_of_numbers)
print(new_item_list)




