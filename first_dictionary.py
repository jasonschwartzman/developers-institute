my_items = {'apple': 30, 'banana': 20.3, 'meat': 500.56}
quantity = input("how many do you want to buy?")
my_item_to_buy = input("What item would you like to buy?")
cost = my_items[my_items_to_buy] * int(quantity)
print("The cost is: ", cost )