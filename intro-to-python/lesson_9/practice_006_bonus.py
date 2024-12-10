# Create a program that does the following:
#
# 1. Keeps asking for names, one at a time. Stop asking for names when user's input is "end".
# 2. When the user is done adding names, the program should show two lines for each name:
#    - A line with a greeting: "Hello, {name}!"
#    - A line with the first letter of the user's name: "Your initial is {initial}."
#
# Use at least one function. Extra points if you use two and call a function from another function.

def create_names_list():
    name = ""
    list = []

    while name != "end":
        name = input("Enter a name (enter 'end' to finish): ")
        if name != "" and name != "end":
            list.append(name.title())

    return list

def print_greetings(names_list):
    for name in names_list:
        initial = name[0]
        print(f"Hello, {name}")
        print(f"Your initial is {initial}")

names = create_names_list()
print_greetings(names)