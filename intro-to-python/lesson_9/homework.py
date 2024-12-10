# HOMEWORK: Functions
# Read carefully until the end before you start solving the exercises.

# Basic Function
# Define a basic function that only prints Hello. Create the definition using def and the call that executes it.

def hello():
    print("Hello")

hello()

# ----------------------------------------------------------------------------------------------------------------------

# Basic Function with Parameters
# Define a basic function that prints a greeting taking a given name.

def greeting(name = "stranger"):
    print(f"Hello, {name}!")

greeting("Alex")

# ----------------------------------------------------------------------------------------------------------------------

# Basic Function with Default Values
# Define a basic function that prints a greeting for a name, but if none is given, use stranger instead of the name,
# so it behaves like this:

# Prints: Hello, stranger!
greeting()

# Prints: Hello, Tom!
greeting('Tom')

# ----------------------------------------------------------------------------------------------------------------------

# Multiple Parameters
# Define a function that takes two parameters, add them up and prints the sum.

def add(num1 = 0, num2 = 0):
    sum = num1 + num2
    print(f"The sum of {num1} + {num2} = {sum}")

# Prints: The sum of 1 + 2 = 3
add(1, 2)

# Prints (default values might be useful): The sum of 1 + 0 = 1
add(1)

# ----------------------------------------------------------------------------------------------------------------------

# Parameters out of order
# Define a function that takes a first_name and a last_name and prints a full_name. Define the function and create
# the function call in such a way that first_name and last_name can be given in any order and the printed full_name
# would still be correct.

def full_name(first, last):
    print(f"{first} {last}")

# Prints: Nelson Mandela
full_name("Nelson", "Mandela")

# Is there anything you can add to the line below, so the function also prints "Nelson Mandela"?
full_name(last="Mandela", first="Nelson")

# ----------------------------------------------------------------------------------------------------------------------

# Returning Values
# Define a validator function that you can use to determine if a word is longer than 8 characters.
# After creating the function, make sure to test it. Create a list of words and iterate over this
# list using a for loop.

# Tip: Validator functions return True / False which we can use in conditionals to do things like print a message.

def validate_length(word):
    if len(word) > 8:
        return True
    else:
        return False

list = ["fix", "my", "sleep", "passwords", "restlessness", "food", "accomplishment"]

for word in list:
    result = validate_length(word)
    if result:
        print(f"{word} is longer than 8 characters")
    else:
        print(f"{word} is not longer than 8 characters")

# ----------------------------------------------------------------------------------------------------------------------

# You're going to revisit some of the algorithms you've already solved. But this time, there's a twist! Your challenge
# is to solve and encapsulate each algorithm into its own Python function. This will not only help you review these
# algorithms but also give you valuable practice in defining and using functions.

# FizzBuzz
# You remember FizzBuzz, right?
# You print Fizz for multiples of 3, Buzz for multiples of 5, and FizzBuzz for multiples of both 3 and 5.

# Now, your task is to take your existing FizzBuzz code and wrap it into a function called fizzbuzz.

# Requirements:
# - Create a function named fizzbuzz that takes a single argument, number.
# - If the number is a multiple of both 3 and 5, the function should return: FizzBuzz
# - If the number is a multiple of 3, the function should return: Fizz
# - If the number is a multiple of 5, the function should return: Buzz
# - Otherwise, the function should return the number.

# Call the function here

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number

print(fizzbuzz(15))

# ----------------------------------------------------------------------------------------------------------------------

# Anagram
# Your next challenge is to implement a function that checks if two given strings are anagrams of each other.
# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase. For example,
# "listen" is an anagram of "silent".

# What You Need to Check
# - The two strings must have the same length.
# - The sorted form of the first string must be equal to the sorted form of the second string.

# Approach
# - Create a function that takes two strings as arguments.
# - Check if the lengths are equal. If they're NOT equal, return False (anagrams are always same length).
# - Sort both strings. If the sorted versions are equal, they're anagrams!

# Test your function with these strings
test_str1 = 'abcde'
test_str2 = 'edcba'

def is_anagram(word1, word2):
    if len(word1) != len(word2):
        return False

    sorted1 = sorted(word1)
    sorted2 = sorted(word2)

    if sorted1 == sorted2:
        return True
    else:
        return False

result = is_anagram(test_str1, test_str2)
print(f"{test_str1} is an anagram of {test_str2}: {result}")

# ----------------------------------------------------------------------------------------------------------------------

# Find Max number
# Create a function to find the largest number in a list without using the built-in max() function.

# - Define a function called find_max that takes a list of numbers as an argument.
# - Initialize a variable result and set it to the 1st item of the list using [0]
#   - This variable will hold the largest number as we iterate through the list.
# - Loop through each number in the list.
# - Check if number > result
#   - If it is, update result with the new greater number.
# - return result

# Define your function here

def max_number(numbers):
    result = numbers[0]

    for num in numbers:
        if num > result:
            result = num

    return result

# Test the function with a sample list of numbers.

nums = [4, 3, 2, 5, 8, 10, 3, 6]
print(max(nums))

# Output should be the maximum number in the list.

# ----------------------------------------------------------------------------------------------------------------------

# Even/Odd Checker Function
# Your task is to write a function that determines if a given integer is even or odd. The function should
# print Even for even numbers and Odd for odd numbers.

# What You Need to Check
# - Determine whether the input number is even or odd.
# - An even number can be exactly divided by 2 without a remainder.
# - An odd number leaves a remainder of 1 when divided by 2.

# Define a function is_even_odd(number) here

def is_even_odd(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# Test the function calling it using a variety of numbers like: 1, 10, 5.5, 9

numlist = [1, 10, 5.5, 9]

for num in numlist:
    print(f"{num} is: ")
    is_even_odd(num)