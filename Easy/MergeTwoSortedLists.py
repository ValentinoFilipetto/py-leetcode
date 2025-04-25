from typing import Optional
from DataStructures import ListNode

# Pattern: Two Pointers
# Time complexity: O(n + m), where n and m are the list sizes
# Space complexity: O(1), as the algorithm uses a constant amount of extra space for the dummy node and pointers
# The merged list is constructed by reusing the nodes from the input lists,
# so no additional memory is allocated for the nodes themselves.


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
