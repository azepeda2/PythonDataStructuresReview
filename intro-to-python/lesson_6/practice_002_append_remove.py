# Create an empty list and add the following elements about your location, in this order:
# - City
# - State or Province
# - A list with the temperatures the last three days
# - Your favorite animal

my_list = []
my_list.append("Oakland")
my_list.append("Cali")
my_list.append([80, 75, 70])
my_list.append("Penguin")

print(my_list)

# Then, remove the State, without using the indexes.
my_list.remove("Cali")
print(my_list)

# Bonus: Remove the last element, using a negative index.
del my_list[-1]
print(my_list)