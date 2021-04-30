# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseNodesInKGroups(l, k):
    if l is None:
        return None

    lastNode = None
    node = l
    count = 0

    while node is not None and count < k:
        lastNode = node
        node = node.next
        count += 1

    if lastNode is not None:
        lastNode.next = None

    if count == k:
        result = reverseLinkedList(l)
        l.next = reverseNodesInKGroups(node, k)
    else:
        result = l

    return result

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

def printList(l):
    node = l
    result = ""

    while node is not None:
        result += f"{node.value} ->"
        node = node.next

    result += " NULL"
    print(result)