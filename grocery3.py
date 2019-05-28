# This is my grocery list with a while
linein = input("What is the number of items in your list? ")
if linein.isdigit():
	print("You have entered a number!")
else:
	print("You entered in invalid number!")
bad_list = ['meat', 'chicken', 'beef', 'duck', 'turkey', 'bison']
new_item_list = []
try:
	number = int(linein)
	counter = 0
	while counter < number:
		message = "What is the "+str(counter+1)+" item in the list? "
		new_item = input(message)
		if new_item.lower() in bad_list:
			print('You are a vegetarian!!')
		else:
			new_item_list.append(new_item)
			counter = counter + 1
except:
	print('You didn\'t enter in any valid number!!!')
print(new_item_list)