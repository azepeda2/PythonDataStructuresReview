# Given an integer, return the integer with reversed digits.
#
# Note:
# The integer could be either positive or negative.
#
# Example:
# -876 -> -678

number = -789
num_str = str(number)

if number < 0:
    reversed = num_str[0] + num_str[4:0:-1]
else:
    reversed = num_str[::-1]

print("original: " + num_str)
print("reversed: " + reversed)
