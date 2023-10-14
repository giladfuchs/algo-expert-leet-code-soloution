# This is an input class. Do not edit.
from algoexpert.LinkdLIstCreation import create_list


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    arr_one = []
    while linkedListOne is not None:
        arr_one.append(linkedListOne.value)
        linkedListOne = linkedListOne.next
    while linkedListTwo is not None:
        try:
            index = arr_one.index(linkedListTwo.value)
            temp = linkedListTwo
            while linkedListTwo is not None and index < len(arr_one):
                if linkedListTwo.value == arr_one[index]:
                    index += 1
                    linkedListTwo = linkedListTwo.next
                else:
                    break
            if linkedListTwo is None and index == len(arr_one):
                return temp
        except:
            pass

        # else:
        linkedListTwo = linkedListTwo.next

    return None


if __name__ == '__main__':
    he1 = create_list([
        {"id": "1", "next": "3", "value": 1},
        {"id": "2", "next": "3", "value": 2},

    ])
    he2 = create_list([
        {"id": "4", "next": "6", "value": 4},
        {"id": "2", "next": "6", "value": 2},

    ])
    print(mergingLinkedLists(he1, he2))
