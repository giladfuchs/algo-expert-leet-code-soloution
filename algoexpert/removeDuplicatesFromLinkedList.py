# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    temp: LinkedList = linkedList
    while temp != None:
        if temp.next and temp.next.value == temp.value:
            temp.next = temp.next.next
        else:
            temp = temp.next
    return linkedList


if __name__ == '__main__':
    a = LinkedList(1)
    a.next = LinkedList(3)
    a.next.next = LinkedList(4)
    a.next.next.next = LinkedList(5)
    a.next.next.next.next = LinkedList(6)
    b = removeDuplicatesFromLinkedList(a)
    print()
