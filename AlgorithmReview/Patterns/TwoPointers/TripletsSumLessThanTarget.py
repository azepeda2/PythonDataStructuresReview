def searchTriplets(arr, target):
    if len(arr) < 3:
        return 0
    
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        count += searchPair(arr, target - arr[i], i)
    return count

def searchPair(arr, target_sum, first):
    count = 0
    left = first + 1
    right = len(arr) - 1

    while (left < right):
        if arr[left] + arr[right] < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    return count

if __name__ == '__main__':
    print(searchTriplets([-1, 0, 2, 3], 3))
    print(searchTriplets([-1, 4, 2, 1, 3], 5))