# Given a number, print its factorial.

number = 5

factorial = 1

for num in range(1, number + 1):
    factorial *= num

print(f"{factorial} is the factorial of {number}")