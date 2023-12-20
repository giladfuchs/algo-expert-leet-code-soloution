from algoexpert.LinkdLIstCreation import LinkedList


def removeDuplicatesFromLinkedList2(linkedList):
    # Write your code here.
    temp: LinkedList = linkedList
    while temp != None:
        if temp.next and temp.next.value == temp.value:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return linkedList


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    node = linkedList
    while node:
        temp = node.next
        while temp and temp.value == node.value: temp = temp.next
        node.next = temp
        node = node.next
    return linkedList


if __name__ == '__main__':
    a = LinkedList(1)
    a.next = LinkedList(3)
    a.next.next = LinkedList(4)
    a.next.next.next = LinkedList(5)
    a.next.next.next.next = LinkedList(6)
    b = removeDuplicatesFromLinkedList(a)
    print()
