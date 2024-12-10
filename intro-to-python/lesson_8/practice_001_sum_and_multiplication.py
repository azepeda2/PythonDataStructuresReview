# Given a list.
# Calculate sum and multiplication of all elements.
# Print the list, sum and multiplication of elements.
# For example:
# Input: [1, 2, 3, 4]
# Output sum: 10
# Output multiplication: 24

numbers =  [1, 2, 3, 4]

sum = 0
product = 1

for num in numbers:
    sum += num
    product *= num

print(numbers)
print(f"Output sum: {sum}")
print(f"Output product: {product}")