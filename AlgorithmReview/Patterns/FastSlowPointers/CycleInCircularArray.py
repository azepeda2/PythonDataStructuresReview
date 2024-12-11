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


def isCircularOptimized(arr):
    n = len(arr)
    visited = [False] * n  # Initialize visited array

    for i in range(n):
        if visited[i]:
            continue  # Skip already visited indices

        isForward = arr[i] >= 0  # Determine the direction
        slow, fast = i, i

        # Use slow and fast pointers to detect cycle
        while True:
            slow = findNextIndex(arr, isForward, slow)
            fast = findNextIndex(arr, isForward, fast)
            if fast != -1:
                fast = findNextIndex(arr, isForward, fast)

            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True  # Cycle found

        markVisited(arr, i, isForward, visited)

    return False


def markVisited(arr, startIndex, isForward, visited):
    index = startIndex
    while True:
        visited[index] = True
        nextIndex = findNextIndex(arr, isForward, index)
        if nextIndex == -1 or visited[nextIndex]:
            break
        index = nextIndex


print(isCircular([1, 2, -1, 2, 2]))
print(isCircular([2, 2, -1, 2]))
print(isCircular([2, 1, -1, -2]))