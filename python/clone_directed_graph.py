class Node:
    def __init__(self, d):
        self.data = d
        self.neighbors = []

def clone(root):
    knownNodes = {}
    return _clone(root, knownNodes)

def _clone(node, knownNodes):
    if node in knownNodes:
        return knownNodes[node]

    copy = Node(node.data)
    knownNodes[node] = copy

    for neighbor in node.neighbors:
        neighborCopy = _clone(neighbor, knownNodes)
        copy.neighbors.append(neighborCopy)

    return copy

def printGraph(root):
    knownNodes = {}
    return _printGraph(root, knownNodes)

def _printGraph(node, knownNodes):
    if node in knownNodes:
        return

    knownNodes[node] = True
    neighborDatas = []

    for neighbor in node.neighbors:
        _printGraph(neighbor, knownNodes)
        neighborDatas.append(neighbor.data)

    print("Node:", node.data)
    print("Neighbors:", neighborDatas)


if __name__ == "__main__":
    node0 = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node0.neighbors = [node2, node3, node4]
    node1.neighbors = [node2]
    node2.neighbors = [node0]
    node3.neighbors = [node2]
    node4.neighbors = [node0, node1, node3]

    printGraph(node0)

    copy = clone(node0)

    print("---------")

    printGraph(copy)
