# This is an input class. Do not edit.
from algoexpert.LinkdLIstCreation import create_list


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    slow_ptr = head.next
    fast_ptr = head.next.next
    while slow_ptr is not fast_ptr:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    res = head
    while res is not slow_ptr:
        slow_ptr = slow_ptr.next
        res = res.next
    return res


if __name__ == '__main__':
    he1 = create_list([
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "6", "value": 5},
        {"id": "6", "next": "2-2", "value": 6},
        {"id": "2-2", "next": "7", "value": 2},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": "9", "value": 8},
        {"id": "9", "next": "2-2", "value": 9}
    ])
    b = he1.next.next.next.next.next.next.next
    he1.next.next.next.next.next.next.next.next.next.next.next = b
    a = findLoop(he1)
    print()
