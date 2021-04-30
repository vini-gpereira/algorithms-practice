# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    x = l1
    y = l2
    res = None
    resNode = None

    while x is not None and y is not None:
        if x.value < y.value:
            if resNode is None:
                res = x
            else:
                resNode.next = x
            resNode = x
            x = x.next
        else:
            if resNode is None:
                res = y
            else:
                resNode.next = y
            resNode = y
            y = y.next

    if x is not None:
        resNode.next = x
    
    if y is not None:
        resNode.next = y

    return res
    
