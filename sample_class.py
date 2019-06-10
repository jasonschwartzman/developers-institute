class Animal:

	weight =  0.0
	height = 0.0
	atype = 'unknown'
	age = 0
	legs = 4

	def __init__(self, name):
		self.name = name

	def print_out_details(self):
		print("Name:", self.name)
		print("Weight:", self.weight)
		print("Height:", self.height)
		print("Type:", self.atype)
		print("Age:", self.age)
		print("Legs:", self.legs)

class Marsupial(Animal):
	legs = 2

	def print_out_details(self):
		print("You are a marsupial")

dog = Animal('dog')
elephant = Animal('elephant')
cat = Animal('cat')
cat.print_out_details()
dog.print_out_details()
elephant.print_out_details()

kangaroo = Marsupial('kangaroo')
kangaroo.print_out_details()
