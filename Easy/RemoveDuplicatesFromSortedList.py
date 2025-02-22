from typing import Optional
from DataStructures import ListNode

# Time complexity: O(n)
# Space complexity: O(n)


class LinearSpaceSolution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = ListNode(head.val)
        res_head = current

        while head.next is not None:
            if head.next.val != head.val:
                current.next = ListNode(head.next.val)
                current = current.next

            head = head.next

        return res_head


# Time complexity: O(n)
# Space complexity: O(1)


class ConstantSpaceSolution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next

            curr = curr.next

        return head
