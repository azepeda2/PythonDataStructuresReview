# Homework: Classes
# Read carefully until the end before you start solving the exercises.

# Practice the Basics

# Basic Class

# - Create an empty class HouseForSale
# - Create two instances.
# - Add number_of_rooms and price as instance attributes.
# - Create print statements that show the attribute values for the instances.

class HouseForSale:
    pass

house1 = HouseForSale()
house2 = HouseForSale()

house1.number_of_rooms = 3
house1.price = 500000
house2.number_of_rooms = 4
house2.price = 750000

print(f"Price: {house1.price} rooms: {house1.number_of_rooms}")
print(f"Price: {house2.price} rooms: {house2.number_of_rooms}")


# ----------------------------------------------------------------------------------------------------------------------

# Instance Methods

# - Create a Computer class.
# - Create method:
#   - turn_on that prints Computer has Turned On
#   - turn_off that prints Computer has Turned Off
# - Create an instance of the Computer class then call each method.

class Computer:
    def turn_on(self):
        print("Computer has Turned On")

    def turn_off(self):
        print("Computer has Turned Off")

computer = Computer()
computer.turn_on()
computer.turn_off()

# ----------------------------------------------------------------------------------------------------------------------

# Constructor with Parameters

# - Create a Dog class.
# - Dog should have a constructor with a name parameter.
# - Dog should have a method say_name that prints the name of the dog.

class Animal:
    def __init__(self, name = ""):
        self.name = name

    def say_name(self):
        if self.name:
            print(self.name)
        else:
            print("I don't have a name yet.")

    def speak(self):
        print("I cant speak!")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog("Dog")
dog.say_name()

# ----------------------------------------------------------------------------------------------------------------------

# Inheritance

# Create the classes that would make the following code possible, with the caveat that
# both Dog and Cat must inherit from Animal.


animal = Animal()
animal.say_name()   # Prints: I don't have a name yet.
animal.speak()      # Prints: I can't speak!
#
dog = Dog('Fido')
dog.say_name()      # Prints: Fido
dog.speak()         # Prints: Woof!
#
cat = Cat('Max')
cat.say_name()      # Prints: Max
cat.speak()         # Prints: Meow!

# ----------------------------------------------------------------------------------------------------------------------

# Exercises
# Exercise 1: Books and Authors

# Create an empty class called Book. Then create three instances.
# Add the following attributes for each of the instances: title, author, and publication_year.
# Create print statements to display the attributes of each one of the instances.

# Pre-code:
class Book:
   pass

book1 = Book()
book1.title = 'To Kill a Mockingbird'
book1.author = 'Harper Lee'
book1.publication_year = 1960

# Your code here

print(f"{book1.title} is written by {book1.author} and was published in {book1.publication_year}.")

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 2. Vehicle and Types of Vehicles

# Create a Vehicle class.
# - Its constructor should take the name and type of the vehicle and store them as instance attributes.
# - This Vehicle class should also have a show_type() instance method that prints out the
#   message: "<NAME_OF_VEHICLE> is a <TYPE_OF_VEHICLE>"
# - Create Car and Bike classes that inherit from Vehicle.
# - Create instances of Car and Bike and make them show their types.

class Vehicle:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def show_type(self):
        print(f"{self.name} is a {self.type}")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

car = Car("Thunderbird", "Sports Car")
bike = Bike("Huffy", "Bicycle")
car.show_type()
bike.show_type()

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 3. Spot and correct the mistakes

# - You are given a task to create a Car class.
# - Each car will have attributes for model and year.
# - Unfortunately, the given code below contains several mistakes.
# - Your task is to find and correct these mistakes to make the code run successfully.
# - Please include a comment in the code explaining the corrections you made and why.

# Pre-code
class Car:
   def __init__(self, model, year):
       self.model = model
       self.year = year

my_car = Car("Toyota", 2024)
print(my_car.model)
print(my_car.year)

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 4. SmartHome with Constructor

# Create a SmartHome class that has a constructor __init__ and a send_notification() method.
#
# The constructor should initialize the attributes:
# - home_name
# - location
# - number_of_devices
#
# send_notification() should print a notification including the home_name and location.

# Create instances for the following:
# Home Name      Location      Number of Devices
# Villa Rosa     New York      15 devices
# Green House    California    10 devices
# Sea View       Florida       20 devices

# Call the send_notification() method for each instance, 
# passing a message reminding to turn off the lights.


class SmartHome:
    def __init__(self, home_name, location, number_of_devices):
        self.home_name = home_name
        self.location = location
        self.number_of_devices = number_of_devices

    def send_notification(self, message):
        print(f"Notification for {self.home_name}, {self.location}: {message}")

home1 = SmartHome("Villa Rosa","New York","15 devices")
home2 = SmartHome("Green House","California","10 devices")
home3 = SmartHome("Sea View ","Florida","20 devices")
home1.send_notification("Reminder to turn off the lights")
home2.send_notification("Reminder to turn off the lights")
home3.send_notification("Reminder to turn off the lights")

# ----------------------------------------------------------------------------------------------------------------------

# Exercise 5. Inheritance. Spot and correct mistakes

# You should have the following hierarchy of classes:

 # Animal
 # │
 # ├── Mammal
 # │
 # ├── Bird
 # │
 # └── Fish

# Each class has the following attributes:

# - Animal name
# - Mammal name, age, number of legs
# - Bird name, age, can fly or not
# - Fish name, age, number of fins

# But, the provided code for these classes and their instances has several mistakes
# related to hierarchy, class attributes, and instance creation.

# Find and correct these mistakes to make the code work properly.
# Leave a comment in the code explaining what the problems were and why it wouldn't work.
# There are seven mistakes in the pre-code.

# Pre-code
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Mammal(Animal):
    def __init__(self, name, age, num_legs):
        super().__init__(name, age)
        self.num_legs = num_legs

class Bird(Animal):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

class Fish(Animal):
    def __init__(self, name, age, num_fins):
        super().__init__(name, age)
        self.num_fins = num_fins

tiger = Mammal('Tiger', 5, 4)
sparrow = Bird("sparrow", 3, True)
goldfish = Fish('Goldfish', 2, 4)
