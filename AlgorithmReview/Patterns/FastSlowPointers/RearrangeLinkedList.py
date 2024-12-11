class Node:
 def __init__(self, value, next=None):
   self.val = value
   self.next = next

def rearrangeList(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    middle = slow
    prev = None

    while middle is not None:
        next = middle.next
        middle.next = prev
        prev = middle
        middle = next

    secondHalfHead = prev
    firstHalfHead = head

    while firstHalfHead is not None and secondHalfHead is not None:
        temp = firstHalfHead.next
        firstHalfHead.next = secondHalfHead
        firstHalfHead = temp

        temp = secondHalfHead.next
        secondHalfHead.next = firstHalfHead
        secondHalfHead = temp

    if firstHalfHead is not None:
        firstHalfHead.next = None

    return head

def printList(head):
    temp = head
    while temp is not None:
        print(str(temp.val) + " ", end="")
        temp = temp.next
    print()

head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
head.next.next.next.next.next = Node(12)
printList(head)
rearrangeList(head)
printList(head)

