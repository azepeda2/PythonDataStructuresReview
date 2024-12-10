# Homework Lesson 5 - Workshop - Homework

# READ CAREFULLY THE EXERCISE DESCRIPTION AND SOLVE IT RIGHT AFTER IT

# Challenge 1
# Make a number Positive
#
# Create a variable called my_number and set it to any integer value.
# Write code to make the number positive if it's negative, and keep it
# as is if it's already positive or zero.
#
# Example:
# Input: -3 => Output: 3
# Input: 5 => Output: 5

my_number = -500

if my_number < 0:
    my_number = -my_number

print(my_number)

# ---------------------------------------------------------------------

# Challenge 2
# BinGo!
#
# If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”
# For numbers which are divisible of 3 and 7, print “BinGo”
# Otherwise, print the original number: “{number} is just a number”

number = 21

if number % 3 == 0 and number % 7 == 0:
    print("BinGo")
elif number % 3 == 0:
    print("Bin")
elif number % 7 == 0:
    print("Go")
else:
    print(f"{number} is just a number")

# ---------------------------------------------------------------------

# Challenge 3
# Find the middle number
#
# Given three different numbers x, y, and z, find the number that is neither
# the smallest nor the largest and print it.
#
# Example:
# x = 1, y = 5, z = 3 => Output: 3

x = 1
y = 5
z = 3

if x <= y <= z or z <= y <= x:
    print(y)
elif y <= x <= z or z <= x <= y:
    print(x)
else:
    print(z)

# ---------------------------------------------------------------------

# Challenge 4
# Palindrome Numbers
#
# Ask a user to input a number.
# Write a program to check if the given number is a palindrome.
# It should print True if the number is a palindrome and False if it is not.
#
# Palindrome number: 121, 898

number = 121

num_str = str(number)

print(num_str == num_str[::-1])

i = 0
j = len(num_str) - 1
isPalindrome = "True"

while i < j:
    if num_str[i] != num_str[j]:
        isPalindrome = "False"
        break
    i += 1
    j -= 1

print(isPalindrome)
# ---------------------------------------------------------------------

# Challenge 5
# Reverse a string
#
# You're part of a team working on analyzing customer reviews for a new video game.
# Due to a software glitch, some reviews have been recorded in reverse with punctuation
# at the beginning instead of the end. Your task is to correct these reviews so that they
# are in the correct order and the punctuation is appropriately placed at the end of the
# sentence or word.
#
# Example: "tcefreP!" -> Perfect!

review = "tcefreP!"

fixed = review[:-1][::-1] + review[-1]
print(fixed)