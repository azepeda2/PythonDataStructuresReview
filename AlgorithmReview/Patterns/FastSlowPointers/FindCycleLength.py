class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next


def findCycleLength(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return calculateLength(slow)

    return 0

def calculateLength(slow):
    current = slow
    count = 0

    while True:
        current = current.next
        count += 1

        if current == slow:
            break

    return count


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
print("LinkedList has cycle: " + str(findCycleLength(head)))

head.next.next.next.next.next.next = head.next.next
print("LinkedList has cycle: " + str(findCycleLength(head)))

head.next.next.next.next.next.next = head.next.next.next
print("LinkedList has cycle: " + str(findCycleLength(head)))