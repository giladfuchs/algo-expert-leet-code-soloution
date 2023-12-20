from typing import Optional

from leetcode.mergeKList import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return []

        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow.next
        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        slow.next = None
        node1, node2 = head, prev
        while node2 is not None:
            next_node = node1.next
            node1.next = node2
            node1 = node2
            node2 = next_node

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        res = head.next
        prev, cur = None, head
        while cur and cur.next:
            nextt = cur.next

            if prev:
                prev.next = nextt

            nextt.next, cur.next = cur, nextt.next
            prev, cur = cur, cur.next
        return res


print(Solution().swapPairs(ListNode(1, ListNode(2, ListNode(3, ListNode(4))))))
