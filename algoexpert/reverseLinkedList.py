from algoexpert.LinkdLIstCreation import LinkedList, create_list


def reverseLinkedList(head: LinkedList):
    if not head or not head.next:
        return head
    temp = reverseLinkedList(head.next)
    head.next.next = head
    head.next = None
    return temp


if __name__ == '__main__':
    he1 = create_list([
        {"id": "0", "next": "1", "value": 0},
        {"id": "1", "next": "2", "value": 1},
        {"id": "2", "next": "3", "value": 2},
        # {"id": "3", "next": "4", "value": 3},
        # {"id": "4", "next": "5", "value": 4},
        # {"id": "5", "next": None, "value": 5}
    ])
    a = reverseLinkedList(he1)
    print()
