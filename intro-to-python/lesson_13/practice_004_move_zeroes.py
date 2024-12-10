# Given an array of integers, write a function to move all 0's
# to the end while maintaining the relative order of the other elements.
# Input: 0 4 0 3 12
# Output: 4 3 12 0 0

def move_zeros(arr):
    zeroes = 0
    i = 0

    for number in arr:
        if number == 0:
            zeroes += 1
        else:
            arr[i] = number
            i += 1

    while zeroes > 0:
        arr[i] = 0
        i += 1
        zeroes -= 1

arr = [0, 4, 0, 3, 12]
print(arr)
move_zeros(arr)
print(arr)
