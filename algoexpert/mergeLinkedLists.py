from algoexpert.LinkdLIstCreation import LinkedList, create_list


def mergeLinkedLists(headOne, headTwo):
    res = LinkedList(-1)
    head_res=None
    while headOne and headTwo:
        if headOne.value<headTwo.value:
            val = headOne.value
            headOne = headOne.next
        else:
            val = headTwo.value
            headTwo = headTwo.next

        res.next = LinkedList(val)
        if head_res is None:
            head_res= res.next
        res=res.next
    while headOne  :
        val = headOne.value
        headOne = headOne.next
        res.next = LinkedList(val)
        res=res.next
    while headTwo  :
        val = headTwo.value
        headTwo = headTwo.next
        res.next = LinkedList(val)
        res=res.next
    # Write your code here.
    return head_res





if __name__ == '__main__':
    he1 = create_list([
        {"id": "1", "next": "3", "value": 1},
        {"id": "3", "next": "4", "value": 3},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": "9", "value": 5},
        {"id": "9", "next": "10", "value": 9},
        {"id": "10", "next": None, "value": 10}
    ])
    he2 = create_list([
        {"id": "2", "next": "6", "value": 2},
        {"id": "6", "next": "7", "value": 6},
        {"id": "7", "next": "8", "value": 7},
        {"id": "8", "next": None, "value": 8}
    ])
    print(mergeLinkedLists(he1, he2))
