# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    step = linkedList
    step2 = linkedList

    while step2.next:
        step2 = step2.next
        step = step.next
        if step2.next:
            step2 = step2.next

    # Write your code here.
    return step
