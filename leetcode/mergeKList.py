class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional, List
import queue


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = queue.PriorityQueue()
        for i, node in enumerate(lists):
            pq.put((node.val, i))

        min_node = pq.get()
        head = ListNode(min_node[0])
        res = head
        if lists[min_node[1]].next:
            pq.put((lists[min_node[1]].next.val, min_node[1]))
            lists[min_node[1]] = lists[min_node[1]].next

        while not pq.empty():
            min_node = pq.get()
            res.next = ListNode(min_node[0])
            res = res.next

            if lists[min_node[1]].next:
                pq.put((lists[min_node[1]].next.val, min_node[1]))
                lists[min_node[1]] = lists[min_node[1]].next

        return head


# [1,4,5],[1,3,4],[2,6]
lst = [
    ListNode(1, ListNode(4, ListNode(5))),
    ListNode(1, ListNode(3, ListNode(4))),
    ListNode(2, ListNode(6)),
]
print(Solution().mergeKLists(lst))
