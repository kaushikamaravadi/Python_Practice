"""Calculating Volumes of Cube, Cuboid, Hemisphere and Cylinder"""

import math
class calculate():

    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def volume_cuboid(self):
        if self.length and self.height and self.breadth < 1:
            print("Invalid input. Make sure its positive")
        else:
            volume = self.length * self.height * self.breadth
            return str(round(volume,3))

    def lsa_cuboid(self):
        if self.length and self.height and self.breadth < 1:
            print("Invalid input. Make sure its positive")
        else:
            lsa = 2 * (self.length * self.height) + (self.breadth * self.height)
            return str(round(lsa,3))

    def surface_area_cuboid(self):
        if self.length and self.height and self.breadth < 1:
            print("Invalid input. Make sure its positive")
        else:
            sa = 2 * ((self.length * self.breadth) + (self.breadth * self.height) + (self.height * self.length))
            return str(round(sa,3))

    def volume_cube(self, edge):
        self.edge = edge
        if self.edge < 1:
            print("Invalid input. Make sure its positive")
        else:
            volume = self.edge ** 3
            return str(round(volume,3))

    def volume_cylinder(self, radius):
        self.radius = radius
        if self.radius and self.height < 1:
            print("Invalid input. Make sure its positive")
        else:
            volume = math.pi * (self.radius ** 2) * self.height
            return str(round(volume,3))

    def volume_hemisphere(self, radius):
        self.radius = radius
        if self.radius < 1:
            print("Invalid input. Make sure its positive")
        else:
            volume = (2 / 3) * math.pi * self.radius
            return str(round(volume,3))





n = float(input("enter length "))
n1 = float(input("enter Breadth "))
n2 = float(input("enter height"))

c = calculate(n, n1, n2)

switch = True

while switch == True:

    lime = """
    1. Volume of Cuboid
    2. Volume of Cube
    3. Volume of Cylinder
    4. Volume of Hemisphere
    5. LSA of a Cuboid
    6. Surface Area of a Cuboid
    7. To Exit
     """
    print(lime)

    user_input = int(input("What do you wanna do:"))
    if user_input == 1:
        print(c.volume_cuboid())
    elif user_input == 2:
        n2 = float(input("enter edge"))
        print(c.volume_cube(n2))
    elif user_input == 3:
        n3 = float(input("enter radius"))
        print(c.volume_cylinder(n3))
    elif user_input == 4:
        n3 = float(input("enter radius"))
        print(c.volume_hemisphere(n3))
    elif user_input == 5:
        print(c.lsa_cuboid())
    elif user_input == 6:
        print(c.surface_area_cuboid())
    elif user_input == 7:
        switch = False
    else:
        print("Please select correct choice")
