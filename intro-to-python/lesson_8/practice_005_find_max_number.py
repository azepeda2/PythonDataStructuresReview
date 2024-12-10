# Your goal is to write a Python program that finds the maximum number in a given list of numbers.
# Example:
# numbers = [1, 2, 42, 77, 99, -100]
# Output: 99

numbers = [1, 2, 42, 77, 99, -100]
max = numbers[0]

for num in numbers:
    if num > max:
        max = num

print(numbers)
print(max)