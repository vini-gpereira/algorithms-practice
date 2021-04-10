import time

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

    def printTree(self):
        self.root.printTree()

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

def convert_to_linked_list(binaryTree):
    return _convert_to_linked_list(binaryTree.root)

def _convert_to_linked_list(node):
    if node is not None:
        leftSubtree = _convert_to_linked_list(node.left)
        rightSubtree = _convert_to_linked_list(node.right)
        node.left = node.right = node
        node = concatenate_list(leftSubtree, node)
        node = concatenate_list(node, rightSubtree)

    return node

def concatenate_list(head1, head2):
    if head1 is None:
        return head2
    
    if head2 is None:
        return head1

    tail1 = head1.left
    tail2 = head2.left

    tail1.right = head2
    head2.left = tail1

    tail2.right = head1
    head1.left = tail2

    return head1


if __name__ == "__main__":
    binaryTree = BinaryTree()
    binaryTree.inserValues([10, 3, 20, 7, 1, 15, 25])
    binaryTree.printTree()
    binaryTree.root = convert_to_linked_list(binaryTree)
    current = binaryTree.root

    while True:
        print(current.value, "<->", end=" ")
        current = current.right
        if current == binaryTree.root:
            break
    
    print()

