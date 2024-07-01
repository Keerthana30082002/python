class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type):
        super().__init__(make, model, year)
        self.type = type

    def display_info(self):
        super().display_info()
        print(f"Type: {self.type}")


# Creating instances and displaying information
car = Car("Toyota", "Corolla", 2022, 4)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2020, "Cruiser")

car.display_info()
print()
motorcycle.display_info()
