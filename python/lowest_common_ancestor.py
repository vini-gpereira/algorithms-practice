def lca(root, v1, v2):
    cmp1 = 0
    cmp2 = 0
    node = root
    lastNode = root

    while node is not None and cmp1 == cmp2:
        cmp1 = compare(node.info, v1)
        cmp2 = compare(node.info, v2)

        lastNode = node

        if cmp1 == -1:
            node = node.left
        elif cmp1 == 1:
            node = node.right
        else:
            node = None

    return lastNode

def compare(v1, v2):
    if v1 > v2:
        return -1
    elif v1 < v2:
        return 1
    return 0
