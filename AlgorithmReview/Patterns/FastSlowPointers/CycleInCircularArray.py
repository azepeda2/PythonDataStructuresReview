def isCircular(arr):
    for i in range(len(arr)):
        isForward = arr[0] >= 0
        slow = i
        fast = i

        while True:
            slow = findNextIndex(arr, isForward, slow)
            fast = findNextIndex(arr, isForward, fast)

            if fast != -1:
                fast = findNextIndex(arr, isForward, fast)

            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True

    return False

def findNextIndex(arr, isForward, currentIndex):
    direction = arr[currentIndex] >= 0

    if isForward != direction:
        return -1

    nextIndex = (currentIndex + arr[currentIndex]) % len(arr)

    if nextIndex == currentIndex:
        nextIndex = -1

    return nextIndex


print(isCircular([1, 2, -1, 2, 2]))
print(isCircular([2, 2, -1, 2]))
print(isCircular([2, 1, -1, -2]))