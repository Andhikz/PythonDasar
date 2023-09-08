class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
      print("Sail!")

class PLane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
      print("Fly!")

car1 = Car("Ford", "Mustabg")
boat1 = Boat("Ibiza", "Tourning 20")
planel1 = PLane("Boeing", "747")

for x in (car1, boat1, planel1):
    x.move()



 