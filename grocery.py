# This is my grocery list
linein = input("What is the number of items in your list? ")
bad_list = ['pork', 'meat', 'chicken', 'beef', 'duck', 'turkey', 'bison']
new_item_list = []
try:
	number = int(linein)
	for counter in range(number):
		message = "What is the "+str(counter+1)+" item in the list? "
		new_item = input(message)
		if new_item.lower() in bad_list:
			print('You are a vegetarian!!')
		else:
			new_item_list.append(new_item)
except:
	print('You didn\'t enter in any valid number!!!')
print(new_item_list)
