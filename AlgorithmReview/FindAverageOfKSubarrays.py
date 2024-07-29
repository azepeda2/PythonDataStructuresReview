def find_average_of_subarrays(K, array):
    result = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(array)):
        windowSum+= array[windowEnd]
        # slide the windo, no need to slide if we have not hit the required window size of K
        if windowEnd >= K - 1:
            result.append(windowSum / K)
            windowSum -= array[windowStart]
            windowStart += 1

    return result


def find_average_of_subarrays_slower(K, array):
    result = []
    for i in range(len(array) - K + 1):
        #find sum of the next  K elems
        _sum = 0.0
        for j in range (i, i + K):
            _sum = array[j]
        result.append(_sum / K) # calculate average

    return result

def main():
    result = find_average_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Average of subarrays of size K: "+ str(result))

main()