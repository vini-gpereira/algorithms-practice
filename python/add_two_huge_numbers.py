# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def addTwoHugeNumbers(a, b):
    if a is None:
        return b
    if b is None:
        return a

    a = reverseLinkedList(a) # O(n)
    b = reverseLinkedList(b) # O(n)

    x = a
    y = b
    overflow = 0
    initialRes = None
    res = None

    while x is not None and y is not None:
        s = x.value + y.value + overflow
        overflow = s // 10000
        newNodeValue = s % 10000
        newNode = ListNode(newNodeValue)

        if res is None:
            res = newNode
            initialRes = newNode
        else:
            res.next = newNode
            res = res.next

        x = x.next
        y = y.next

    while x is not None:
        s = x.value + overflow
        overflow = s // 10000
        newNodeValue = s % 10000
        newNode = ListNode(newNodeValue)
        res.next = newNode
        res = res.next
        x = x.next

    while y is not None:
        s = y.value + overflow
        overflow = s // 10000
        newNodeValue = s % 10000
        newNode = ListNode(newNodeValue)
        res.next = newNode
        res = res.next
        y = y.next

    if overflow > 0:
        res.next = ListNode(overflow)

    return reverseLinkedList(initialRes)

def reverseLinkedList(l):
    node = l
    lastNode = None
    nextNode = None

    while node:
        nextNode = node.next
        node.next = lastNode
        lastNode = node
        node = nextNode

    return lastNode
