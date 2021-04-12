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

def serialize(node):
    result = ""
    if node is not None:
        result += f"{node.value};"
        result += serialize(node.left)
        result += serialize(node.right)
    return result

def deserialize(serialized):
    values = serialized.split(";")[:-1]
    numbers = [int(value) for value in values]
    bb = BinaryTree()
    bb.inserValues(numbers)
    return bb

if __name__ == "__main__":
    bb = BinaryTree()
    bb.inserValues([100, 50, 25, 75, 200, 350])
    bb.printTree()

    serialized = serialize(bb.root)
    copy = deserialize(serialized)

    print("----------")
    
    copy.printTree()

