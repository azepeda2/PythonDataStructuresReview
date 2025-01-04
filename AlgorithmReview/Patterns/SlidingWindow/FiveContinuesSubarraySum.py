def calculateSubarraySums(arr, k):
    subSums = []
    for i in range(len(arr) - k + 1):
        sum = 0
        for j in range(i, i + k):
            print(f"i: {i} j: {j}")
            sum += arr[j]

        subSums.append(sum / k)

    return subSums
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(calculateSubarraySums(arr, k))