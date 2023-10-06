def get_sum_of_linked_list(node):
    ans = ''
    while node:
        ans += str(node.value)
        node = node.next
    ans = int(ans[::-1])
    return ans


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    first_sum, second_sum = get_sum_of_linked_list(linkedListOne), get_sum_of_linked_list(linkedListTwo)
    merge_sum = str(first_sum + second_sum)[::-1]
    res = LinkedList(int(merge_sum[0]))
    temp = res
    for num in merge_sum[1:]:
        temp.next = LinkedList(int(num))
        temp = temp.next

    return res


from algoexpert.LinkdLIstCreation import LinkedList, create_list

if __name__ == '__main__':
    he1 = create_list([
        {"id": "2", "next": "4", "value": 2},
        {"id": "4", "next": "7", "value": 4},
        {"id": "7", "next": "1", "value": 7},
        {"id": "1", "next": None, "value": 1}
    ])
    he2 = create_list([
        {"id": "9", "next": "4", "value": 9},
        {"id": "4", "next": "5", "value": 4},
        {"id": "5", "next": None, "value": 5}
    ])
    print(sumOfLinkedLists(he1, he2))
