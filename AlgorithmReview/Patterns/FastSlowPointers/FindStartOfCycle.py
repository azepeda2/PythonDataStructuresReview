class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next


def findCycleStart(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycleLength = calculateLength(slow)
            break

    return findStart(head, cycleLength)

def calculateLength(slow):
    current = slow
    count = 0

    while True:
        current = current.next
        count += 1

        if current == slow:
            break

    return count

def findStart(head, cycleLength):
    pointer1 = head
    pointer2 = head

    while cycleLength > 0:
        pointer2 = pointer2.next
        cycleLength -= 1

    while pointer1 != pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next

    return pointer1

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

# Create a cycle by connecting nodes
head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle start: " + str(findCycleStart(head).val))

# Create a different cycle
head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle start: " + str(findCycleStart(head).val))

# Create a cycle that points back to the head
head.next.next.next.next.next.next = head
print("LinkedList cycle start: " + str(findCycleStart(head).val))