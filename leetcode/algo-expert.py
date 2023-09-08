from typing import Optional


def isValidSubsequence(array, sequence):
    # Write your code here.
    i =0
    j = 0
    while i<len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j +=1
        i +=1

    return j==len(sequence)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_head_next(head: Optional[ListNode])->Optional[ListNode]:
    back_head = head
    head_local = head
    while  head_local.next is not None:
        # if head_local.next is None:
        #     break
        back_head = head_local
        head_local = head_local.next

    back_head.next=None
    return head_local


class Solution:
    def reverseUtil(self,head:ListNode, curr:ListNode, prev:ListNode):

        if curr.next is None:
            head = curr
            curr.next=prev
            return head
        next = curr.next
        curr.next =prev
        return self.reverseUtil(head, next, curr)
    def reorderList(self, head: Optional[ListNode]) -> None:
        node1 = head
        node2 = head
        while node2 is not None:
            node2 = node2.next
            if  node2 is not None:
                node2 = node2.next
            if  node2 is not None:
                node1 = node1.next
            else:
                node2 = node1
                node1 = node1.next
                node2.next=None
                break

        tail = self.reverseUtil(node1, node1, None)

        # head_ans = head
        while tail is not None and head is not None:
            temp_head = head.next
            head.next = tail
            head = head.next
            tail = tail.next
            head.next = temp_head
            head = temp_head




        """
        Do not return anything, modify head in-place instead.
        """

a = ListNode(1)
b=a
for i in range(2,5):
    b.next = ListNode(i)
    b = b.next

print(b)
Solution.reorderList(a)
print(a)
