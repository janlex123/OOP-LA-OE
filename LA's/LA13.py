class Animal:
    def __init__(self, name, type):
        self.name = name
        self.type = type
       
class Fish(Animal):
    def __init__(self, name, type, can_swim):
        self.can_swim =  True
swordfish = Fish("Swordfish", "sword", True)
print(f"Output:\nQuestion: Can the Swordfish swim?\nAnswer: {swordfish.can_swim}")