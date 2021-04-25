// Singly-linked lists are already defined with this interface:
function ListNode(x) {
  this.value = x;
  this.next = null;
}


function isListPalindrome(l) {
    const [leftList, rightList] = splitListInHalf(l); // O(n)
    const reversedRightList = reverseLinkedList(rightList); // O(n)

    let left = leftList;
    let right = reversedRightList;
    let response = true;

    // O(n)
    while (left) {
        response = response && (left.value === right.value);
        left = left.next;
        right = right.next;
    }

    // O(n)
    l = joinLists(leftList, reverseLinkedList(reversedRightList));

    return response
}

function splitListInHalf(l) {
    let lastSplitNode = null;
    let twoStepsNode = l;
    let splitNode = l;
    
    while (twoStepsNode && twoStepsNode.next) {
        twoStepsNode = twoStepsNode.next.next;
        lastSplitNode = splitNode;
        splitNode = splitNode.next;
    }

    if (lastSplitNode) {
        lastSplitNode.next = null;
    }

    return [l, splitNode];
}

function reverseLinkedList(l) {
    let node = l;
    let lastNode = null;
    let nextNode = null;

    while (node) {
        nextNode = node.next;
        node.next = lastNode;
        lastNode = node;
        node = nextNode;
    }

    return lastNode;
}

function joinLists(l, r) {
    let lastLeft = l;
    let left = l;

    while (left) {
        lastLeft = left;
        left = left.next;
    }

    if (lastLeft) {
        lastLeft.next = r;
    }

    return l;
}

function stringifyList(l) {
    let node = l;
    let string = "";

    while (node) {
        string += node.value + " ";
        node = node.next;
    }

    return string;
}

function main() {
    const node1 = new ListNode(0);
    const node2 = new ListNode(1);
    const node3 = new ListNode(1);
    const node4 = new ListNode(0);
    // const node5 = new ListNode(0);

    node1.next = node2;
    node2.next = node3;
    node3.next = node4;
    // node4.next = node5;

    console.log(stringifyList(node1));
    console.log(isListPalindrome(node1));
    console.log(stringifyList(node1));
}

main()
