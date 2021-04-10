class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = BinaryTreeNode(value)
        else:
            self.root.insert(value)

    def inserValues(self, values):
        for value in values:
            self.insert(value)

class BinaryTreeNode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BinaryTreeNode(value)
            else:
                self.left.insert(value)
        elif self.value < value:
            if self.right is None:
                self.right = BinaryTreeNode(value)
            else:
                self.right.insert(value)

    def printTree(self):
        if self.left:
            self.left.printTree()
        
        print(self.value)
        
        if self.right:
            self.right.printTree()

class LinkedList:
    def __init__(self):
        self.first = None

    def insert(self, value):
        newNode = LinkedListNode(value)
        if self.first is None:
            self.first = newNode
        else:
            newNode.next = self.first
            self.first.previous = newNode
            self.first = newNode

    def insertValues(self, values):
        for value in values:
            self.insert(value)

    def printLinkedList(self):
        node = self.first
        while node is not None:
            print(node.value, "->", end=" ")
            node = node.next
        print()

class LinkedListNode:
    def __init__(self, value):
        self.next = None
        self.previous = None
        self.value = value

def convert_to_linked_list(binaryTree):
    linkedList = LinkedList()
    return rec_convert_to_linked_list(binaryTree.root, linkedList)
    
def rec_convert_to_linked_list(node, linkedList):
    if node is None:
        return linkedList
    
    linkedList = rec_convert_to_linked_list(node.right, linkedList)

    linkedList.insert(node.value)

    linkedList = rec_convert_to_linked_list(node.left, linkedList)

    return linkedList

if __name__ == "__main__":
    binaryTree = BinaryTree()
    binaryTree.inserValues([10, 3, 20, 7, 1, 15, 25])
    linkedList = convert_to_linked_list(binaryTree)
    linkedList.printLinkedList()
