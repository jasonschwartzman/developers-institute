class Fish:


    def __init__(self, fins, scales, weight, length, color):
        self.fins = fins
        self.scales = scales
        self.weight = weight
        self.length = length
        self.color = color

    def print_out(self):
        print("Fins", self.fins)
        print("Scales", self.scales)
        print("Color", self.color)

class Kosher_Fish(Fish):

    def __init__(self, fins, scales, weight, length, color):
        self.fins = True
        self.scales = True
        self.weight = weight
        self.length = length
        self.color = color


shark = Fish(True, False, 1000, 80, "Grey")
shark.print_out()

salmon = Kosher_Fish(True, False, 5, 10, "Pink")
salmon.print_out()