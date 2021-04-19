class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BinaryTreeNode(data)
        else:
            self.root.insert(data)

    def inserDatas(self, datas):
        for data in datas:
            self.insert(data)

    def printTree(self):
        self.root.printTree()

class BinaryTreeNode:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if self.data > data:
            if self.left is None:
                self.left = BinaryTreeNode(data)
            else:
                self.left.insert(data)
        elif self.data < data:
            if self.right is None:
                self.right = BinaryTreeNode(data)
            else:
                self.right.insert(data)

    def printTree(self):
        if self.left:
            self.left.printTree()
        
        print(self.data)
        
        if self.right:
            self.right.printTree()

def checkBST(root):
    return isBst(root, set(), {}, {})
    
def isBst(root, visited, minInSubtrees, maxInSubtrees):
    if root is None:
        return True

    if root.data in visited:
        return False

    visited.add(root.data)
    nodeIsValid = isNodeValid(root, minInSubtrees, maxInSubtrees)
    return nodeIsValid and isBst(root.left, visited, minInSubtrees, maxInSubtrees) and isBst(root.right, visited, minInSubtrees, maxInSubtrees)

def isNodeValid(root, minInSubtrees, maxInSubtrees):
    maxLeftSubtree = getMaxDataInTree(root.left, minInSubtrees)
    minRightSubtree = getMinDataInTree(root.right, maxInSubtrees)
    return maxLeftSubtree < root.data < minRightSubtree

def getMaxDataInTree(root, minInSubtrees):
    if root is None:
        return float('-inf')

    if root.data in minInSubtrees:
        return minInSubtrees[root.data]

    result = max(root.data, getMaxDataInTree(root.left, minInSubtrees), getMaxDataInTree(root.right, minInSubtrees))
    minInSubtrees[root.data] = result

    return result

def getMinDataInTree(root, maxInSubtrees):
    if root is None:
        return float('inf')

    if root.data in maxInSubtrees:
        return maxInSubtrees[root.data]

    result = min(root.data, getMinDataInTree(root.left, maxInSubtrees), getMinDataInTree(root.right, maxInSubtrees))
    maxInSubtrees[root.data] = result

    return result

if __name__ == "__main__":
    elements = [9, 5, 3, 7, 13, 11, 15]
    bb = BinaryTree()
    bb.inserDatas(elements)
    if checkBST(bb.root):
        print("Yes")
    else:
        print("No")
