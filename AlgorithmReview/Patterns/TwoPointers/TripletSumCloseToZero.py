def searchTriplets(arr):
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        searchPair(arr, -arr[i], i + 1, triplets)

    return triplets

def searchPair(arr, targetSum, left, triplets):
    right = len(arr) - 1

    while(left < right):
        currentSum = arr[left] + arr[right]

        if currentSum == targetSum:
            triplets.append([-targetSum, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif targetSum > currentSum:
            left += 1
        else:
            right -= 1

print(searchTriplets([-3, 0, 1, 2, -1, 1, -2]))
print(searchTriplets([-5, 2, -1, -2, 3]))