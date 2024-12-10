def squareArray(arr):
    n = len(arr)

    squared = [0 for x in range(n)]
    left = 0
    right = n - 1
    highestSquaredIndex = n - 1

    while left <= right:
        leftSquared = arr[left] * arr[left]
        rightSquared = arr[right] * arr[right]

        if leftSquared > rightSquared:
            squared[highestSquaredIndex] = leftSquared
            left += 1
        else:
            squared[highestSquaredIndex] = rightSquared
            right -= 1

        highestSquaredIndex -= 1

    return squared

print("Squares: " + str(squareArray([-2, -1, 0, 2, 3])))
print("Squares: " + str(squareArray([-3, -1, 0, 1, 2])))