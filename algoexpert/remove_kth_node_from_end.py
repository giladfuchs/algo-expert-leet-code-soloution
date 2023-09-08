# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head: LinkedList, k: int):
    # Write your code here.
    size: int = 0
    temp: LinkedList = head
    while temp.next:
        temp = temp.next
        size += 1
    steps: int = size - k
    i: int = 0
    temp: LinkedList = head
    while i < steps:
        temp = temp.next
        i += 1
    if steps == -1:
        head.value = head.next.value
    temp.next = temp.next.next
    print(head.value, temp.value)


def test():
    nodes = [
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": "9", "value": 8},
        {"id": "9", "next": None, "value": 9}
    ]
    node = LinkedList(nodes.pop(0).get('value'))
    tail = node
    for _ in nodes:
        tail.next = LinkedList(_.get('value'))
        tail = tail.next
    removeKthNodeFromEnd(node, 10)


if __name__ == '__main__':
    test()
