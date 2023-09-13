class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_list(ls):
    head = LinkedList(ls[0].get('value'))
    tail = LinkedList(ls[1].get('value'))
    head.next = tail
    for _ in ls[2:]:
        tail.next = LinkedList(_.get('value'))
        tail = tail.next
    return head
