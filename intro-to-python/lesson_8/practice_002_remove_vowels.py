# Remove the lowercase vowels in a given string:
# str1 = ‘Hello, World!’
# The vowels are:
# vowels = "aeiou"
# “y” is not considered a vowel for this task. The input string is always in lowercase.
# Examples:
# "hello" --> "hll"
# "goodbye" --> "gdby"

str1 = "hello, world!"
vowels = "aeiou"
str2 = ""

for char in str1:
    if char not in vowels:
        str2 += char

print(str2)