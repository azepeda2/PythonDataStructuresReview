"""
Take the Dog and Cat classes you built in the last practice and
override the greeting method to give the following output:

Dog: "Hello <NAME>, my name is <DOG_NAME> and I'm a dog! 🐶"
Cat: "Hello <NAME>, my name is <CAT_NAME> the cat and I hate you. 😾"
"""

class Animal:
    def __init__(self, name):
        self.Name = name
    def greeting(self, name):
        print(f"Hello {name}, I'm {self.Name}")

class Dog(Animal):
    def greeting(self, name):
        print(F"Hello {name}, my name is {self.Name} and I'm a dog! 🐶")
class Cat(Animal):
    def greeting(self, name):
        print(F"Hello {name}, my name is {self.Name} the cat and I hate you. 😾")

animal = Animal("Animal")
dog = Dog("Dog")
cat = Cat("Cat")

animal.greeting("Alex")
dog.greeting("Alex")
cat.greeting("Alex")