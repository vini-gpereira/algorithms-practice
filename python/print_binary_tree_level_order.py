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

def level_order_traversal(root):
  levels = create_levels_map(root)
  result = create_order_traversal_string(levels)
  return result

def create_levels_map(root):
    levels = {}
    _create_levels_map(root, 0, levels)
    return levels

def _create_levels_map(node, depth, levels):
    if node is not None:
        if depth in levels:
            levels[depth].append(node.value)
        else:
            levels[depth] = [node.value]
        _create_levels_map(node.left, depth + 1, levels)
        _create_levels_map(node.right, depth + 1, levels)

def create_order_traversal_string(levels):
    result = ""
    for level in levels.values():
        for number in level:
            result += str(number) + " "
        result += "\n"
    return result

if __name__ == "__main__":
    binaryTree = BinaryTree()
    binaryTree.inserValues([100, 50, 200, 25, 75, 350])
    print(level_order_traversal(binaryTree.root))
