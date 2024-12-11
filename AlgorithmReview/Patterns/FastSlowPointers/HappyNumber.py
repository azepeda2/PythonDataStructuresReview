def findHappyNumber(number):
    slow = number
    fast = number

    while True:
        slow = findSquareSum(slow)
        fast = findSquareSum(findSquareSum(fast))

        if slow == fast:
            break

    return slow == 1


def findSquareSum(num):
    sum = 0

    while num > 0:
        digit = num % 10
        sum += digit * digit
        num //= 10

    return sum

print(findHappyNumber(23))
print(findHappyNumber(12))