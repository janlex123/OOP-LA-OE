class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describeToy(self):
        print(f"Output:\n{self.name} is a toy and its price is around ${self.price}")

# Child Class
class Plastic(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

# Creating an instance of Plastic
plastic = Plastic("Bat", 5)
plastic.describeToy()  