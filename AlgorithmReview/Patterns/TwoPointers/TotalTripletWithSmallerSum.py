import sys


def findTriplets(arr, targetSum):
    arr.sort()

    n = len(arr)
    currentSum = sys.maxsize
    matchingTriplets = 0

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while(left < right):
            currentSum = arr[i] + arr[left] + arr[right]

            if currentSum < targetSum:
                matchingTriplets += right - left
                left += 1
            else:
                right -= 1

    return matchingTriplets

print(findTriplets([-1, 0, 2, 3], 3))
print(findTriplets([-1, 4, 2, 1, 3], 5))