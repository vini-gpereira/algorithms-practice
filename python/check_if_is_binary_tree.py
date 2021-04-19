def checkBST(root):
    return isBst(root, float('-inf'), float('inf'))
    
def isBst(root, minimum, maximum):
    if root is None:
        return True

    if minimum < root.data < maximum:
        return isBst(root.left, minimum, root.data) and isBst(root.right, root.data, maximum)
    
    return False

if __name__ == "__main__":
    elements = [9, 5, 3, 7, 13, 11, 15]
    bb = BinaryTree()
    bb.inserDatas(elements)
    if checkBST(bb.root):
        print("Yes")
    else:
        print("No")
