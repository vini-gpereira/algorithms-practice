# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    length = getListLength(l)
    goal = length - n + 1

    if goal == 1 or n == 0:
        return l

    idx = 1
    node = l
    lastNode = node

    while node is not None and idx < goal:
        lastNode = node
        node = node.next
        idx += 1

    if lastNode is not None:
        lastNode.next = None
    
    return connectLists(node, l)
    

def getListLength(l):
    length = 0
    node = l
    
    while node is not None:
        node = node.next
        length += 1
        
    return length

def connectLists(l1, l2):
    if l1 is None:
        return l2

    node = l1

    while node.next is not None:
        node = node.next

    node.next = l2
    return l1
