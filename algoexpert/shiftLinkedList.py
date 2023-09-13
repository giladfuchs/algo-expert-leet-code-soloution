from algoexpert.LinkdLIstCreation import create_list


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    size = 0
    temp = head
    while temp:
        temp = temp.next
        size += 1
    k = k % size
    if k == 0:
        return head
    temp = head
    while size > k + 1:
        temp = temp.next
        size -= 1
    new_root = temp.next
    temp.next = None
    temp = new_root
    while temp and temp.next:
        temp = temp.next
    if temp:
        temp.next = head
    return new_root


if __name__ == '__main__':
    he1 = create_list([
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": None, "value": 5}
    ])
    a = shiftLinkedList(he1, 2)
    print()
