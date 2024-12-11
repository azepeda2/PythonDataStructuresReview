class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

def findMid(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Print the middle node's value
print("Middle Node: " + str(findMid(head).val))

head.next.next.next.next.next = Node(6)
# Print the middle node's value after adding a new node
print("Middle Node: " + str(findMid(head).val))

head.next.next.next.next.next.next = Node(7)
# Print the middle node's value after adding another new node
print("Middle Node: " + str(findMid(head).val))


head.next.next.next.next.next.next = head.next.next.next
print("LinkedList has cycle: " + str(findMid(head)))