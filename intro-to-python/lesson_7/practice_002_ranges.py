# Figure out the values required for range() to generate the expected result:

# 0, 1, 2, 3, 4
for num in range(0, 5):
    print(num)

# 20, 21, 22 ... 30 (all the numbers between 20 and 30, inclusive)
for num in range(20, 31):
    print(num)

# Even numbers: 2, 4, 6, 8, 10
for num in range(2, 11, 2):
    print(num)

# Years ending in zero between 1900 and 2000 (inclusive)
for num in range(1900, 2001, 10):
    print(num)

# Bonus!
# 20, 19, 18, 17, 16
for num in range(20, 15, -1):
    print(num)

# print(list(range(20, 15, -1)))