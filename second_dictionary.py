my_items = {'apple': 30, 'banana': 20.3, 'meat': 500.56}
quantity = input("how many do you want to buy?")
my_item_to_buy = input("What item would you like to buy?")
#cost = my_items[my_item_to_buy] * int(quantity)
#exact same way:
itemcost =  my_items.get(my_item_to_buy.lower())
if itemcost is None:
	cost = 'Not Available Item'
else: 
	cost = itemcost * int(quantity)
#if my_item_to_buy.get(my_item_to_buy) == None:

print("The cost is: ", cost)

# This is the difference in the error: 
#Avners-Mac-mini:Python yaakovschwartzman$ python3 second_dictionary.py 
#how many do you want to buy?40
#What item would you like to buy?steak
#Traceback (most recent call last):
#  File "second_dictionary.py", line 4, in <module>
#    cost = my_items[my_item_to_buy] * int(quantity)
#KeyError: 'steak'
#Avners-Mac-mini:Python yaakovschwartzman$ python3 second_dictionary.py 
#how many do you want to buy?40
#What item would you like to buy?steak
#Traceback (most recent call last):
#  File "second_dictionary.py", line 6, in <module>
#    cost = my_items.get(my_item_to_buy) * int(quantity)
#TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'