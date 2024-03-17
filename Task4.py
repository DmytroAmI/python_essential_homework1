class Car:
    """Model and describe the car"""

    def __init__(self, make, model, year, color, vin):
        """Initiate the attributes that describe the car"""
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.vin = vin

    def __str__(self):
        """Show car describe """
        return f"{self.make} {self.model}, {self.year}, {self.color}, vin - '{self.vin}'"

    def __repr__(self):
        return (f"Car(make={self.make}, "
                f"model={self.model}, "
                f"year={self.year}, "
                f"color={self.color}, "
                f"vin={self.vin})")


class Dealership:
    """Model a car dealership"""

    def __init__(self):
        """Create a car dictionary where vin is the key"""
        self.lots = {}

    def add(self, *cars):
        """Add a new cars"""
        if cars is None or len(cars) == 0:
            print("Please provide cars")
            return

        for car in cars:
            self.lots.update({car.vin: Lot(car)})

    def sell(self, vin):
        """Sell a car"""
        lot = self.lots.pop(vin)

        if lot is None:
            print("There is no such car")
            return

        if lot.reserved:
            print("Cannot sell reserved car")
            return

        print(f"Car {lot.car} is successfully sold")

    def reserve(self, vin):
        """Reserve a car"""
        lot = self.lots.get(vin)
        if lot is None:
            print("There is no such car")
            return

        lot.reserved = True
        print("Car successfully reserved")

    def __str__(self):
        """Show car lists"""
        result = "Available cars:"
        for car in self.lots.values():
            result += f"\n{car}"
        return result

    def __repr__(self):
        return f"Dealership(lots={self.lots})"


class Lot:
    """Model a lot with the ability to reserve a car"""
    def __init__(self, car):
        """Initiate the attributes"""
        self.car = car
        self.reserved = False

    def __str__(self):
        """Show car whether it is reserved"""
        return f"{self.car}, reserve: {self.reserved}"

    def __repr__(self):
        return f"Lot(car={self.car}, reserved={self.reserved})"


car1 = Car("Subaru", "Outback", 2017, "blue", "123")
car2 = Car("Subaru", "Outback", 2015, "black", "234")
car3 = Car("Nissan", "Rogue", 2019, "blue", "345")
car4 = Car("Jeep", "Cherokee", 2016, "red", "567")
car5 = Car("Jeep", "Cherokee", 2017, "white", "777")

car_dealership = Dealership()
car_dealership.add(car1, car2, car3, car4, car5)
print(car_dealership)

print()
car_dealership.reserve(car2.vin)
print(car_dealership)

print()
car_dealership.sell(car1.vin)
car_dealership.sell(car5.vin)
print(car_dealership)
