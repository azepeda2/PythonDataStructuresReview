# A palindrome is a word, number, phrase, or other sequence of symbols
# that reads the same backwards as forwards:
#
# madam -> madam
# racecar -> racecar
# tacocat -> tacocat
#
# Write a program that will print True if the word is a palindrome
# and False if it is not.

word = "racecara"

i = 0
j = len(word) - 1
isPalindrome = "True"

print(word)
print(word[::-1])
print(len(word))
print(word == word[::-1])

while i < j:
    if word[i] != word[j]:
        isPalindrome = "False"
        break
    i += 1
    j -= 1

print(isPalindrome)