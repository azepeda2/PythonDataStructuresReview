"""
Create a basic dictionary that contains the following information about
an imaginary person:

- Their name
- Their age
- Their location (city, state). Bonus points if you use a
  nested dictionary.
- Whether they’re married or not.
"""

dict = {
    "name" : "Alex",
    "age" : 30,
    "location" : {
        "city" : "San Francisco",
        "state" : "California"
    },
    "married" : False
}

car = {}
car["make"] = "Cadillac"
car["model"] = "Escalade"
car["year"] = 2024

print(dict)
print(car)