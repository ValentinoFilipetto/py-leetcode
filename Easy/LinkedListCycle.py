from typing import Optional
from DataStructures import ListNode


# Time complexity: O(n)
# Space complexity: O(n)


class LinearSpaceSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seenValues = set()

        if not head:
            return False

        while head.next:
            if head in seenValues:
                return True

            seenValues.add(head)

            head = head.next

        return False


# Time complexity: O(n)
# Space complexity: O(1)


class ConstantSpaceSolution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
