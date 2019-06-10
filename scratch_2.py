class Car(object):
    wheels = 4
    fuel = "diesel"

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def print(self):
        print("Your car is: ", self.make, self.model, self.fuel, self.wheels, "wheels")

mustang = Car('Ford', 'Mustang')
print(type(mustang))
print(mustang.wheels)
print(mustang.make)
mustang.print()
mercedes = Car('Benz', 'Class A')
print(type(mercedes))
print(mercedes.wheels)
mercedes.wheels = 8
print(mercedes.window)
print(mercedes.make)
mercedes.print()
#kldsjflkjsdlkjsdlfkjsdlkfjsl/dkfjlskdjflskdjf l