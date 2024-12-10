def removeInPlace(arr, key):
    currentInsertionIndex = 0

    for i in range(len(arr)):
        if arr[i] != key:
            arr[currentInsertionIndex] = arr[i]
            currentInsertionIndex += 1

    return currentInsertionIndex

print(removeInPlace([3, 2, 3, 6, 3, 10, 9, 3], 3))
print(removeInPlace([2, 11, 2, 2, 1], 2))