def moveElements(arr):
    nextNonDuplicate = 1

    i = 0

    while i < len(arr):
        if arr[nextNonDuplicate - 1] != arr[i]:
            arr[nextNonDuplicate] = arr[i]
            nextNonDuplicate += 1

        i += 1

    return nextNonDuplicate

print(moveElements([2, 3, 3, 3, 6, 9, 9]))  # Output: 4 (modified array: [2, 3, 6, 9, 6, 9, 9])
print(moveElements([2, 2, 2, 11]))         # Output: 2 (modified array: [2, 11, 2, 11])
