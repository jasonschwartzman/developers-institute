class Animal:

	weight =  0.0
	height = 0.0
	type = 'unknown'
	age = 0

	def __init__(self, name):
		self.name = name



dog = Animal('dog')
elephant = Animal('elephant')
print(elephant.name)

print(dog.weight)
print(dog.name)

cat = Animal('cat')
print(cat.weight)
print(cat.name)