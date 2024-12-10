"""
Create an empty class called Car, then create two instances.
Add the following attributes for each of the instances: Make, Model, Year.
Create print statements to display the attributes of each one of the instances.
"""

# another way of making a class and adding attributes later
# class Car:
#     pass
class Car:
    def __init__(self, make, model, year):
        self.Make = make
        self.Model = model
        self.Year = year

car = Car("Cadillac", "Escalade", 2024)
print(f"{car.Make} {car.Model} {car.Year}")