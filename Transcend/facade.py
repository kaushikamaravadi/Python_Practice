"""Facade Design Pattern"""


class Vehicle(object):

    def __init__(self, type, make, model, color, year, miles):
        self.type = type
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.miles = miles

    def print(self):
        print("vehicle type is",str(self.type))
        print("vehicle make is", str(self.make))
        print("vehicle model is", str(self.model))
        print("vehicle color is", str(self.color))
        print("vehicle year is", str(self.year))
        print("vehicle miles is", str(self.miles))


class Car(Vehicle):

    def prints(self):
        Vehicle.print(self)
        return Vehicle.print(self)


    def drive(self, speed):
        peek = "the car is at %d" %speed
        return peek




car = Car(30, 'SUV', 'BMW', 'X5', 'silver', 2003)
print(car.print())
print(car.drive(35))

