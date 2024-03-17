class Car:
    """Model and describe the car"""

    def __init__(self, make, model, year, color):
        """Initiate the attributes that describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        """Show car describe """
        return f"{self.make} {self.model}, {self.year}, {self.color}"

    def __repr__(self):
        """Show car description in the list"""
        return f"({self.make} {self.model}, {self.year}, {self.color})"


class CarDealership:
    """Model a car dealership"""

    def __init__(self):
        """Create a list of car"""
        self.car_list = []
        self.reserve_car = []

    def add_car(self, *new_cars):
        """Add a new car"""
        for car in new_cars:
            self.car_list.append(car)

    def sell_car(self, car):
        """Sell a car"""
        if car in self.car_list:
            self.car_list.remove(car)
        else:
            print("There is no such car")

    def reserved_car(self, car):
        """Reserve a car, not available for sale"""
        if car in self.car_list:
            car_index = self.car_list.index(car)
            r_car = self.car_list.pop(car_index)
            self.reserve_car.append(r_car)
        else:
            print("There is no such car")

    def __str__(self):
        """Show car lists"""
        return f"Available cars: {self.car_list}\nReserved cars: {self.reserve_car}"

    def __repr__(self):
        """Show car lists"""
        return f"({self.car_list}, {self.reserve_car})"


car1 = Car("Subaru", "Outback", 2017, "blue")
car2 = Car("Subaru", "Outback", 2015, "black")
car3 = Car("Nissan", "Rogue", 2019, "blue")
car4 = Car("Jeep", "Cherokee", 2016, "red")
car5 = Car("Jeep", "Cherokee", 2017, "white")

car_dealership = CarDealership()
car_dealership.add_car(car1, car2, car3, car4, car5)
print(car_dealership)

print()
car_dealership.reserved_car(car2)
print(car_dealership)

print()
car_dealership.sell_car(car1)
car_dealership.sell_car(car5)
print(car_dealership)
