# Given two words, check if both are anagrams.
# An anagram of a string is another string that contains the same characters, only the order
# of characters can be different.
# For example:
# is_anagram('cat', 'act') => should return True
# is_anagram('bus', 'sub') => should return True
# is_anagram('map', 'cap') => should return False


str1 = "cat"
str2 = "tac"

if len(str1) != len(str2):
    print("False")
elif sorted(str1) == sorted(str2):
    print("True")
else:
    print("False")

