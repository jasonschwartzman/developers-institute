import random
try:
	number = int(input("Pick a number between 1 and what:"))
except ValueError:
	print("You didn't enter in a proper number!!!! I am going to assume 100")
	number = 100
try:
	random_number = random.randint(1, number)
except ValueError:
	random_number = "unknown!!!!"
print("Your picked number is: ", random_number)