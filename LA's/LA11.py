class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def describePhone(self):
        return f"{self.brand} is a {self.model} type of phone object. "
class Android(Phone):
   def __init__(self, brand, model):
        self.brand = brand
        self.model = model
techno = Android("Techno", "Camon 12 Pro")
print(f"Output:\n{techno.describePhone()}")