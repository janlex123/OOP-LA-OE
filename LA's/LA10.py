class Vhicle:
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describeVehicle(self):
        return f"{self.brand} is a {self.model} and its fuel usage is {self.fuel_type} "
   
class Car(Vhicle):
    pass
car = Car("Ferrari", "GTC4Lusso", "Diesel")

class Motorcycle(Vhicle):
    pass

motorcycle = Motorcycle("Honda","Click125i","Shell")

print(f"Output:\n{car.describeVehicle()}\n{motorcycle.describeVehicle()}")